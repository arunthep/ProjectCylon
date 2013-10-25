# -*- coding: utf-8 -*- 
from framework.PageRefObFramework import *
class WeLoveSigninPageClass(Page):
	username = None
	password = None
	checkbox = None
	def __init__(self):
		super( WeLoveSigninPageClass, self ).__init__( name="WeLoveSigninPage", title="เข้าสู่ระบบ : Weloveshopping.com", url="http://www.weloveshopping.com/member/signin/", needlogin=False, loginfunction="", pageverifymethod="URL"  )
		self.username = Element (
				name="username",
				parent=self,
				locatingmethod="xpath",
				locator='//*[@id="username"]',
				objecttype="text",
				checkattribute=['class="jq_watermark field"'],
				)
		self.password = Element (
				name="password",
				parent=self,
				locatingmethod="xpath",
				locator='//*[@id="password"]',
				objecttype="password",
				checkattribute=['class="jq_watermark field"'],
				)
		self.checkbox = Element (
				name="rememberpasswd",
				parent=self,
				locatingmethod="xpath",
				locator='//*[@id="form"]/form/input',
				objecttype="checkbox",
				checkattribute=['class="checkbox float-left"'],
				)
WeLoveSigninPage = WeLoveSigninPageClass()