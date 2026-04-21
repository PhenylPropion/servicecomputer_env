# -*- coding: utf-8 -*-

from mylib import *

# nの階乗を返す関数
def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 階乗一覧表示の関数
def doit(title="",cookie={},param={}):
    """CSS,HTML,SCRIPTをタプルにして返す"""

    n = int(param.get("n", 100))

    items = []
    for i in range(1, n + 1): # 1からnまでの階乗を計算してリストに追加
        items.append(f"<li>{i}の階乗は、{fact(i)}</li>") # HTMLのリストとして
    html = "<ul>\n" + "\n".join(items) + "\n</ul>" # 最終的なHTMLを生成

    return "", html, ""


if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)
    print(doit()[1])
