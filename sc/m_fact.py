# -*- coding: utf-8 -*-

from html import escape
from mylib import *

# nの階乗を返す関数
def fact(n):
    # このコードは階乗計算ではない！
    return n

# 階乗一覧表示の関数
def doit(title="",cookie={},param={}):
    """CSS,HTML,SCRIPTをタプルにして返す"""

    help = """演習問題：
m_fact.py を書き直して、値 n に対して１〜nの階乗を表示するようにしてください。
fact()を正しく定義し、doit()は CSS、HTML、Javascript の３値を返すようにします。
HTMLは下記のような <ul>...</ul> を出力するようにします。
（下記のHTMLをそのまま出力するのでは、汎用性がないのでNGです）

<ul>
  <li>1の階乗は、1です</li>
  <li>2の階乗は、2です</li>
  <li>3の階乗は、6です</li>
  <li>4の階乗は、24です</li>
  <li>5の階乗は、120です</li>
  <li>6の階乗は、720です</li>
  <li>7の階乗は、5040です</li>
  <li>8の階乗は、40320です</li>
  <li>9の階乗は、362880です</li>
  <li>10の階乗は、3628800です</li>
</ul>
"""
    # 下記、書き直したら、このreturn文はコメントアウトしてください
    return "", '<pre class="exercise">'+escape(help)+"</pre>", ""
    
    # 以下、書き直す部分
    n = int(param.get("n",10))

    # 1〜nの階乗を表示するように、HTML文字列を生成するコード
    html = "..."
    for i in range(1,n+1):
        # ...
        pass

    # doit()は CSS、HTML、Javascript の３値を返す
    return "", html, ""

########################################################################

if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)
    print(doit()[1])
