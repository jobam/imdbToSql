#!/bin/bash

_path='ftp.funet.fi/pub/mirrors/ftp.imdb.com/pub/temporaryaccess/'
_destFolder='input_list_files/'
declare -a _files=("aka-names.list.gz" "actors.list.gz" "actresses.list.gz" "movies.list.gz" "aka-titles.list.gz" "genres.list.gz" "keywords.list.gz")

echo "======Download Files=========="

for i in "${_files[@]}"
do
	wget -m ftp://anonymous@"$_path/$i" -O ./"$_destFolder$i"
done

echo "====Now Unzipping files====="

for i in "${_files[@]}"
do
	gunzip "$_destFolder$i"
done

echo "====Clean====="

rm -f *.gz