#!/usr/bin/env python3
#
# build-xlsx - Generate a spread sheet from files
#
# USAGE
#
# (1) Output an empty sheet
#
#　   $ build-xlsx -o config.xlsx
#
# (2) Generate a filled sheet
#
#     $ build-xlsx esr60.txt esr68.txt verify-targets-to-chapters.csv
#
import re
import sys
import glob
import getopt
import csv
import os

BASEDIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(BASEDIR)

import adlib
try:
    import xlsxwriter
except ImportError:
    print('ERROR: Please install xlswriter to run this script\n')
    print('  $ sudo apt install python3-xlsxwriter\n')
    sys.exit(1)

#
# Global settings

ESR_PREVIOUS = 'esr60'
ESR_CURRENT = 'esr68'
CHAPTERS_CSV = 'verify-targets-to-chapters.csv'

WORKBOOK_DEF = [
    ('基本設定', [
        'Install',
        'Application',
        'Admin',
        'Security',
        'Privacy',
        'Startup',
        'Websearch',
        'Location',
        'Download',
        'Tab',
        'Network',
        'Update',
        'Ui',
        'Script',
        'Plugin',
        'External',
        'Stability',
        'Appearance',
        'Performance',
        'Addon-IEView',
        'Addon-FireIE',
        'Addon-Acrobat',
    ]),
    ('機能無効化', [
        'MenuShortcut',
    ]),
]

DEFAULT_FORMAT = {
    'valign': 'top',
    'border': 1,
    'font_size': 8,
    'font_name': 'MS Gothic',
    'text_wrap': 1
}

#
# XLSX writer

def is_deprecated(x):
    return '廃止' in x

def count_options(conf):
    return sum(len(item['opts']) for item in conf)

def create_formats(wb):
    def new_format(**kwargs):
        return wb.add_format(dict(DEFAULT_FORMAT, **kwargs))
    return {
        'default':          new_format(),
        'noborder':         new_format(border=0),
        'center':           new_format(align='center'),
        'deprecated':       new_format(bg_color='#dddddd'),
        'question':         new_format(bg_color='#90ee90'),
        'selected':         new_format(bg_color='#fffa95'),
        'selected_changed': new_format(bg_color='#ffb571'),
    }

def write_legend(sheet, formats, row):
    sheet.write(row, 1, '', formats['selected'])
    sheet.write(row, 2, '前バージョンから引き続き利用する項目', formats['noborder'])
    sheet.write(row + 1, 1, '', formats['selected_changed'])
    sheet.write(row + 1, 2, '前バージョンから異同がある項目', formats['noborder'])
    sheet.write(row + 2, 1, '', formats['deprecated'])
    sheet.write(row + 2, 2, '廃止済みの項目', formats['noborder'])

def write_header(sheet, formats):
    curr = ESR_CURRENT.upper()
    prev = ESR_PREVIOUS.upper()
    fmt = formats['center']

    sheet.freeze_panes(1, 0)

    sheet.write(0, 0, 'カテゴリー', fmt)
    sheet.write(0, 1, '項目設定番号', fmt)
    sheet.write(0, 2, 'カスタマイズ項目 (目的)', fmt)
    sheet.write(0, 3, '状態', fmt)
    sheet.write(0, 4, '選択肢番号', fmt)
    sheet.write(0, 5, '選択肢', fmt)
    sheet.write(0, 6, '設定内容の雛形\n(%s)' % curr, fmt)
    sheet.write(0, 7, '最終的に反映した設定値\n(%s)' % curr, fmt)
    sheet.write(0, 8, '%s→%sでの変更' % (prev, curr), fmt)
    sheet.write(0, 9, '検証手順書対応番号', fmt)
    sheet.write(0, 11, '設定内容の雛形\n(%s)' % prev, fmt)
    sheet.write(0, 12, '最終的に反映した設定値\n(%s)' % prev, fmt)

    sheet.set_row(0, 25)
    sheet.set_column(0, 12, None, formats['default'])
    sheet.set_column(0, 0, 10)
    sheet.set_column(1, 1, 10)
    sheet.set_column(2, 2, 30)
    sheet.set_column(3, 3, 5)
    sheet.set_column(4, 4, 5)
    sheet.set_column(5, 5, 20)
    sheet.set_column(6, 6, 40)
    sheet.set_column(7, 7, 40)
    sheet.set_column(8, 8, 10)
    sheet.set_column(9, 9, 10)
    sheet.set_column(10, 10, 12)
    sheet.set_column(11, 11, 40)
    sheet.set_column(12, 12, 40)

