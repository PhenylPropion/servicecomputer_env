#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import io

"""
# Comment out by Satoru Fujita 2024/03/31
#   These lines are multiply defined in mylib.py
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer,encoding='utf-8')   
"""

from importlib import import_module
from os import environ

# cgi and cgitb will be deprecated from python 3.13,
# then we hold these libraries in our package with different names.
# by Satoru Fujita 2024/03/31
import cgi0
import cgitb0
cgitb0.enable()

from mylib import *
from mysession import *

########################################

_action_list = {"hello","9x9","fact","input","cookie","session",
                "cart","db","csrf","loadlog","dellog"}

########################################

def importDynamic(modname):
    #logger('importDynamic',modname)
    try:
        # モジュール名(Pythonファイル名)は "m_ACTION名.py" に紐付けされる
        return import_module('m_'+modname)
    except Exception as e:
        logger(e)
        mesg = str(e)
    return None
    
# サブモジュール毎の処理を行い、CSS/HTML/JSを生成
def doAction(cookie={},param={}):
    action = param.get("action",None)
    #logger('doAction',action,cookie,param)
    if action == 'tab':
        name = param.get("name",None)
        if name:
            cookie["tab"] = name
            session = cookie.get("session",None)
            if session:
                sess = loadSession(session)
                sess["tab"] = name
                dumpSession(session, sess)
        return '', '', ''
        
    if action in _action_list:
        module = importDynamic(action)
        if module:
            return module.doit(title=action,cookie=cookie,param=param)
    return '', '"%s" not defined'%(action), ''
    
# CGIのメインモジュール
def printMain(title="無題"):
    param = getParam()
    cookie = getCookie()
    logger('COOKIE',cookie)
    bakeCookie(cookie,param)
    #logger('BAKED',cookie)

    # サブモジュール毎の処理を行い、CSS/HTML/JSを生成
    style,html,script = doAction(cookie=cookie,param=param)

    # パラメータajax=1が指定されていたら、HTML化せずにhtmlをデータとして直接返す
    if param.get("ajax",False):
        printHTTPHeader(cookie=cookie)
        print(html)
        return
    
    # HTML化(style+html+script)した結果を返す
    printHTTPHeader(cookie=cookie)
    printHeader(title=param.get("action",title),style=style)
    printBody(html=html)
    printFooter(script=script)

# Mainプログラムの実行
printMain()
