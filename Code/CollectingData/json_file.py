# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 22:11:12 2021

@author: bberry
"""
import requests
import json

r = requests.get("https://reqres.in/api/users?page=2")

res = r.json()

print(json.dumps(res, indent=4)
      
#q = res['contents']['quotes'][0]


