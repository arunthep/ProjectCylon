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
if platform.system() == 'Windows':
	import colorama
	colorama.init()
else:
	pass
 
def printc(text, color):
	"""Print in color."""
	if usecolor == True:
		print "\033["+codeCodes[color]+"m"+text+"\033[0m",
	else:
		print text,
	
def writec(text, color):
	"""Write to stdout in color."""
	if usecolor == True:
		sys.stdout.write("\033["+codeCodes[color]+"m"+text+"\033[0m")
	else:
		sys.stdout.write(text)
		
def switchColor(color):
	"""Switch console color."""
	sys.stdout.write("\033["+codeCodes[color]+"m")
	
try:

	for Page in World.PageList:
		if Page.needlogin == False:
			print "Testing : ",
			printc( Page.title, 'bright cyan')
			print ( " at url : " + Page.url)
			Page.Go()
			if Page.Verify():
				print "Test Page : "+Page.title + " : "
				printc( "[OK]", 'bright green')
				print "\n"
			else:
				print "Test Page : "+Page.title + " : "
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