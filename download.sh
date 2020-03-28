#!/usr/bin/bash
{ 
    date -u +'%Y-%m-%d %H:%M:%S UTC:'; 
    # kaggle datasets download sudalairajkumar/covid19-in-italy -p output --unzip --force;
} | tr "\n" " " >> log/execution.log
echo "" >> log.txt