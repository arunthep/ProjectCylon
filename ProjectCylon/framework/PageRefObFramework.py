# -*- coding: utf-8 -*-
from framework.WorldContext import *
from urlparse import urlparse
from selenium.common.exceptions import NoSuchElementException
import sys
import time

# == Use Color ==#
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


codeCodes = {
    'black':    '0;30', 'bright gray':  '0;37',
    'blue':     '0;34', 'white':        '1;37',
    'green':    '0;32', 'bright blue':  '1;34',
    'cyan':     '0;36', 'bright green': '1;32',
    'red':      '0;31', 'bright cyan':  '1;36',
    'purple':   '0;35', 'bright red':   '1;31',
    'yellow':   '0;33', 'bright purple':'1;35',
    'dark gray':'1;30', 'bright yellow':'1;33',
    'normal':   '0'
}

def printc(text, color):
    """Print in color."""
    if usecolor == True:
        print "\033[" + codeCodes[color] + "m" + text + "\033[0m",
    else:
        print text,

def writec(text, color):
    """Write to stdout in color."""
    if usecolor == True:
        sys.stdout.write("\033[" + codeCodes[color] + "m" + text + "\033[0m")
    else:
        sys.stdout.write(text)

def switchColor(color):
    """Switch console color."""
    sys.stdout.write("\033[" + codeCodes[color] + "m")


class Element(object):
    name = ""
    locatingmethod = "name"
    locator = ""
    label = ""
    parent = None
    functionbeforecheckelement = None
    objecttype = None
    defaultstate = None
    defaultvalue = None
    availablevalue = None
    checkattribute = None

    def __init__(self,
                  name="",
                  parent=None,
                  locatingmethod="name",
                  locator="",
                  functionbeforecheckelement=None,
                  objecttype=None ,
                  defaultstate=None,
                  defaultvalue=None,
                  availablevalue=None,
                  checkattribute=None,
                  ):
        self.name = name
        self.locatingmethod = locatingmethod.lower()
        self.locator = locator
        self.parent = parent
        World.ElementList.append(self)
        self.functionbeforecheckelement = functionbeforecheckelement
        self.objecttype = objecttype
        self.defaultstate = defaultstate
        self.defaultvalue = defaultvalue
        self.availablevalue = availablevalue
        self.checkattribute = checkattribute

    def check_exists(self):
        if self.locatingmethod == "name":
            try:
                World.driver.find_element_by_name(self.locator)
            except NoSuchElementException:
                return False
            return True
        elif self.locatingmethod == "xpath":
            try:
                World.driver.find_element_by_xpath(self.locator)
            except NoSuchElementException:
                return False
            return True
        else:
            print "Invalid Locator Method"
            return False

    def Get(self):
        element = None

        wait = ui.WebDriverWait(World.driver, 3)
        try:
            # print "checking"
            wait.until(lambda driver : self.check_exists() != False)
        except:
            pass

        try:
            if self.locatingmethod == "name":
                element = World.driver.find_element_by_name(self.locator)
            elif self.locatingmethod == "xpath":
                element = World.driver.find_element_by_xpath(self.locator)
        except:
            pass
        return element

    def Click(self):
        if(self.Verify() == False):
            return False
        element = self.Get()
        element.click()
        return True

#Verify Enable and Disable ---------------------------------------------------------------------------
    def VerifyIsEnabled(self):
        if(self.Verify() == False):
            return False
        element = self.Get()
        print(" VerifyIsEnabled : ",)
        if(element.is_enabled() == True):
            printc("passed" + "\n", "bright green")
            return True
        else:
            printc("failed" + "\n", "bright red")
            return False

    def VerifyIsDisabled(self):
        if(self.Verify() == False):
            return False
        element = self.Get()
        print(" VerifyIsDisabled : ",)
        if(element.is_enabled() == False):
            printc("passed" + "\n", "bright green")
            return True
        else:
            printc("failed" + "\n", "bright red")
            return False
#Verify Enable and Disable ---------------------------------------------------------------------------

