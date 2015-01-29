
SPECDIR="./specs"
PKGLIST="./specs.list"

mkdir -p $SPECDIR
rm $SPECDIR/*

for pkg in $(cat $PKGLIST); do
    echo $pkg
    dap2rpm $pkg > $SPECDIR/devassistant-dap-$pkg.spec
done

