#!/usr/bin/bash

if [ $# -lt 1 ]; then
    echo 'You must specify prefix!'
    return 1
fi

PREFIX="$1"

DAPS=$(
for dap in $(ls rpms); do
    echo $PREFIX/$dap
done
)

if [ ! $(which xsel) ]; then
    echo -e $DAPS
else
    echo -e $DAPS | xsel
    echo 'Names copied to X clipboard'
fi
