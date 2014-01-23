#!/bin/bash

# Purpose: kill firefox foreground process
# Author: Lek
# Created Date: 2014-01-22
# Updated Date: 

kill -9 $(ps -x | grep 'firefox' | grep foreground | awk '{print $1}')