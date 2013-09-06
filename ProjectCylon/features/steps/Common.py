# -*- coding: utf-8 -*- 
from framework.WorldContext import *
World = WorldContext.Instance()

from behave import *
import pageobject.AllPages

#def When( )

@given("User has [{PageName}] open")
def step(context, PageName):
	Page = World.FindPage( PageName )
	if Page is not None :
		if Page.Go()  == False:
			assert False
	
#This does all When, And	
@when ("User enters '{Value}' to [{Name}]")	
def step(context, Name, Value):
	Element = World.FindElement(Name)
	if Element is not None :
		if Element.SendKeys(Value) == False:
			assert False
	
@when ('User clicks [{Button}] button')
def step(context, Button):
	Element = World.FindElement(Button)
	if Element is not None :
		return Element.Click()

@Then ("The system displays [{PageName}]")
def step(context, PageName):
	Page = World.FindPage( PageName )
	if Page is not None :
		if Page.Verify() == False:
			assert False
	
@Then ("The [{Name}] shows '{Value}'")
def step(context, Name, Value):
	Element = World.FindElement(Name)
	if Element is not None :
		if Element.VerifyText(Value) == False:
			assert False
	