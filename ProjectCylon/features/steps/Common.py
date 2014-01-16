# -*- coding: utf-8 -*-
from framework.WorldContext import *
from behave import *
import pageobject.AllPages

# def When( )

@given("User has [{PageName}] open")
def step(context, PageName):
    Page = World.FindPage(PageName)
    if Page is not None :
        if Page.Go() == False:
            assert False

# This does all When, And
@when ("User enters '{Value}' to [{Name}]")
def step(context, Name, Value):
    Element = World.FindElement(Name)
    if Element is not None :
        if Element.SendKeys(Value) == False:
            assert False

@when ("User enters date '{Value}' to [{Name}]")
def step(context, Name, Value):
    Element = World.FindElement(Name)
    if Element is not None :
        if Element.SendKeysByScript(Value) == False:
            assert False

@when ("User clears input [{Name}]")
def step(context, Name):
    Element = World.FindElement(Name)
    if Element is not None :
        if Element.SendKeysByScript('') == False:
            assert False
            
@when ('User clicks [{Button}] button')
def step(context, Button):
    Element = World.FindElement(Button)
    if Element is not None :
        return Element.Click()

@when ('User clicks [{Link}] link')
def step(context, Link):
    Element = World.FindElement(Link)
    if Element is not None :
        return Element.Click()

# Example: When User uploads file 'd:\\file.txt' to [upload]
@when ("User uploads file '{filePath}' to [{fileUploadElement}]")
def step(context, filePath, fileUploadElement):
    Element = World.FindElement(fileUploadElement)
    if Element is not None :
        if Element.SendKeys(filePath) == False :
            assert False

@Then ("The system displays [{PageName}]")
def step(context, PageName):
    Page = World.FindPage(PageName)
    if Page is not None :
        if Page.Verify() == False:
            assert False

@Then ("The [{Name}] shows '{Value}'")
def step(context, Name, Value):
    Element = World.FindElement(Name)
    if Element is not None :
        if Element.VerifyText(Value) == False:
            assert False

@Then ("The [{Name}] is blank")
def step(context, Name):
    Element = World.FindElement(Name)
    if Element is not None :
        if Element.HasValue() == True :
            assert False

@Then ("The [{Name}] has a value")
def step(context, Name):
    Element = World.FindElement(Name)
    if Element is not None :
        if Element.HasValue() != True :
            assert False

@Then ("The [{Name}] exists")
def step(context, Name):
    Element = World.FindElement(Name)
    if Element is None :
        assert False

@Then ("The [{Name}] does not exist")
def step(context, Name):
    Element = World.FindElement(Name)
    if Element.check_exists() == True :
        assert False

