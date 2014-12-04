#!/bin/bash

SOURCES=$PWD/specs/
RESULTS=$PWD/daps/
TMP=$PWD/tmp/
RPMBUILDDIR=~/rpmbuild/

rm -rf $RESULTS $TMP

mkdir $RESULTS $TMP

pushd $TMP

for spec in ${SOURCES}/*.spec; do
    pkg=$(basename $spec | sed -e 's/\.spec$//')
    echo Rebuilding $pkg
    cp $spec .

    spectool -g $pkg.spec
    cp *.dap $RPMBUILDDIR/SOURCES
    rm $RPMBUILDDIR/SRPMS/$pkg*src.rpm
    rpmbuild -bs $pkg.spec
    cp $RPMBUILDDIR/SRPMS/$pkg*src.rpm $RESULTS

    rm -f *
done

popd # tmp


