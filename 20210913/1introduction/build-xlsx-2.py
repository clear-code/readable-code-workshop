#!/usr/bin/env python3
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
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
#     $ build-xlsx esr68.txt esr78.txt ... verify-targets-to-chapters.csv
#     $ build-xlsx -p esr68.txt -c esr78.txt
#     $ build-xlsx -d ESR68:esr68.txt -d ESR78:esr78.txt -d "ESR78 variation:esr78-variation.txt"
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

ESR_PREVIOUS = 'esr78'
ESR_CURRENT = 'esr91'
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

def sanitize_conf(conf):
    return re.sub(' *[^:]+:\n', '', conf).strip()

def create_formats(wb):
    def new_format(**kwargs):
        return wb.add_format(dict(DEFAULT_FORMAT, **kwargs))
    return {
        'default':          new_format(),
        'noborder':         new_format(border=0),
        'center':           new_format(align='center'),
        'changed':          new_format(bold=True),
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

def write_header(sheet, formats, conf):
    fmt = formats['center']

    sheet.freeze_panes(1, 0)

    sheet.write(0, 0, 'カテゴリー', fmt)
    sheet.write(0, 1, '項目設定番号', fmt)
    sheet.write(0, 2, 'カスタマイズ項目 (目的)', fmt)
    sheet.write(0, 3, '選択肢番号', fmt)
    sheet.write(0, 4, '選択肢', fmt)
    sheet.write(0, 5, '設定内容の雛形\n(%s)' % ESR_CURRENT.upper(), fmt)

    col_count = 5
    prev_key = ESR_PREVIOUS.upper()
    for key in conf.keys():
        if key == ESR_PREVIOUS.upper():
            continue
        sheet.write(0, col_count+1, '反映した設定値\n(%s)' % key, fmt)
        sheet.write(0, col_count+2, '%s→%sでの変更' % (prev_key, key), fmt)
        sheet.set_column(col_count+1, col_count+1, 40)
        sheet.set_column(col_count+2, col_count+2, 10)
        col_count+=2
        prev_key = key

    sheet.write(0, col_count+1, '検証手順書対応番号', fmt)
    sheet.write(0, col_count+3, '設定内容の雛形\n(%s)' % ESR_PREVIOUS.upper(), fmt)
    sheet.write(0, col_count+4, '反映した設定値\n(%s)' % ESR_PREVIOUS.upper(), fmt)

    sheet.set_row(0, 25)
    sheet.set_column(0, 0, 10)
    sheet.set_column(1, 1, 10)
    sheet.set_column(2, 2, 30)
    sheet.set_column(3, 3, 5)
    sheet.set_column(4, 4, 20)
    sheet.set_column(5, 5, 40)

    sheet.set_column(col_count+1, col_count+1, 10)
    sheet.set_column(col_count+2, col_count+2, 12)
    sheet.set_column(col_count+3, col_count+3, 40)
    sheet.set_column(col_count+4, col_count+4, 40)
    col_count+=4

    sheet.set_column(0, col_count, None, formats['default'])

def generate_xlsx(wb, conf, chapters, excludes):
    formats = create_formats(wb)
    prev_conf = conf[ESR_PREVIOUS.upper()]

    for title, files in WORKBOOK_DEF:
        if title in excludes:
            continue

        sheet = wb.add_worksheet(title)
        write_header(sheet, formats, conf)

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
                    status = ''
                    chapter = ''
                    fmt = formats['default']
                    item_fmt = formats['default']
                    opt_id = opt['opt_id']

                    applied_prev_conf = prev_conf.get(opt_id, {'conf':''})['conf']
                    template_curr_conf = opt['conf'].strip()
                    template_prev_conf = prev.get(opt_id, {'conf':''})['conf']

                    if is_deprecated(item['item_title']):
                        item_fmt = formats['deprecated']

                    col_count = 5
                    base_conf = prev_conf
                    applied_base_conf = applied_prev_conf
                    for key, variation_conf in conf.items():
                        if key == key == ESR_PREVIOUS.upper():
                            continue

                        variation_status = ''
                        variation_fmt = ''
                        applied_variation_conf = variation_conf.get(opt_id, {'conf':''})['conf']

                        if is_deprecated(item['item_title']) or is_deprecated(opt['opt_title']):
                            variation_fmt = formats['deprecated']
                        elif opt_id in variation_conf:
                            chapter = chapters.get(opt_id, '省略')
                            if opt_id not in base_conf:
                                variation_fmt, variation_status = formats['selected_changed'], '新規'
                            elif sanitize_conf(applied_base_conf) != sanitize_conf(applied_variation_conf):
                                variation_fmt, variation_status = formats['selected_changed'], '変更あり'
                            else:
                                variation_fmt, variation_status = formats['selected'], ''
                        elif base_conf == prev_conf:
                            if sanitize_conf(template_curr_conf) != sanitize_conf(template_prev_conf):
                              chapter = chapters.get(opt_id, '省略')
                              if template_prev_conf == '':
                                  variation_fmt, variation_status = formats['changed'], '新規（未設定）'
                              else:
                                  variation_fmt, variation_status = formats['changed'], '変更あり（未設定）'
                        else:
                            if sanitize_conf(applied_base_conf) != sanitize_conf(applied_variation_conf):
                                variation_status = '削除'

                        if base_conf == prev_conf:
                          fmt = variation_fmt

                        sheet.write(row, col_count+1, applied_variation_conf, variation_fmt)
                        sheet.write(row, col_count+2, variation_status, variation_fmt)
                        col_count+=2
                        base_conf = variation_conf
                        applied_base_conf = applied_variation_conf

                    sheet.write(row, 0, fn, formats['default']) # A
                    sheet.write(row, 1, int(item['item_no']), item_fmt) # B
                    sheet.write(row, 2, item['item_title'], item_fmt) # C
                    sheet.write(row, 3, int(opt['opt_no']), fmt) # D
                    sheet.write(row, 4, opt['opt_title'], fmt) # E
                    sheet.write(row, 5, template_curr_conf, fmt) # F

                    sheet.write(row, col_count+1, chapter, formats['default'])
                    sheet.write(row, col_count+2, '', formats['noborder'])
                    sheet.write(row, col_count+3, template_prev_conf, fmt)
                    sheet.write(row, col_count+4, applied_prev_conf, fmt)
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
    conf = {}
    chapters = {}
    outfile = 'config.xlsx'
    excludes = []

    opts, args = getopt.getopt(args, 'o:x:p:c:d:')
    for k, v in opts:
        if k == '-o':
            outfile = v
        elif k == '-x':
            excludes = v.split(',')
        elif k == '-p':
            conf[ESR_PREVIOUS.upper()] = v
        elif k == '-c':
            conf[ESR_CURRENT.upper()] = v
        elif k == '-d':
            parts = v.split(':', 1)
            conf[parts[0]] = parts[1]

    for arg in args:
        if ESR_PREVIOUS in arg and not ESR_PREVIOUS.upper() in conf:
            print('%s -> %s' % (ESR_PREVIOUS, arg))
            conf[ESR_PREVIOUS.upper()] = arg
        elif ESR_CURRENT in arg and not ESR_CURRENT.upper() in conf:
            print('%s -> %s' % (ESR_CURRENT, arg))
            conf[ESR_CURRENT.upper()] = arg
        elif CHAPTERS_CSV in arg:
            print('Loading', os.path.basename(arg))
            chapters = load_chapters(arg)

    for label, path in conf.items():
        conf[label] = adlib.load_as_dict(path)

    with xlsxwriter.Workbook(outfile) as wb:
        generate_xlsx(wb, conf, chapters, excludes)

    print('Generated:', wb.filename)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
