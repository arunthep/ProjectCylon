#!/bin/sh


for i in *.csv
do
    python ./GenPageObject.py --InputFile "$i" --OutputDir ./../pageobject   
done

rm ./../pageobject/AllPages.py

echo #All Page Objects > ./../pageobject/AllPages.py

# regular expression
for i in `ls -1 ./../pageobject/*Page.py | sed 's/.\/..\/pageobject\///' | sed 's/\..*$//'`
do
         
	echo "from $i import * " >> ./../pageobject/AllPages.py
done

