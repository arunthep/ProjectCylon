# -*- coding: utf-8 -*- 
from framework.PageRefObFramework import *
class WeLoveHomePageClass(Page):
	login = None
	def __init__(self):
		super( WeLoveHomePageClass, self ).__init__( name="WeLoveHomePage", title="ร้านค้าออนไลน์ ขายของออนไลน์ เว็บขายของ ช้อปปิ้ง | Weloveshopping", url="http://www.weloveshopping.com/", needlogin=False, loginfunction="", pageverifymethod="URL"  )
		self.login = Element (
				name="login",
				parent=self,
				locatingmethod="xpath",
				locator='//*[@id="wrapper_login"]/div[1]/div[3]/div[1]/div[2]/a',
				checkattribute=['href="http://www.weloveshopping.com/member/signin/"'],
				)
WeLoveHomePage = WeLoveHomePageClass()