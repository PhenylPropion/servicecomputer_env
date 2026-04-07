# -*- coding: utf-8 -*-

from html import escape
from mylib import *

def doit(title="",cookie={},param={}):
    """HTMLコンテンツ出力部を記述"""
    if "submit" in param: logger('COOKIE/SESSION',param)
    param.pop("submit","")

    anti, secret, remark = "", "", ""
    if "anticsrf" in param:
        anticsrf = param["anticsrf"]
        anti = '<input type="hidden" name="anticsrf" value="%s" />'%(anticsrf)
        
        if anticsrf=='1':
            key = cookie.get("session","")[::-1]
            secret = '<input type="hidden" name="secret" value="%s" />'%(key)
            param["secret"] = key

    data = escape(param.get("data",""))
    if param.get("DETECTED",""):
        remark = '<div class="red">CSRFを検出してdataを強制削除</div>'

    clist = ", ".join([k+"="+str(v) for k,v in cookie.items()])
    param.pop("anticsrf",None)
    plist = ", ".join([k+"="+str(v) for k,v in param.items()])

    html = """
<form method="GET" action="index.py">
データ(任意):<input type="text" name="data" value="%(data)s" />
<input type="hidden" name="action" value="cookie" />
%(anti)s
%(secret)s
<input id="send" type="submit" name="submit" value="送信" />
<hr />
%(remark)s
<div title="サーバー側で受信したフォームパラメータ">Parameters: <span id="param">%(plist)s</span></div>
<div title="サーバー側で設定したクッキー or 受信したクッキー">Cookies: <span id="cookie">%(clist)s</span></div>
<input type="button" value="reset cookie" onclick="document.cookie='session=';document.getElementById('cookie').innerHTML='';" />
</form>
"""[1:-1]%{"data":data,"anti":anti,"secret":secret,
           "plist":plist,"clist":clist,"remark":remark}

    return "", html, ""

########################################################################

if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)
    print(doit()[1])
