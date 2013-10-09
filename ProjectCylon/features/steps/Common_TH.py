# -*- coding: utf-8 -*- 
from framework.WorldContext import *
World = WorldContext.Instance()

from behave import *
import pageobject.AllPages

#def When( )

@given(u"User เปิด page [{PageName}]")
def step(context, PageName):
	Page = World.FindPage( PageName )
	if Page is not None :
		if Page.Go()  == False:
			assert False

@given(u"User ยังไม่ได้ logged in")
def step( context ):
	if World.FindElement( "login" ).Verify():
		return True
	else:
		if World.FindElement( "logout" ).Click() == False:
			assert False	

