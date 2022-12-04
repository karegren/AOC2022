#!/bin/sh
if [ ! -d "$1" ]; then
    mkdir $1
    touch $1/input.txt $1/puzzle.py $1/debug.txt
    echo "def task_1(values):
    return

def task_2(values):
    return

input = open('input.txt', 'r')
values = input.readlines()
print(task_1(values))
print(task_2(values))
" >> $1/puzzle.py
    echo "$1/ created!"
else
    echo "Files for day $1 already exist"
fi