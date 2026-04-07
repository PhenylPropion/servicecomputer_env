#!C:/usr/anaconda3/python.exe
# -*- coding: utf-8 -*-
########################################
import sys
import io

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer,encoding='utf-8')   

from importlib import import_module
import os
import hashlib
import time
from datetime import datetime

# cgi and cgitb will be deprecated from python 3.13,
# then we hold these libraries in our package with different names.
# by Satoru Fujita 2024/03/31
import cgi0
import cgitb0
cgitb0.enable()

from mysession import *

########################################

_LOG_FILE = "log/SC.log"

########################################

def timestr(dt=None):
    if dt is None: dt = datetime.now()
    return dt.strftime("%Y-%m-%d %H:%M:%S")

# エラーメッセージの出力
def logger(*args):
    print(*args, file=sys.stderr)
    with open(_LOG_FILE, "a") as fp:
        print(timestr(), *args, file=fp)

# GET/POSTのパラメータをdictにして返す
def getParam():
    # cgi to cgi0 by Satoru Fujita 2024/03/31
    param = cgi0.parse()
    for k,v in param.items():
        if len(v)==1: param[k] = v[0]
    return param

# cookieにsessionを付与するためのキーを生成する
def genSession(key=None,length=32):
    if key is None: key = str(time.time())
    return hashlib.sha256(key.encode()).hexdigest()[0:length]

# cookieヘッダーを解析してdictにして返す
def getCookie(cookie=None):
    ret = {}
    for kv in (cookie or os.environ.get("HTTP_COOKIE","")).split(";"):
        kv = kv.strip()
        if not kv: continue
        (k,v) = kv.split("=")
        if k=='Admin-Token': continue
        ret[k.strip()] = v.strip()
    return ret

# cookieにsessionがなければ付与、ANTI-CSRF設定があればCSRF検出を行う
def bakeCookie(cookie,param):
    if "anticsrf" in param:
        # anticsrfパラメータが付与されていたら、「簡易」CSRFチェックを行う
        # 本来session値から推測不可能な値を「秘密情報(=csrf値)」にするところだが、
        # ここでは「簡易」方式として、session値の逆順文字列を使っている
        if cookie.get("session","")[::-1] != param.get("secret",""):
            # CSRFならパラメータを空にする対策
            logger('CSRF Detected!')
            # dataパラメータは強制的に未設定にし、DETECTEDパラメータが設定される
            param.pop("data",None)
            param["DETECTED"] = "CSRF"
    if not cookie.get("session","") and param.get("anticsrf","")!="0":
        # cookieにsessionキーがなければ、自動的にキーを生成して付与する
        cookie["session"] = genSession()

# レスポンスにcookieを付与
def printHTTPHeader(cookie={},status=None):
    if cookie:
        cstr = "Set-Cookie:"+";".join([k+"="+v for k,v in cookie.items()])
        #logger('SET-COOKIE',cstr)
        print(cstr)
    print("Content-Type: text/html; charset=UTF-8")
    if status: print("Status: %s"%(status))
    print()
  
# 共通のHTMLヘッダー(<html>,<head>パート)を出力：title、styleを付加可能
def printHeader(title="",style=""):
    print("""
<!DOCTYPE html>
<html lang="ja">

<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta http-equiv="Content-Style-Type" content="text/css" />
<meta http-equiv="Content-Script-Type" content="text/javascript" />

<link rel="stylesheet" href="css/default.css" type="text/css" />
<style>
%(style)s
</style>

<title>%(title)s</title>
</head>
<body onload="typeof _init !== 'undefined' && _init()">
"""[1:-1]%{"title":title,"style":style})

# 共通のHTMLフッター(<script>パート)を出力：javascriptを付加可能
def printFooter(script=""):
    print("""

<!-- scripts -->
<script src="js/default.js"></script>
<script type="text/javascript">
%(script)s
</script>

</body>

</html>
"""[1:-1]%{"script":script})

# デバッグ甩
def printDebug(cookie={},title="DEBUG",param={}):
    printHTTPHeader(cookie=cookie)
    printHeader(title=title,style="")
    print(", ".join([k+"="+(v[0]) for k,v in param.items()]))
    printFooter()

# HTML出力
def printBody(html=""):
    """HTMLコンテンツを出力"""
    print('<img class="viewbutton" src="images/html32b.png" onclick="view_html()" title="ブラウザのコンソールにHTMLを表示します" />\n')
    print(html)
