#!/bin/sh


python ./GenPageObject.py --InputFile "$1" --OutputDir ./../pageobject

rm ./../pageobject/AllPages.py

echo #All Page Objects > ./../pageobject/AllPages.py

#regular expression: 
for i in `ls -1 ./../pageobject/*Page.py | sed 's/.\/..\/pageobject\///' | sed 's/\..*$//'`
do
         
	echo "from $i import * " >> ./../pageobject/AllPages.py
done

