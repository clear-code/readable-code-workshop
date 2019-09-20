# リーダブルな例

## 複数の値用の変数の名前には複数形を使う

```java
	List<String> terms = new ArrayList<String>();
```

理由:

「terms」というように変数名が複数形になっているので、複数の値が入っ
ていることがわかりやすい。

## ファイルから単語情報を読み込む処理を別関数に分けている

```java
	for (String term : getLinesFromFileName(fileName)) {
        System.out.println(term);
    }
// ...
	public static List<String> getLinesFromFileName(String termsFileName) {
// ...
    }
```

処理の塊が何をしているのかわかりやすい。

変更するときに他の処理に影響が及びにくい。