#Verify Check and Uncheck ----------------------------------------------------------------------------

    def VerifyIsChecked(self):
        if(self.Verify() == False):
            return False
        element = self.Get()
        print(" VerifyIsChecked : ",)
        if(element.is_selected() == True):
            printc("passed" + "\n", "bright green")
            return True
        else:
            printc("failed" + "\n", "bright red")
            return False

    def VerifyIsUncheck(self):
        if(self.Verify() == False):
            return False
        element = self.Get()
        print(" VerifyIsUncheck : ",)
        if(element.is_selected() == False):
            printc("passed" + "\n", "bright green")
            return True
        else:
            printc("failed" + "\n", "bright red")
            return False
#Verify Check and Uncheck ----------------------------------------------------------------------------

    def Verify(self):
        if self.parent is not None:
            if(self.parent.Verify() == False):
                return False
        element = self.Get()
        if element is None:
            return False
        return True

    def VerifyUI(self):
        if self.parent is not None:
            if(self.parent.Verify() == False):
                return False
        element = self.Get()

        if element is None:
            return False
        overallresult = True

        if self.objecttype is not None:
            if self.VerifyAttribute('type', self.objecttype) == False:
                overallresult = False

        if self.defaultstate is not None:

            if self.defaultstate == 'Enable':
                if self.VerifyIsEnable() == False:
                    overallresult = False
            elif self.defaultstate == 'Disable':
                if self.VerifyDisable() == False:
                    overallresult = False

            elif self.defaultstate == 'True':
                if self.VerifyIsCheck() == False:
                    overallresult = False
            elif self.defaultstate == 'False':
                if self.VerifyIsUncheck() == False:
                    overallresult = False

            else :
                print "Invalid Default State : " + (self.defaultstate)
                overallresult = False

        if self.defaultvalue is not None:
            if self.VerifyValue(self.defaultvalue) == False:
                    overallresult = False

        if self.availablevalue is not None:
            element = self.Get()
            for i in range(len(self.availablevalue)):
                options = element.find_element_by_xpath('//option')
                print options
                # if self.VerifyAttribute(self.availablevalue[i]) == False:
                    # overallresult = False

        if self.checkattribute is not None:
            element = self.Get()
            print self.checkattribute
            # for i in range(len(self.checkattribute)):
            for i in self.checkattribute:
                for j in i.split('|'):
                    # row = self.checkattribute[j].split("=")
                    row = j.strip().split("=")
                    if self.VerifyAttribute(row[0], row[1]) == False:
                        overallresult = False

        return(overallresult)

    def VerifyNotexist(self):
        if self.parent is not None:
            if(self.parent.Verify() != True):
                print 'Error parent incorrect'
                return False
        element = self.Get()
        if element is None:
            return True
        return False

    def SendKeys(self, textinput):
        textinput = World.ConvertValue(textinput)
        if self.parent is not None:
            if(self.parent.Verify() == False):
                return False
        element = self.Get()
        element.send_keys(textinput)
        return True

    def SendKeysByScript(self, textinput):
        textinput = World.ConvertValue(textinput)
        if self.parent is not None:
            if(self.parent.Verify() == False):
                return False
        element = self.Get()
        script = "arguments[0].value = '" + textinput + "'"
        World.driver.execute_script(script, element)
        return True

    def VerifyText(self, expectedresult):
        if(self.Verify() != True):
            return False
        element = self.Get()
        resultText = str(element.text.encode('utf-8', 'ignore'))
        resultValue = element.get_attribute('value')
        if resultValue is not None:
            resultValue = str(resultValue.encode('utf-8', 'ignore'))
        else:
            resultValue = ""
        # World.DebugToFile('self.locator=' + self.locator)
        # World.DebugToFile('resultText=' + resultText)
        # World.DebugToFile('resultValue=' + resultValue)
        expectedresult = str(World.ConvertValue(expectedresult).encode('utf-8', 'ignore'))
        # World.DebugToFile('expectedresult=' + expectedresult)
        if expectedresult == "":
            print " Verify Text : '<blank>' : ",
            if resultText == "" and resultValue == "":
                printc("passed\n", "bright green")
                return True
            else:
                printc("failed\n", "bright red")
                print "Got '",
                printc(str(resultText) + str(resultValue) + "'\n", "bright yellow")
                return False
        else :
            print " Verify Text : '" + str(expectedresult) + "': ",
            if resultText.find(expectedresult) != -1 or resultValue.find(expectedresult) != -1:
                printc("passed\n", "bright green")
                return True
            else:
                printc("failed", "bright red")
                print "Got '",
                printc(str(resultText) + str(resultValue) + "'\n", "bright yellow")
                return False

    def VerifyValue(self, value):
        if(self.Verify() != True):
            return
        element = self.Get()
        result = str(element.text.encode('utf-8', 'ignore'))
        value = str(World.ConvertValue(value).encode('utf-8', 'ignore'))
        # print str(element.text)
        if value == "":
            if result == "":
                print " Verify Value : <blank> passed"
                return True
            else:
                print " Verify Value : <blank> failed got " + result + " instead"
                return False
        else :
            if result.find(value) != -1:
                print " Verify Value : " + str(value) + " passed"
                return True
            else:
                print " Verify Value : " + str(value) + " failed got " + result + " instead"
                return False

    def VerifyAttribute(self, attributename, expectedresult):
        if(self.Verify() != True):
            return False
        element = self.Get()
        result = str(element.get_attribute(attributename).encode('utf-8', 'ignore'))
        expectedresult = str(expectedresult.encode('utf-8', 'ignore'))
        if expectedresult[0] == '"' and expectedresult[len(expectedresult) - 1] == '"':
            expectedresult = expectedresult[1:len(expectedresult) - 1]
        print " Verify ",
        printc(str(attributename), 'bright yellow')
        print ":",
        printc(str(expectedresult), 'bright yellow')
        if result.find(expectedresult) != -1:
            printc("passed\n", 'bright green')
            return True
        else:
            printc("failed", 'bright red')
            print "got",
            printc(result, 'bright red')
            print "instead"
            return False

    def IsBlank(self):
        if(self.Verify() != True):
            return False
        element = self.Get()
        textValue = str(element.text.encode('utf-8', 'ignore'))
        currentValue = element.get_attribute('value')
        if currentValue is not None:
            currentValue = str(currentValue.encode('utf-8', 'ignore'))
        else:
            currentValue = ""
        if textValue != "" or currentValue != "" :
            return False
        else:
            return True

    def HasValue(self):
        return self.IsBlank() != True

