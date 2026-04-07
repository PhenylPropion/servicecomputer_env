# -*- coding: utf-8 -*-

from mylib import *

def doit(title="",cookie={},param={}):
    """HTMLコンテンツ出力部を記述"""

    return '', title.upper(), ''

########################################################################

if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)
    print(doit()[1])
