#!/bin/sh
file='sortflag.txt'
while [ true ]
do
       clear
       python same.py
       cat "$file"
       sleep 1
done


