#!/bin/bash

DEST=/mnt/fedorapeople/reviews/daps

for dap in $(cat specs.list); do
    echo ${dap}
    dapdir=${DEST}/devassistant-dap-${dap}/0/
    mkdir -p ${dapdir}
    cp specs/devassistant-dap-${dap}.spec ${dapdir}
    cp rpms/devassistant-dap-${dap}-* ${dapdir}
done
