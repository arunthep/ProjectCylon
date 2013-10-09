# -*- coding: utf-8 -*- #
from framework.WorldContext import *
World = WorldContext.Instance()

def before_all(context):
	import	framework.ContextObjects.User
	import	framework.ContextObjects.LoadUser
	
#def after_all(context):
#	World.driver.quit()

