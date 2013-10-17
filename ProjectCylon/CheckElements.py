# -*- coding: utf-8 -*- #
from framework.WorldContext import *
World = WorldContext.Instance()

import pageobject.AllPages

import sys
 
codeCodes = {
	'black':    '0;30',     'bright gray':  '0;37',
	'blue':     '0;34',     'white':        '1;37',
	'green':    '0;32',     'bright blue':  '1;34',
	'cyan':     '0;36',     'bright green': '1;32',
	'red':      '0;31',     'bright cyan':  '1;36',
	'purple':   '0;35',     'bright red':   '1;31',
	'yellow':   '0;33',     'bright purple':'1;35',
	'dark gray':'1;30',     'bright yellow':'1;33',
	'normal':   '0'
}

#== Use Color ==#
usecolor = True
# before changing to true, run "pip install colorama" in commandline
# and uncomment the 2 lines below first
#

import platform
if platform.system() == 'Windows':
	import colorama
	colorama.init()
else:
	pass
 
def printc(text, color = None):
	"""Print in color."""
	if usecolor == True and color != None:
		print "\033["+codeCodes[color]+"m"+text.decode('utf-8')+"\033[0m",
	else:
		print text.decode('utf-8'),
	
def writec(text, color = None):
	"""Write to stdout in color."""
	if usecolor == True and color != None:
		sys.stdout.write("\033["+codeCodes[color]+"m"+text.decode('utf-8')+"\033[0m")
	else:
		sys.stdout.write(text.decode('utf-8'))
		
def switchColor(color):
	"""Switch console color."""
	sys.stdout.write("\033["+codeCodes[color]+"m")
	
try:

	for Page in World.PageList:
		if Page.needlogin == False:
			printc( "Testing : " )
			printc( Page.name, 'bright cyan' )
			printc( " : " )
			printc( Page.title, 'bright cyan' )
			printc( " at url : " + Page.url )
			Page.Go()
			if Page.Verify():
				printc( "Test Page : "+Page.title + " : \n" )
				printc( "[OK]\n", 'bright green')
			else:
				printc( "Test Page : "+Page.title + " : \n" )
				printc( "[FAIL]\n", 'bright red')
			
			for Element in World.ElementList:
				if Element.parent == Page:
					printc( "Testing : " )
					printc(  Element.name, 'bright blue')
					printc( " at : " + Element.locator + "\n" )
					if Element.parent.Verify() == False or Element.functionbeforecheckelement is not None:
						Element.parent.Go()
					try:
						if Element.functionbeforecheckelement is not None:
							Element.functionbeforecheckelement()
							time.sleep(3)
					except:
						pass
					if Element.VerifyUI():
						print "Test Element : "+Element.name+ " : "
						printc( "[OK]", 'bright green')
						print "\n"
					else:
						print "Test Element : "+Element.name+ " : "
						printc( "[FAIL]", 'bright red')
						print "\n"
			print "=============================== End page ====================================="
			
	for Page in World.PageList:
		if Page.needlogin == True:
			print "Testing : ",
			printc( Page.name, 'bright cyan')
			print ( " at url : " + Page.url)
			World.Login(Page.loginfunction)
			Page.Go()
			print "Test Page : "+Page.name + " : "
			if Page.Verify():
				printc( "[OK]", 'bright green')
				print "\n"
			else:
				printc( "[FAIL]", 'bright red')
				print "\n"
			
			for Element in World.ElementList:
				if Element.parent == Page:
					print "Testing : ",
					printc(  Element.name, 'bright blue')
					print " at : " + Element.locator
					if Element.parent.Verify() == False or Element.functionbeforecheckelement is not None:
						Element.parent.Go()
					try:
						if Element.functionbeforecheckelement is not None:
							Element.functionbeforecheckelement()
							time.sleep(3)
					except:
						pass
					if Element.VerifyUI():
						print "Test Element : "+Element.name+ " : "
						printc( "[OK]", 'bright green')
						print "\n"
					else:
						print "Test Element : "+Element.name+ " : "
						printc( "[FAIL]", 'bright red')
						print "\n"
			print "=============================== End page ====================================="
except Exception as e:
	print e
	pass
#World.driver.quit()
