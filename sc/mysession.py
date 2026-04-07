#!C:/usr/anaconda3/python.exe
# -*- coding: utf-8 -*-

import sys
import os
import json

########################################

_session_dir = "session"

def _makeSessionDir():
    if not os.path.exists(_session_dir): os.mkdir(_session_dir)

def dumpSession(session,data):
    if not session: return
    _makeSessionDir()
    file = os.path.join(_session_dir,session)
    with open(file,"w",encoding="utf-8") as fp:
        json.dump(data,fp,ensure_ascii=False)

def loadSession(session):
    if not session: return {}
    _makeSessionDir()
    file = os.path.join(_session_dir,session)
    try:
        with open(file,"r",encoding="utf-8") as fp:
            return json.load(fp) or {}
    except Exception:
        return {}

########################################

if __name__ == '__main__':
    argv = sys.argv
    argc = len(sys.argv)
    print(loadSession('f8c1857924d9e5c5fb1039a158f497d1'))
    dumpSession('TEST',{"userName":"テスト","eMail":"test@bar.com"})
    print(loadSession('TEST'))
