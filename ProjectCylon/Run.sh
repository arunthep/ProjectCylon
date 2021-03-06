#!/bin/bash

# Purpose: Generate Object and run Automated test
# Author: Lek
# Created Date: 2013-10-09
# Updated Date: 2013-10-25: Refactor, add option 3,4, help
#               2013-10-28: Add ClearPY() function


# Print out Menu Function
Menu(){
echo "----------------[`basename ${0}`]-------------------"
echo " USAGE $./Run.sh <option>          "
echo " <option> = "
echo " DEFAULT | VOID | ANY :: GENERATE -> RUN"
echo " 1:: RUN ONLY"
echo " 2:: CHECKELEMENT ONLY"
echo " 3:: GENERATE ONLY"
echo " 10:: GENERATE -> RUN"
echo " 20:: GENERATE -> CHECK"
echo " 100:: GENERATE -> CHECK -> RUN"
echo ""
echo " kill:: KILL FIREFOX"
echo " h:: SHOW MENU"
echo "-------------------------------------------"
}

# Clear All .py file at pageobject dir except __init__.py*
ClearPY(){
    ls pageobject/* | grep -v "__init__.py*" | xargs rm -f    
}

# Generate Object Function
Generate(){

    ClearPY
    cd pageobjectdefinition
    ./GenAllPageObject.sh
    cd ../
    echo "GENERATE OBJECT(S): END"
}

# Generate Object Function
GenerateSingleObject(){
    echo "filename: $2"
    ClearPY
    cd pageobjectdefinition
    ./GenSinglePageObject.sh "$Input2"
    cd ../
    echo "GENERATE OBJECT(S): END"
}

# Run behave Function
Run(){
    #echo "ENTER RUN FUNCTION"
    behave --logging-level INFO --color --no-source --no-skipped    
}

RunWithTag(){
    #echo "ENTER RunWithTag FUNCTION"

    behave --logging-level INFO --color --no-source --no-skipped --tags "$Input2"    
}

# Check Element Function
Check(){
    python CheckElements.py 
}

Kill_Firefox(){
    ps -ef | grep "firefox" | grep "foreground" | awk '{print $2}' | xargs kill
}

# Main Command
Menu
OPTION="$1"
Input2="$2"
echo "TAG: $TAG"

Kill_Firefox

case "$OPTION" in

    1) Run
    ;;
    2) Check
    ;;
    3) Generate
    ;;
    10) Generate; Run
    ;;
    20) Generate; Check
    ;;
    100) Generate; Check; Run
    ;;
    [hH] | help | HELP ) Menu
    ;;
    --tags) Generate; RunWithTag
    ;;
    --gensingle) GenerateSingleObject
    ;;         
    *) Generate; Run
    ;;
esac




