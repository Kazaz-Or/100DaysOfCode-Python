#!/bin/bash

echo "date is $1"
log=$(git log --pretty=format:"%w(100,2,2)%s %w(72,0,0)<%an> (%ar)%n\n" origin/develop)
echo "***********************"
echo -e $log
echo "***********************"
echo -e ::set-output name=log::$log
