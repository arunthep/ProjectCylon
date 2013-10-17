# -*- coding: utf-8 -*- 
import string
import argparse
import csv

global debug
global systemdebug
global extractmode

import time as tm

import platform
if platform.system() == 'Windows':
	SEPARATOR = "\\"
else:
	EPARATOR = "/"
systemdebug=0
debug=0

parser = argparse.ArgumentParser(description='PageObject Creator Utility')
parser.add_argument('--InputFile', dest='inputfile', action='store',
                   help='input csv filename')
parser.add_argument('--OutputDir', dest='outputdir', action='store',
                   help='output directory')
				   
args = parser.parse_args()
csvfile = None
outputdir = "."
if (args.inputfile is not None):
	csvfile = open( args.inputfile )
if (args.outputdir is not None):
	outputdir = args.outputdir
if csvfile is None:
	print "ERROR invalid inputfile"
	assert False
ClassName = ""
PageTitle = ""
PageURL = ""
NeedLogin = False
LoginFunction = ""
ElementList = []

inputfile = csv.reader( csvfile, delimiter=',', quotechar='"' )

columnlist = {'ObjectName':1,'Name':2,'LocatingMethod':3,'Locator':4,'PreCheck':5,'ObjectType':6,'DefaultState':7,'Image':8,'Link':9,'DefaultValue':10,'Lable':11,'AvailableValue':12, 'CheckAttribute':13}

for row in inputfile:
	if row[0] == "Name:":
		ClassName = row[1]
	if row[0] == "Title:":
		PageTitle = row[1]
	if row[0] == "URL:":
		PageURL = row[1]
	if row[0] == "NeedLogin:":
		NeedLogin = (row[1]=="TRUE") #Excel auto convert to capital
	if row[0] == "LoginFunction:":
		LoginFunction = row[1]
	
	
	if row[0] == "##Elements##":
		for column in columnlist:
			columnlist[column] = -1
		for i in range(len(row)):
			for column in columnlist:
				if row[i] == column:
					columnlist[column] = i

	if row[0] == "Element:":
		item ={}
		for column in columnlist:
			if columnlist[column] != -1:
				item[column] = row[columnlist[column]]
			else:
				item[column] = ""
		
		ElementList.append(item)
		
		
if ClassName == "":
	print "ERROR Name not found"
	assert False
if PageTitle == "":
	print "ERROR Title not found"
	assert False
text = ""
text+="# -*- coding: utf-8 -*- \n"
text+="from framework.PageRefObFramework import *\n"
text+="class {ClassName}Class(Page):\n".format(ClassName=ClassName)
for Element in ElementList:
	text+="\t"+Element["ObjectName"]+ " = None\n" 
text+="\tdef __init__(self):\n"
text+='\t\tsuper( {ClassName}Class, self ).__init__( name="{ClassName}", title="{PageTitle}", url="{PageURL}", needlogin={NeedLogin}, loginfunction="{LoginFunction}"  )\n'.format(ClassName=ClassName, PageTitle=PageTitle, PageURL=PageURL, NeedLogin=NeedLogin, LoginFunction=LoginFunction )
for Element in ElementList:
	text+="\t\tself." + Element["ObjectName"] + " = Element (\n"
	text+="\t\t\t\tname=\"" + Element["Name"] +"\",\n"
	text+="\t\t\t\tparent=self,\n"
	if Element["PreCheck"] != "":
		text+="\t\t\t\tfunctionbeforecheckelement=self." + Element["PreCheck"] +",\n"
	if Element["LocatingMethod"] != "":
		text+="\t\t\t\tlocatingmethod=\"" + Element["LocatingMethod"] +"\",\n"
	if Element["Locator"] != "":
		text+="\t\t\t\tlocator='" + Element["Locator"] +"',\n"
	if Element["ObjectType"] != '':
		text+="\t\t\t\tobjecttype=\"" + Element["ObjectType"] +"\",\n"
	if Element["DefaultState"] != '':
		text+="\t\t\t\tdefaultstate=\"" + Element["DefaultState"] +"\",\n"
	if Element["Image"] != '':
		text+="\t\t\t\timage=\"" + Element["Image"] +"\",\n"
	if Element["Link"] != '':
		text+="\t\t\t\tlink=\"" + Element["Link"] +"\",\n"
	if Element["AvailableValue"] != '':
		availablevalue = Element["AvailableValue"].split("\n")
		# print str(availablevalue)
		# for i in range(len(availablevalue)):
			# print str(i+1) + " : " + str(availablevalue[i])
		text+="\t\t\t\tavailablevalue=" + str(availablevalue) +",\n"
	if Element["CheckAttribute"] != '':
		checkattribute = Element["CheckAttribute"].split("\n")
		text+="\t\t\t\tcheckattribute=" + str(checkattribute) +",\n"
	if Element["DefaultValue"] != '':
			text+="\t\t\t\tdefaultvalue=u\"" + Element["DefaultValue"] +"\",\n"
	if Element["Lable"] != '':
		text+="\t\t\t\tlable=u\"" + Element["Lable"] +"\",\n"
	text+="\t\t\t\t)\n"
text+= "{ClassName} = {ClassName}Class()".format(ClassName=ClassName)

filename = outputdir+SEPARATOR+ClassName+".py"

print "Output filename = " + filename
fo = open(filename, 'w')
fo.write(text)
