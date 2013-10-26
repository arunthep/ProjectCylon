# -*- coding: utf-8 -*-
from framework.WorldContext import *
World = WorldContext.Instance()

from behave import *

import pageobject.AllPages

@given(u"No user currently logged in")
def step( context ):
	if World.FindElement( "login" ).Verify():
		return True
	else:
		if World.FindElement( "logout" ).Click() == False:
			assert False

@when (u"User logs in with username '{UserName}' and password '{Password}'")
def step( context, UserName, Password ):
	context.execute_steps(u'''
        When User enters '{UserName}' to [username]
		And User enters '{Password}' to [password]
		And User clicks [Login] button
		'''.format(UserName=UserName,Password=Password))

@given (u"The Current User is '{User}'")
def step( context, User ):
	user = World.Find( User, "User" )
	if user is not None:
		World.CurrentUser = user
		return True
	else:
		print "Error! User Not Found"
		assert False

@when (u"User logs in with Current User profile")
def step( context ):
	context.execute_steps(u'''
        When User logs in with username '{UserName}' and password '{Password}'
		'''.format(UserName=World.CurrentUser.UserName,Password=World.CurrentUser.Password))

@then(u'The system do something else')
def step_impl(context):
	assert False

@then(u"The Current User ID is correct")
def step( context ):
	context.execute_steps(u'''
		Then The [currentuser] shows '{UserName}'
		'''.format(UserName=World.CurrentUser.UserName))



