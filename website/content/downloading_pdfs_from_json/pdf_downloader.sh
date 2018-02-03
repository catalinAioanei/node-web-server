#!/bin/sh

file="urls.txt"
COUNTER=0
MULT=0
while IFS= read -r line
do
  MULT=0
  file="$COUNTER.zip"
  if [ -f "$file"]
  then mv "$file" "$logfile($MULT).zip"
  fi
  wget -O "$file" "$line"
  unzip -n $file
  rm $file
  let COUNTER=COUNTER+1
	printf '%s\n' "$line"
done <"$file"
