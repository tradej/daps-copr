#!/usr/bin/bash

if [ $# -lt 1 ]; then
    echo 'You must specify prefix!'
    return 1
fi

PREFIX="$1"

DAPS=$(
for dap in $(ls specs); do
    echo $PREFIX/$dap
done
)

if [ ! $(which xsel) ]; then
    echo $DAPS
else
    echo $DAPS | xsel
    echo 'Names copied to X clipboard'
fi
