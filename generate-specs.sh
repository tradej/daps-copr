
SPECDIR="./specs"
PKGLIST="./specs.list"

mkdir -p $SPECDIR
rm $SPECDIR/*

for pkg in $(cat $PKGLIST); do
    dap2rpm $pkg > $SPECDIR/dap-$pkg.spec
done

