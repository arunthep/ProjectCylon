# -*- coding: utf-8 -*-
from framework.WorldContext import *
World = WorldContext.Instance()

from behave import *
import pageobject.AllPages

@given ("User opens Windows program [{ExecutableName}]")
@given ("User opens window [{ExecutableName}]")
@given ("User runs program [{ExecutableName}]")
@given ("User runs program [{ExecutableName}] with argument [{Parameter}]")
@given ("User runs program [{ExecutableName}] with parameter [{Parameter}]")
def step(context, ExecutableName, Parameter=None):
    if Parameter != None and Parameter != '':
        World.autoit.Run( ExecutableName + ' ' +  Parameter)
    else:
        World.autoit.Run( ExecutableName )


@when ("User enters '{Input}' into [{ControlName}] on window [{WindowTitle}]")
@when ("User types '{Input}' into [{ControlName}] on window [{WindowTitle}]")
def step(context, Input, ControlName, WindowTitle):
    World.autoit.WinWait( WindowTitle, "", 10 )
    if World.autoit.WinExists( WindowTitle ) == False:
        assert False
    World.autoit.WinActivate( WindowTitle )
    World.autoit.WinWaitActive( WindowTitle )

    try:
        control_class_selector = World.Find( ControlName, WindowTitle+"ControlList" )
    except:
        assert False
    World.autoit.ControlSend( WindowTitle, "", control_class_selector, World.ConvertSpecialKey(Input) )
    return True

@then ("[{ControlName}] on window [{WindowTitle}] should display '{ExpectedResult}'")
@then ("[{ControlName}] on window [{WindowTitle}] should show '{ExpectedResult}'")
def step(context, ControlName, WindowTitle, ExpectedResult):
    World.autoit.WinWait( WindowTitle, "", 10 )
    if World.autoit.WinExists( WindowTitle ) == False:
        assert False

    World.autoit.WinActivate( WindowTitle )
    World.autoit.WinWaitActive( WindowTitle )

    try:
        control_class_selector = World.Find( ControlName, WindowTitle+"ControlList" )
    except:
        assert False
    output = World.autoit.ControlGetText ( WindowTitle, "", control_class_selector )
    print output
    print ExpectedResult
    if (output.lower().find(ExpectedResult.lower()) == -1):
        assert False

    return True

@Then ("[{WindowTitle}] window is shown")
@Then ("[{WindowTitle}] dialog is shown")
def step(context, WindowTitle):
    World.autoit.WinWait( WindowTitle, "", 10)
    if World.autoit.WinExists( WindowTitle ):
        return True
    else:
        assert False

@when (u"User clicks [{ControlName}] on window [{WindowTitle}]")
def step(context, ControlName, WindowTitle):
    World.autoit.WinWait( WindowTitle, "", 10 )
    if World.autoit.WinExists( WindowTitle ) == False:
        assert False

    World.autoit.WinActivate( WindowTitle )
    World.autoit.WinWaitActive( WindowTitle )

    try:
        control_class_selector = World.Find( ControlName, WindowTitle+"ControlList" )
    except:
        assert False
    World.autoit.ControlClick( WindowTitle, "", control_class_selector )
    return True

@when ("[Optional] User clicks [{ControlName}] on window [{WindowTitle}]")
def step(context, ControlName, WindowTitle):
    World.autoit.WinWait( WindowTitle, "", 10)
    if World.autoit.WinExists ( WindowTitle ):
        context.execute_steps(u'''
        When User clicks [{ControlName}] on window [{WindowTitle}]
        '''.format(ControlName=ControlName,WindowTitle=WindowTitle))
    else:
        return True

@when( "User sends '{Input}' to window [{WindowTitle}]" )
@when( "User types '{Input}' to window [{WindowTitle}]" )
def step(context, Input, WindowTitle):
    World.autoit.WinWait( WindowTitle, "", 10 )
    if World.autoit.WinExists( WindowTitle ) == False:
        assert False
    World.autoit.WinActivate( WindowTitle )
    World.autoit.WinWaitActive( WindowTitle )

    World.autoit.Send( World.ConvertSpecialKey(Input) )
    return True

@then( "[{WindowTitle}] window is closed" )
def step(context, WindowTitle):
    World.autoit.WinWait( WindowTitle, "", 5)
    if World.autoit.WinExists( WindowTitle ) == True:
        assert False
    else:
        return True
