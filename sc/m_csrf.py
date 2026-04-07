# -*- coding: utf-8 -*-

from html import escape
from mylib import *

def doit(title="",cookie={},param={}):
    """HTMLコンテンツ出力部を記述"""

    anticsrf = param.get("anticsrf","")
    if anticsrf: anticsrf = '&anticsrf='+anticsrf
    
    html = """
<div class="pagelike rose">
攻撃者が攻撃対象者(＝一般利用者)に送ったページに利用者がアクセスしてしまい、危険なリンク <a href="index.py?action=cookie%s&data=100">index.py?data=100</a> が実行され得る状態（これはデモなので、このリンクはクリックされず、晒されている状態にしてある）。
<ul>
<li>このページはあくまで利用者のブラウザで開いているので、攻撃者は状況を観測できないが...</li>
<li>利用者がこのリンクをクリック → サーバーにデータ(data=100)送信。サーバー側ではこれが攻撃なのか利用者の通常操作なのかの区別がつかない！？ 攻撃者は、利用者が意図しない操作を実行することができる！</li>
<li><strong>CSRFの対策が施されていれば、それらの区別ができる！</strong></li>
</ul>
</div>
"""[1:-1]%(anticsrf)
    
    return "", html, ""

########################################################################

if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)
    print(doit()[1])