class Page(object):
    name = ""
    title = ""
    url = ""
    needlogin = False
    loginfunction = ""
    pageverifymethod = "Title"

    def __init__(self,
                  name="",
                  title="",
                  url="",
                  needlogin=False,
                  loginfunction="",
                  pageverifymethod="Title",):
            self.name = World.appendSuffix(name, World.PAGE_SUFFIX)
            self.title = title
            self.url = url
            self.needlogin = needlogin
            self.loginfunction = loginfunction
            self.pageverifymethod = pageverifymethod
            World.PageList.append(self)

    def Go(self):
        # World.GoTo( self.url )
        World.GoToPage(self)
        time.sleep(2)
        return self.Verify()

    def Verify(self):
        World.CurrentPageVerified = False
        if self.pageverifymethod.lower() == "title" or self.pageverifymethod.lower() == "any":
            if self.VerifyPageWithTitle() == True:
                World.CurrentPageVerified = True
                World.CurrentPageVerifiedPageName = self.name
                return True
        if self.pageverifymethod.lower() == "url" or self.pageverifymethod.lower() == "any":
            if self.VerifyPageWithURL() == True:
                World.CurrentPageVerified = True
                World.CurrentPageVerifiedPageName = self.name
                return True
        return False

    def VerifyPageWithTitle(self, title=None):
        if title is None:
            title = self.title
        wait = ui.WebDriverWait(World.driver, 10)
        try:
            wait.until(lambda driver : World.driver.title.lower().find(title.lower()) != -1)
        except:
            pass
        if(World.driver.title.lower().find(title.lower()) != -1):
            return True
        else:
            print "Incorrect Page"
            return False

    def VerifyPageWithURL(self , url=None):
        if url is None:
            url = self.url
        url1 = urlparse(url)
        targeturl = url1.netloc + url1.path

        wait = ui.WebDriverWait(World.driver, 10)
        try:
            wait.until(lambda driver : World.driver.current_url.lower().find(targeturl.lower()) != -1)
        except:
            pass
        if(World.driver.current_url.lower().find(targeturl.lower()) != -1):
            return True
        else:
            print "Incorrect Page"
            return False
