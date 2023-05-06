#!bin/bash

mkdir archive

mv *.json archive/
mv q archive/dif-copy
zip -r archive-v7-2.zip archive
#rm -r archive

mkdir q
echo All is Done!


