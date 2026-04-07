# -*- coding: utf-8 -*-

from mylib import *

# doit()は、CSS、HTML、Javascript の３値を返すように定義する
def doit(title="",cookie={},param={}):
    """HTMLコンテンツ出力部を記述"""

    with open("log/SC.log", "w") as fp:
        fp.write("")

    return '', '', ''

########################################################################

if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)
    print(doit()[1])
