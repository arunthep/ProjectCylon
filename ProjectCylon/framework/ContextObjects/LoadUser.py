# -*- coding: utf-8 -*-
from framework.WorldContext import *
World = WorldContext.Instance()

from User import *

DefaultUser = User()
ManagerDemoUser = User("managerdemo", "managerdemo!")
AgentDemoUser = User("agentdemo1", "agentdemo1!")

World.MasterList["User"] = {}
World.MasterList["User"]["DefaultUser"] = DefaultUser
World.MasterList["User"]["ManagerDemoUser"] = ManagerDemoUser
World.MasterList["User"]["AgentDemoUser"] = AgentDemoUser
