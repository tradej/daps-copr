#!/bin/bash

SOURCES=$PWD/specs/
RESULTS=$PWD/rpms/
TMP=$PWD/tmp/
RPMBUILDDIR=~/rpmbuild/

rm -rf $RESULTS $TMP

mkdir $RESULTS $TMP

pushd $TMP

for spec in ${SOURCES}/*.spec; do
    pkg=$(basename $spec | sed -e 's/\.spec$//')
    echo Rebuilding $pkg
    cp $spec .

    spectool -g $pkg.spec &> /dev/null
    cp *.dap $RPMBUILDDIR/SOURCES
    rm $RPMBUILDDIR/SRPMS/$pkg*src.rpm 2> /dev/null
    rpmbuild -bs $pkg.spec || return 1
    cp $RPMBUILDDIR/SRPMS/$pkg*src.rpm $RESULTS

    rm -f *
done

popd # tmp


