# トラブルシューティング

2014/06/22に開催した第1回目のリーダブルコード勉強会ではここにあげたよう
なトラブルが発生しました。このようなトラブルが発生しないように事前に対
策しておくと、当日は「リーダブルコードの勉強」に集中できます。参加前に
一度確認してください。

なお、多くの人はトラブルが発生しませんでした。発生したのは数人です。そ
のため、多くの人はここに書かれていることは問題なく実行できるはずです。

## Git・GitHub関連

トラブルの多くはGit・GitHub関連でした。この勉強会では基本的な使い方しか
しません。そのため、まだよくわかっていない人でも次に書いていることだけ
できるようになっておけば「リーダブルコードの勉強」に集中できます。まだ
よくわかっていない人は確認してください。

  * GitHub: 自分のリポジトリーの作成
  * GitHub: 他の人のリポジトリーをfork
  * Git: `git clone`
  * Git: `git add`
  * Git: `git commit`
  * Git: `git push`

なお、トラブルが発生していた人の多くはGitHub for Windowsなど専用のツー
ルを使っている人たちでした。Webブラウザーとgitコマンドを使っている人で
トラブルが発生している人はほとんどいませんでした。

専用ツールを使っている人は専用ツールで同じことができることを確認してく
ださい。

### GitHub: 自分のリポジトリーの作成

自分のリポジトリーの作成方法はGitHubに説明があります。英語ですが、スク
リーンショットが付いているのでここを読みながらやってみましょう。英語は
20段落もなく、簡単な英語なので落ち着いて読めばなにを書いているかわかり
ます。落ち着いて読みましょう。

[Creating a new repository · GitHub Help](https://help.github.com/articles/creating-a-new-repository)

Webブラウザーではなく、GitHub for Windowsなど専用ツールを使っている人は
専用ツールでも自分のリポジトリーを作成できることを確認してください。

### GitHub: 他の人のリポジトリーをfork

他の人のリポジトリーをforkする方法もGitHubに説明があります。英語1文とス
クリーンショットで説明しています。

[Fork A Repo · GitHub Help - Step 1: Fork the "Spoon-Knife" repository](https://help.github.com/articles/fork-a-repo#step-1-fork-the-spoon-knife-repository)

forkの練習には
[この勉強会用のリポジトリー](https://github.com/clear-code/sezemi-2014-readable-code)
を使ってください。

Webブラウザーではなく、GitHub for Windowsなど専用ツールを使っている人は
専用ツールでも他の人のリポジトリーをforkできることを確認してください。

### Git: `git clone`

`git clone` で作成した自分のリポジトリーをcloneできることを確認してくだ
さい。

SSHで接続したい人は適切にSSHを設定していることを確認してください。SSHの
鍵をたくさん持っている場合は `~/.ssh/config` に `Host` を設定しなければ
いけないかもしれません。

gitコマンドではなく、GitHub for Windowsなど専用ツールを使っている人は専
用ツールでも自分のリポジトリーをcloneできることを確認してください。

### Git: `git add`

新しく `README.md` を作って `git add` してください。gitコマンドではなく、
GitHub for Windowsなど専用ツールを使っている人は専用ツールでやってくだ
さい。

注意: `README.md` はプログラムを書く時に使うテキストエディターやIDEで作っ
てください。Webブラウザーなどプログラムを書く時に使わないものでは作らな
いでください。それでは動作確認にならないからです。

`git add` については [Git - 変更内容のリポジトリへの記録 - 新しいファイルの追跡](http://git-scm.com/book/ja/Git-%E3%81%AE%E5%9F%BA%E6%9C%AC-%E5%A4%89%E6%9B%B4%E5%86%85%E5%AE%B9%E3%81%AE%E3%83%AA%E3%83%9D%E3%82%B8%E3%83%88%E3%83%AA%E3%81%B8%E3%81%AE%E8%A8%98%E9%8C%B2#%E6%96%B0%E3%81%97%E3%81%84%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%AE%E8%BF%BD%E8%B7%A1) を参考にしてください。

### Git: `git commit`

`git add` した `README.md` を `git commit` してください。gitコマンドで
はなく、GitHub for Windowsなど専用ツールを使っている人は専用ツールでやっ
てください。

`git commit` については [Git - 変更内容のリポジトリへの記録 - 変更のコミット](http://git-scm.com/book/ja/Git-%E3%81%AE%E5%9F%BA%E6%9C%AC-%E5%A4%89%E6%9B%B4%E5%86%85%E5%AE%B9%E3%81%AE%E3%83%AA%E3%83%9D%E3%82%B8%E3%83%88%E3%83%AA%E3%81%B8%E3%81%AE%E8%A8%98%E9%8C%B2#%E5%A4%89%E6%9B%B4%E3%81%AE%E3%82%B3%E3%83%9F%E3%83%83%E3%83%88) を参考にしてください。

### Git: `git push`

`git commit` したコミットを `git push` してください。gitコマンドではな
く、GitHub for Windowsなど専用ツールを使っている人は専用ツールでやって
ください。

SSHで接続したい人は適切にSSHを設定していることを確認してください。SSHの
鍵をたくさん持っている場合は `~/.ssh/config` に `Host` を設定しなければ
いけないかもしれません。

`git push` については [Git - リモートでの作業 - リモートへのプッシュ](http://git-scm.com/book/ja/Git-%E3%81%AE%E5%9F%BA%E6%9C%AC-%E3%83%AA%E3%83%A2%E3%83%BC%E3%83%88%E3%81%A7%E3%81%AE%E4%BD%9C%E6%A5%AD#%E3%83%AA%E3%83%A2%E3%83%BC%E3%83%88%E3%81%B8%E3%81%AE%E3%83%97%E3%83%83%E3%82%B7%E3%83%A5) を参考にしてください。

## Java関連

Eclipse関連でいくつかトラブルがありました。Eclipseを使う予定の人は次の
ことを確認してください。

  * Gitとの連携
  * コマンドラインでもビルド・実行できるようにする

### Gitとの連携

EclipseからGitを使う場合はうまく動作するか確認してください。前述のGitの
確認手順をEclipseでもできるかどうかで確認できます。

EclipseからGitを使うのではなく、GitHub for Windowsなど別のツールでGitを
使う場合はEclipseで編集して別のツールでGitを操作できるか確認してくださ
い。確認方法は前述の通りです。

### コマンドラインでもビルド・実行できるようにする

勉強会の中で他の人と実装を交換します。実装を交換した人がコマンドライン
で `java` と `javac` コマンドを使っていた場合、交換後は `java` と
`javac` コマンドを使う必要がでてくる可能性があります。

そのため、念のため、コマンドラインから `java` と `javac` コマンドを使え
るようにしておいてください。もう少し言うと、 `PATH` と `JAVA_HOME` 環境
変数を自分の環境にあわせて適切に設定し、 `javac -version` でバージョン
情報を取得できることを確認してください。
