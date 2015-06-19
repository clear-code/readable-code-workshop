# リーダブルな例

## 複数の値用の変数の名前には複数形を使う

https://github.com/toshi0383/toshi0383-readable-code/blob/master/src/Recipe.java#L43

```java
	List<String> recipes = new ArrayList<String>();
```

理由:

「recipes」というように変数名が複数形になっているので、複数の値が入っ
ていることがわかりやすい。

## ファイルからレシピを読み込む処理を別関数に分けている

https://github.com/toshi0383/toshi0383-readable-code/blob/master/src/Recipe.java#L42

```java
	for (String recipe : getLinesFromFileName(fileName)) {
        System.out.println(recipe);
    }
// ...
	public static List<String> getLinesFromFileName(String recipeFileName) {
// ...
    }
```

処理の塊が何をしているのかわかりやすい。

変更するときに他の処理に影響が及びにくい。
