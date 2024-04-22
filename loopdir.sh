#!/bin/sh
command=$1
dirs=`find . -maxdepth 1 -mindepth 1 -type d`
for d in $dirs;
do
    echo "exec command in" $d
    cd $d
    $1
    cd ..
done

    
