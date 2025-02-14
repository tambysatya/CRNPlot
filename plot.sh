
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
	input="$INPUT_DIR/$mdl"
	output="$OUTPUT_DIR/`basename $mdl xml`png"
	python main.py -i $input -o $output
done
