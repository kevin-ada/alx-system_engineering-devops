#!/usr/bin/env bash

count=0

var="Best School"

until [ $count -eq 10 ]
do
	echo "$var"
	count=$((count+1))
done
