# -*- coding: utf-8 -*- 
from framework.PageRefObFramework import *
class WarRoomApplicationPageClass(Page):
	menu = None
	logout = None
	currentuser = None
	search = None
	monitor = None
	pending = None
	def __init__(self):
		super( WarRoomApplicationPageClass, self ).__init__( name="WarRoomApplicationPage", title="Warroom", url="http://tools.thothmedia.com/warroom_new/", needlogin=True, loginfunction="WarRoomLogin", pageverifymethod="Title"  )
		self.menu = Element (
				name="menu",
				parent=self,
				locatingmethod="xpath",
				locator='//*[@id="menu-manager"]/div/div/a',
				)
		self.logout = Element (
				name="logout",
				parent=self,
				locatingmethod="xpath",
				locator='/html/body/div[1]/div[1]/div[2]/div/a',
				)
		self.currentuser = Element (
				name="currentuser",
				parent=self,
				locatingmethod="xpath",
				locator='//*[@id="username-str"]',
				)
		self.search = Element (
				name="search",
				parent=self,
				locatingmethod="xpath",
				locator='//*[@id="btnSearch"]',
				)
		self.monitor = Element (
				name="monitor",
				parent=self,
				locatingmethod="xpath",
				locator='//*[@id="menu-monitor"]/a',
				)
		self.pending = Element (
				name="pending",
				parent=self,
				locatingmethod="xpath",
				locator='//*[@id="menu-monitor"]/div/div[2]/a',
				)
WarRoomApplicationPage = WarRoomApplicationPageClass()