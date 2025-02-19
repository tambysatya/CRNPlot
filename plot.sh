
#!/usr/bin/bash

INPUT_DIR=$1 #`basename $1`
OUTPUT_DIR=$2 #`basename $2`

if [ -z ${1+x} ] || [ -z ${2+x} ];
then
	echo "usage: ./plot.sh INPUT_DIR OUTPUT_DIR"
	exit 1
fi

for mdl in `ls $INPUT_DIR`
do
	PREFIX=`basename $mdl .xml`
	input="$INPUT_DIR/$mdl"
	cnr="$OUTPUT_DIR/${PREFIX}_cnr.svg"
	ig="$OUTPUT_DIR/${PREFIX}_ig.svg"
	qg="$OUTPUT_DIR/${PREFIX}_qg.svg"
	python main.py -i $input -cnr $cnr -ig $ig -qg $qg --remove_dot
done
