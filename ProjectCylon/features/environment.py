# -*- coding: utf-8 -*- #
from framework.WorldContext import *
World = WorldContext.Instance()

def before_all(context):
	import	framework.ContextObjects.User
	import	framework.ContextObjects.LoadUser


def before_tag(context, tag):
	
	if tag=='new_browser':
		World.driver.quit()
		World.driver = webdriver.Firefox()
		World.driver.implicitly_wait(3)    
#def after_all(context):
#	World.driver.quit()

