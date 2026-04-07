# -*- coding: utf-8 -*-

import re
from html import escape
from mylib import *

########################################################################

_re_email = r'^[\w\.\-]+@[\w\-]+(\.[\w\-]+)*$'

########################################################################

def doit(title="",cookie={},param={}):
    """HTMLコンテンツ出力部を記述"""
    check = param.get("check","")
    xss = param.get("xss","")

    #if "submit" in param: logger('INPUT',param)

    if "userName" in param or "eMail" in param:
        # フォームのパラメータが渡されたら、送信された場合なので、送信データを表示する
        user = param.get("userName","")
        email = param.get("eMail","")
        if check=="s":
            if not re.match(_re_email, email):
                email += "はメールアドレスではありません"

        if xss:
            user, email = escape(user), escape(email)

        html = """
<form method="GET" action="index.py">
<input type="hidden" name="action" value="input" />
<input type="hidden" name="check" value="%s" />
<input type="hidden" name="xss" value="%s" />
お名前: %s<br/>
メールアドレス: %s<br/>
<input type="submit" name="submit" value="戻る">
</form>
"""[1:-1]%(check,xss,user,email)

    else:
        # フォームのパラメータがなにもない場合は、初期フォームを表示する
        onchange = ''
        if check=="c":
            onchange = 'onchange="return check_email(this,\'submit\');"'

        html = """
<form method="GET" action="index.py">
<input type="hidden" name="action" value="input" />
<input type="hidden" name="check" value="%s" />
<input type="hidden" name="xss" value="%s" />
お名前: <input type="text" name="userName" value="" /><br/>
メールアドレス: <input type="text" name="eMail" value="" %s /><br/>
<input id="submit" type="submit" name="submit" value="送信" />
</form>
"""[1:-1]%(check,xss,onchange)
    
    return '', html, ''

########################################################################

if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)
    print(doit()[1])
