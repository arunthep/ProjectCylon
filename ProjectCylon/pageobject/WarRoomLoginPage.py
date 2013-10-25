# -*- coding: utf-8 -*- 
from framework.PageRefObFramework import *
class WarRoomLoginPageClass(Page):
	username = None
	password = None
	login = None
	def __init__(self):
		super( WarRoomLoginPageClass, self ).__init__( name="WarRoomLoginPage", title="Warroom", url="http://tools.thothmedia.com/warroom_new/", needlogin=False, loginfunction="", pageverifymethod="Title"  )
		self.username = Element (
				name="username",
				parent=self,
				locatingmethod="xpath",
				locator='/html/body/div/div[1]/div[2]/ul/li/form/input[1]',
				objecttype="text",
				checkattribute=['style="padding: 0px; height: 18px;"', 'class="input-small"'],
				)
		self.password = Element (
				name="password",
				parent=self,
				locatingmethod="xpath",
				locator='/html/body/div/div[1]/div[2]/ul/li/form/input[2]',
				)
		self.login = Element (
				name="login",
				parent=self,
				locatingmethod="xpath",
				locator='/html/body/div/div[1]/div[2]/ul/li/form/button',
				)
WarRoomLoginPage = WarRoomLoginPageClass()