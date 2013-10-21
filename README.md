ProjectCylon
============

Selenium Automate Testing Example

Install
=======

Windows Platform

1. install vc redist (Microsoft Visual C++ 2010 Redistributable Package)

2. install python 2.7 (http://www.python.org/download/releases/2.7/)

3. add path to python 2.7 and scripts and openssl (C:\Python27;C:\Python27\Scripts;C:\Python27\Lib\site-packages;)

4. install pywin (http://sourceforge.net/projects/pywin32/files/pywin32/  select latest build and select correct python version)

5. install python setuptool (https://pypi.python.org/pypi/setuptools/0.9.6#installation-instructions)

6. easy_install pip

7. pip install selenium

8. pip install behave==1.2.2
NOTE: do not use verion 1.2.3 or above -- there is an issue with Thai language.

9. pip install colorama

10. extract ansicon and run ansicon -i (check 32 / 64 bits version)
	+ You can download it here: https://github.com/adoxa/ansicon/downloads
	+ Read the detailed instructions here: http://www.kevwebdev.com/blog/in-search-of-a-better-windows-console-using-ansicon-console2-and-git-bash.html
		+ Focus at section "ANSI escape sequence support with ansicon"

11. Git clone ProjectCylon

12. Install Thai Font for CMD
	+ extract ThaiLang4CMD.zip
	+ install font Courmon.ttf to windows fonts folder
	+ run ThaiLangInDOS.reg
	+ restart machine
	+ run cmd windows and set font to courier mono thai and set font size to 24

13. Make Python able to run Thai

	+ edit C:\Python27\Lib\site.py
	+ find the following 2 rows and comment them out:
		#if hasattr(sys, "setdefaultencoding"):
			#del sys.setdefaultencoding

	+ create sitecustomize.py file at C:\Python27\Lib\site-packages with the following content
		import sys
		reload(sys)
		sys.setdefaultencoding("utf-8")

14. Change Language for non-Unicode program to Thai (Region and Language -> Administrative -> Language for non-Unicode program)

15. Restart machine

How to use
==========

- clear all .py files in \pageobject\ (except __init__)
- edit csv files in \pageobjectdefinition\
- run GenAllPageObject.bat
- run CheckElements.bat to check pageobject
- edit features file in \features\ (format and example: http://pythonhosted.org/behave/tutorial.html#feature-files)
- edit steps file in \features\steps\
- run RunBDDColor.bat to check test
