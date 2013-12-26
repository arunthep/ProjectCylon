# -*- coding: utf-8 -*-
import os
import time
import sys
reload(sys); sys.setdefaultencoding('utf-8')

from selenium                          import webdriver
from selenium.webdriver                import *
from selenium.common.exceptions        import TimeoutException
from selenium.webdriver.support.ui     import WebDriverWait
from selenium.webdriver.support        import expected_conditions as EC
import selenium.webdriver.support.ui                              as ui
import time

class Singleton:
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.

    The decorated class can define one `__init__` function that
    takes only the `self` argument. Other than that, there are
    no restrictions that apply to the decorated class.

    To get the singleton instance, use the `Instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.

    Limitations: The decorated class cannot be inherited from.

    """

    def __init__(self, decorated):
        self._decorated = decorated

    def Instance(self):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.

        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)

@Singleton
class WorldContext:
    driver = None
    MasterList = {}
    ElementList = []
    PageList = []
    cdmlogin = False
    dsflogin = False
    CurrentPage = None
    CurrentPageVerified = False
    CurrentPageVerifiedPageName = None
    _instance = None
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        pass
    def DebugToFile(self, message=None, logFileName='cylon_debug.log'):
        openFlag='w'
        if message is not None and message.strip() != '' and logFileName is not None and logFileName.strip() !='':
            if os.path.isfile(logFileName): openFlag = 'a'
            with open(logFileName, openFlag) as fhandle:
                fhandle.write(time.strftime('%m/%d/%Y %I:%M:%S %p ') + ' ' + message + '\n')
    def GetData(self, inputfile=None, outputdata=None):
        pass
    def GoToURL(self, url):
        self.driver.get(url)
        time.sleep(1)
    def GoToPage(self, Page):
        self.CurrentPage = Page
        self.driver.get(Page.url)
        time.sleep(1)
    def FindPage(self, PageName):
        for Page in self.PageList:
            if Page.name.lower() == PageName.lower():
                return Page
        print "Page not found in PageList"
        assert False
    def FindElement(self, Name):
        for Element in self.ElementList:
            if Element.name.lower() == Name.lower():
                #Skip element that exists in other page
                if self.CurrentPageVerified and Element.parent.name != self.CurrentPageVerifiedPageName: continue
                if self.CurrentPageVerified == True or Element.parent.Verify() == True:
                    return Element
        print "Element not found in ElementList"
        assert False
    # def FindElementOnCurrentPage(self, Name):
        # for Element in World.ElementList:
            # if Element.parent.name.lower() == World.CurrentPage.name.lower():
                # if Element.name.lower() == Name.lower():
                    # if Element.parent.Verify() == True:
                        # return Element
        # print ("Element not found in ElementList")
        # assert False
    def ConvertValue(self, value):
        if value.lower() == "<blank>":
            return ""
        return value
    def Login(self, loginfunctionname):
        if loginfunctionname == "WarRoomLogin" and not self.cdmlogin:
            self.FindPage("WarRoomLoginPage").Go()
            self.FindElement("username").SendKeys("managerdemo")
            self.FindElement("password").SendKeys("managerdemo!")
            self.FindElement("login").Click()
            self.cdmlogin = True
        elif loginfunctionname == "DsfLogin" and not self.dsflogin:
            self.FindPage("DsfLoginPage").Go()
            self.FindElement("username").SendKeys("fruit@gmail.com")
            self.FindElement("password").SendKeys("12345678")
            self.FindElement("login").Click()
            self.dsflogin = True
	else:
            print "Login Function {name} not found".format(name=loginfunctionname)
            pass
    def Find(self, ItemID, ItemListID):
        try:
            itemlist = self.MasterList[ItemListID]
        except KeyError:
            print "List", ItemListID,"Not Found"
            assert False
        try:
            item = itemlist[ItemID]
        except KeyError:
            print "Item", ItemID,"Not Found in list", ItemListID
            assert False
        return item

    CurrentUser = None

World = WorldContext.Instance()