def generate_xlsx(wb, conf_curr, conf_prev, chapters, excludes):
    formats = create_formats(wb)

    for title, files in WORKBOOK_DEF:
        if title in excludes:
            continue

        sheet = wb.add_worksheet(title)
        write_header(sheet, formats)

        row = 1
        for fn in files:
            curr = adlib.load(os.path.join(BASEDIR, ESR_CURRENT, fn))
            prev = adlib.load_as_dict(os.path.join(BASEDIR, ESR_PREVIOUS, fn))
            sheet.merge_range(row, 0, row + count_options(curr) - 1, 0, '')

            for item in curr:
                if len(item['opts']) > 1:
                    sheet.merge_range(row, 1, row + len(item['opts']) - 1, 1, '')
                    sheet.merge_range(row, 2, row + len(item['opts']) - 1, 2, '')

                for opt in item['opts']:
                    selected = ''
                    status = ''
                    chapter = ''
                    fmt = formats['default']
                    item_fmt = formats['default']
                    opt_id = opt['opt_id']

                    if is_deprecated(item['item_title']):
                        item_fmt = formats['deprecated']
                        fmt = formats['deprecated']
                    elif is_deprecated(opt['opt_title']):
                        fmt = formats['deprecated']
                    elif opt_id in conf_curr:
                        selected = 'y'
                        chapter = chapters.get(opt_id, '省略')
                        if opt_id not in conf_prev:
                            fmt, status = formats['selected_changed'], '新規'
                        elif conf_prev[opt_id] != conf_curr[opt_id]:
                            fmt, status = formats['selected_changed'], '変更あり'
                        else:
                            fmt, status = formats['selected'], ''

                    sheet.write(row, 0, fn, formats['default'])
                    sheet.write(row, 1, int(item['item_no']), item_fmt)
                    sheet.write(row, 2, item['item_title'], item_fmt)
                    sheet.write(row, 3, selected, fmt)
                    sheet.write(row, 4, int(opt['opt_no']), fmt)
                    sheet.write(row, 5, opt['opt_title'], fmt)
                    sheet.write(row, 6, opt['conf'].strip(), fmt)
                    sheet.write(row, 7, conf_curr.get(opt_id, ''), fmt)
                    sheet.write(row, 8, status, fmt)
                    sheet.write(row, 9, chapter, formats['default'])
                    sheet.write(row, 10, '', formats['noborder'])
                    sheet.write(row, 11, prev.get(opt_id, ''), fmt)
                    sheet.write(row, 12, conf_prev.get(opt_id, ''), fmt)
                    row += 1
        write_legend(sheet, formats, row+1)

#
# main

def load_chapters(path):
    try:
        with open(path) as fp:
            return dict(csv.reader(fp))
    except FileNotFoundError:
        return {}

def main(args):
    conf_curr = {}
    conf_prev = {}
    chapters = {}
    outfile = 'config.xlsx'
    excludes = []

    opts, args = getopt.getopt(args, 'o:x:')
    for k, v in opts:
        if k == '-o':
            outfile = v
        elif k == '-x':
            excludes = v.split(',')

    for arg in args:
        if ESR_CURRENT in arg:
            print('%s -> %s' % (ESR_CURRENT, arg))
            conf_curr = adlib.load_as_dict(arg)
        elif ESR_PREVIOUS in arg:
            print('%s -> %s' % (ESR_PREVIOUS, arg))
            conf_prev = adlib.load_as_dict(arg)
        elif CHAPTERS_CSV in arg:
            print('Loading', os.path.basename(arg))
            chapters = load_chapters(arg)

    with xlsxwriter.Workbook(outfile) as wb:
        generate_xlsx(wb, conf_curr, conf_prev, chapters, excludes)

    print('Generated:', wb.filename)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
