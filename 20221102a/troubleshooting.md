# トラブルシューティング

トラブルが発生したときに備えて事前に対策しておくと、当日は「リーダブルコードを持ち帰るための体験」に集中できます。参加前に一度確認してください。

## Git・GitHub関連

過去のトラブルの多くはGit・GitHub関連でした。この講座では基本的な使い方しかしないので、次に書いていることだけできるようになっておけば「リーダブルコードを持ち帰るための体験」に集中できます。まだよくわかっていない人は確認してください。

  * GitHub: 自分のリポジトリーの作成
  * GitHub: 他の人のリポジトリーをfork
  * Git: `git clone`
  * Git: `git add`
  * Git: `git commit`
  * Git: `git push`

なお、トラブルが発生していた人の多くはGitHub for Windowsなど専用のツールを使っている人たちでした。Webブラウザーとgitコマンドを使っている人でトラブルが発生している人はほとんどいませんでした。専用ツールを使っている人は、専用ツールで同じことができることを確認してください。

Gitの使い方をまったく知らない人が一通りのことを学ぶには、以下の書籍がお薦めです。

[改訂2版 わかばちゃんと学ぶ Git使い方入門（湊川 あい 著、DQNEO 監修）](https://www.amazon.co.jp/dp/4863543433/


### GitHub: 自分のリポジトリーの作成

自分のリポジトリーの作成方法はGitHubに説明があります。英語ですが、スクリーンショットが付いているのでここを読みながらやってみましょう。英語は20段落もなく、簡単な英語なので落ち着いて読めばなにを書いているかわかります。落ち着いて読みましょう。

[Creating a new repository · GitHub Help](https://help.github.com/articles/creating-a-new-repository)

Webブラウザーではなく、GitHub for Windowsなど専用ツールを使っている人は専用ツールでも自分のリポジトリーを作成できることを確認してください。

### GitHub: 他の人のリポジトリーをfork

他の人のリポジトリーをforkする方法もGitHubに説明があります。英語1文とスクリーンショットで説明しています。

[Fork A Repo · GitHub Help - Step 1: Fork the "Spoon-Knife" repository](https://help.github.com/articles/fork-a-repo#step-1-fork-the-spoon-knife-repository)

forkの練習には[この講座用のリポジトリー](https://github.com/clear-code/readable-code-workshop)を使ってください。

Webブラウザーではなく、GitHub for Windowsなど専用ツールを使っている人は専用ツールでも他の人のリポジトリーをforkできることを確認してください。

### Git: `git clone`

`git clone` で作成した自分のリポジトリーをcloneできることを確認してください。

SSHで接続したい人は適切にSSHを設定していることを確認してください。SSHの鍵をたくさん持っている場合は `~/.ssh/config` に `Host` を設定しなければいけないかもしれません。

gitコマンドではなく、GitHub for Windowsなど専用ツールを使っている人は専用ツールでも自分のリポジトリーをcloneできることを確認してください。

### Git: `git add`

新しく `README.md` を作って `git add` してください。gitコマンドではなく、GitHub for Windowsなど専用ツールを使っている人は専用ツールでやってください。

注意: `README.md` はプログラムを書く時に使うテキストエディターやIDEで作ってください。Webブラウザーなどプログラムを書く時に使わないものでは作らないでください。それでは動作確認にならないからです。

`git add` については [Git - 変更内容のリポジトリへの記録 - 新しいファイルの追跡](http://git-scm.com/book/ja/Git-%E3%81%AE%E5%9F%BA%E6%9C%AC-%E5%A4%89%E6%9B%B4%E5%86%85%E5%AE%B9%E3%81%AE%E3%83%AA%E3%83%9D%E3%82%B8%E3%83%88%E3%83%AA%E3%81%B8%E3%81%AE%E8%A8%98%E9%8C%B2#%E6%96%B0%E3%81%97%E3%81%84%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%AE%E8%BF%BD%E8%B7%A1) を参考にしてください。

### Git: `git commit`

`git add` した `README.md` を `git commit` してください。gitコマンドではなく、GitHub for Windowsなど専用ツールを使っている人は専用ツールでやってください。

`git commit` については [Git - 変更内容のリポジトリへの記録 - 変更のコミット](http://git-scm.com/book/ja/Git-%E3%81%AE%E5%9F%BA%E6%9C%AC-%E5%A4%89%E6%9B%B4%E5%86%85%E5%AE%B9%E3%81%AE%E3%83%AA%E3%83%9D%E3%82%B8%E3%83%88%E3%83%AA%E3%81%B8%E3%81%AE%E8%A8%98%E9%8C%B2#%E5%A4%89%E6%9B%B4%E3%81%AE%E3%82%B3%E3%83%9F%E3%83%83%E3%83%88) を参考にしてください。

### Git: `git push`

`git commit` したコミットを `git push` してください。gitコマンドではなく、GitHub for Windowsなど専用ツールを使っている人は専用ツールでやってください。

SSHで接続したい人は適切にSSHを設定していることを確認してください。SSHの鍵をたくさん持っている場合は `~/.ssh/config` に `Host` を設定しなければいけないかもしれません。

`git push` については [Git - リモートでの作業 - リモートへのプッシュ](http://git-scm.com/book/ja/Git-%E3%81%AE%E5%9F%BA%E6%9C%AC-%E3%83%AA%E3%83%A2%E3%83%BC%E3%83%88%E3%81%A7%E3%81%AE%E4%BD%9C%E6%A5%AD#%E3%83%AA%E3%83%A2%E3%83%BC%E3%83%88%E3%81%B8%E3%81%AE%E3%83%97%E3%83%83%E3%82%B7%E3%83%A5) を参考にしてください。

## Java関連

Eclipse関連でいくつかトラブルがありました。Eclipseを使う予定の人は次のことを確認してください。

  * Gitとの連携
  * コマンドラインでもビルド・実行できるようにする

### Gitとの連携

EclipseからGitを使う場合はうまく動作するか確認してください。前述のGitの確認手順をEclipseでもできるかどうかで確認できます。

EclipseからGitを使うのではなく、GitHub for Windowsなど別のツールでGitを使う場合はEclipseで編集して別のツールでGitを操作できるか確認してください。確認方法は前述の通りです。

EclipseからEGitを使う手順は以下を参考にしてください。

#### Gitリポジトリー作成手順

  1. Javaプロジェクト作成
    * メニューバー -> File -> New -> Java Project
  2. プロジェクトを右クリック -> Team -> Share Projectを選択
  3. Gitを選択
  4. 「Use or create repository in parent folder of project」にチェック
  5. Create Repositoryを押してFinish

#### remoteの登録手順

  1. メニューバー -> Window -> Show View -> Other -> Git -> Git Repositoriesを選択
  2. Git RepositoriesビューのRecipe/Remotesを右クリック
  3. Create Remote
  4. remote名（originなど）を入力
  5. GitHubで作成したリポジトリーのURLを入力

#### commit手順

  1. プロジェクトまたはファイルを右クリック -> Team -> Commitを選択
  2. コミットするファイルを選択（プロジェクトを右クリックした場合）
  3. コミットメッセージを入力
  4. CommitまたはCommit and Pushを押す

#### コミットログ確認手順

  1. Git RepositoriesビューのRecipeを右クリック
  2. Show In -> Historyを選択
  3. （右クリックからpushもできます）

#### clone手順

  1. メニューバー -> File -> Importを選択
  2. Git -> Projects from Gitを選択
  3. Clone URIを選択
  4. フォークしたGitHubリポジトリーのURLを入力
  5. ブランチ（master）を選択
  6. あとはデフォルトのまま数回Nextを押してFinish
  7. Git Repositoriesビューにクローンしたリポジトリーが表示されればOK

### コマンドラインでもビルド・実行できるようにする

講座の中で他の人と実装を交換します。実装を交換した人がコマンドラインで `java` と `javac` コマンドを使っていた場合、交換後は `java` と`javac` コマンドを使う必要がでてくる可能性があります。

そのため、念のため、コマンドラインから `java` と `javac` コマンドを使えるようにしておいてください。もう少し言うと、 `PATH` と `JAVA_HOME` 環境変数を自分の環境にあわせて適切に設定し、 `javac -version` でバージョン情報を取得できることを確認してください。

なお、Eclipseで作成されたプロジェクトをコマンドラインでコンパイルする場合は、以下の手順を参考にしてください。

```bash
$ javac -d bin/ src/net/myokoym/recipe/*.java
$ java -cp bin/ net.myokoym.recipe.Recipe
```


