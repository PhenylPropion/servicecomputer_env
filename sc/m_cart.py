# -*- coding: utf-8 -*-

from mylib import *
from mysession import *

mikan_u = 80
apple_u = 100

server_logs = """<hr />
<div title="サーバー側で受信したフォームパラメータ">Parameters: <span id="param">%(plist)s</span></div>
<div title="サーバー側で設定したクッキー or 受信したクッキー">Cookies: <span id="cookie">%(clist)s</span></div>
<input type="button" value="reset cookie" onclick="document.cookie='session=';document.getElementById('cookie').innerHTML='';" />
"""

complete_html = """<h4>%(title)s</h4>
<div>%(total)d円のお買上、ありがとうございました</div>
<a href="index.py?action=cart">新規カートへ</a>
""" + server_logs

input_tag = """
<input class="right" type="text" name="%(name)s" value="%(quantity)d"
 onchange="check_digit(this);" />
"""[1:]

cart_html = """<h4>%(title)s</h4>
<form method="GET" action="index.py">
<table border="1">
<tr><th>商品名</th><th>単価</th><th>個数</th><th>小計</th></tr>
<tr>
<td>みかん</td>
<td class="right">%(mikan_u)d</td>
<td class="right">%(mikan_tag)s</td>
<td class="right">%(mikan_p)d</td>
</tr>
<tr>
<td>りんご</td>
<td class="right">%(apple_u)d</td>
<td class="right">%(apple_tag)s</td>
<td class="right">%(apple_p)d</td>
</tr>
<tr>
<td colspan="3">計</td>
<td class="right">%(total_p)d</td>
</tr>
</table>
<input type="hidden" name="action" value="cart">
<input type="submit" name="submit" value="カートへ"> ⇔
<input type="submit" name="confirm" value="確認"> →
<input type="submit" name="complete" value="確定">
""" + server_logs

def doit(title="",cookie={},param={},debug=False):
    session = "DUMMYSESSION" if debug else cookie["session"]
    cart = loadSession(session)

    # cookieとparamのダンプ
    clist = ", ".join([k+"="+str(v) for k,v in cookie.items()])
    plist = ", ".join([k+"="+str(v) for k,v in param.items()])

    if "submit" in param or "complete" in param or "confirm" in param:
        logger('CART',param)
    
    if param.get("complete",None):
        # 購入完了画面の表示
        title = "購入完了画面"
        mikan_q, apple_q = cart.get("mikan_q",0), cart.get("apple_q",0)
        total =  mikan_u * mikan_q + apple_u * apple_q
        # 購入完了したので、セッションデータは空にする
        dumpSession(session,{})
        html = complete_html%{"title":title,"clist":clist,"plist":plist,
                              "total":total}
        return "", html, ""

    elif param.get("confirm",None):
        # 確認画面の表示
        title = "確認画面"
        cart["confirm"] = True
        dumpSession(session,cart)
        mikan_q, apple_q = cart.get("mikan_q",0), cart.get("apple_q",0)
        mikan_tag, apple_tag = str(mikan_q), str(apple_q)

    else:
        # カート画面の表示
        title = "商品選択画面"
        if param.get("submit",None) and not cart.get("confirm",None):
            # パラメータから個数を取得してセッションとして保存
            mikan_q = int(param.get("mikan_q",0))
            apple_q = int(param.get("apple_q",0))
            cart = {"mikan_q":mikan_q, "apple_q":apple_q}
            dumpSession(session,cart)
        else:
            # 保存されたセッションから復元
            mikan_q, apple_q = cart.get("mikan_q",0), cart.get("apple_q",0)
            # セッションの確認状態を削除して再度保存
            cart["confirm"] = False
            dumpSession(session,cart)
        # inputタグの生成
        mikan_tag = input_tag%{"name":"mikan_q","quantity":mikan_q}
        apple_tag = input_tag%{"name":"apple_q","quantity":apple_q}
    
    # カート画面、確認画面で共通の処理
    #（商品・単価・個数・価格のテーブルを表示）
    mikan_p = mikan_u * mikan_q
    apple_p = apple_u * apple_q
    total_p = mikan_p + apple_p

    html = cart_html%{"title":title,"clist":clist,"plist":plist,
                      "total_p":total_p,
                      "mikan_u":mikan_u,"mikan_tag":mikan_tag,"mikan_p":mikan_p,
                      "apple_u":apple_u,"apple_tag":apple_tag,"apple_p":apple_p}
    return "", html, ""

########################################################################

if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)
    print("#### 画面表示")
    print(doit(param={},debug=True)[1])
    print("#### 購買中")
    print(doit(param={"submit":True,"mikan_q":2,"apple_q":3},debug=True)[1])
    print("#### 購買確認")
    print(doit(param={"confirm":True},debug=True)[1])
    print("#### 購買完了")
    print(doit(param={"complete":True},debug=True)[1])
