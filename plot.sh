
#!/usr/bin/bash

INPUT_DIR=`basename $1`
OUTPUT_DIR=`basename $2`

if [ -z ${1+x} ] || [ -z ${2+x} ];
then
	echo "usage: ./plot.sh INPUT_DIR OUTPUT_DIR"
	exit 1
fi
for mdl in `ls $INPUT_DIR`
do
	PREFIX=`basename $mdl .xml`
	input="$INPUT_DIR/$mdl"
	cnr="$OUTPUT_DIR/${PREFIX}_cnr.png"
	ig="$OUTPUT_DIR/${PREFIX}_ig.png"
	qg="$OUTPUT_DIR/${PREFIX}_qg.png"
	python main.py -i $input -cnr $cnr -ig $ig -qg $qg #--remove_dot
done
