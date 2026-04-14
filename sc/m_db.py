#!C:/Python3/python.exe
# -*- coding: utf-8 -*-

from html import escape
import pymysql
from mylib import *

def connectDB():
    try:
        conn = pymysql.connect(host="db",
                               db="student",
                               user="sample",
                               passwd="12345",
                               charset="utf8",
                               autocommit=True,
                               cursorclass=pymysql.cursors.DictCursor)
        return conn, True
    except Exception as e:
        return str(e), False

def doit(title="",cookie={},param={}):
    """HTMLコンテンツ出力部を記述""" 
    if "submit" in param: logger('DB',param)

    # データベース接続を確立する
    conn, ok = connectDB()
    if not ok:
        html = """<pre>
データベースとの接続に失敗しました。
XAMPP Control PanelでMySQLが起動しているかをまず確認してください。
起動している場合は、以下のエラーを確認してください。

%s
</pre>
"""%(escape(conn))
        return "", html, ""

    # 入力フィールドチェック(省略時ON)、SQLインジェクション対策(省略時ON)
    studentID = param.get("studentID","")
    check = param.get("check","")
    checkjs = 'onchange="check_studentID(this,\'submit\');"' if check else ''
    inject = param.get("inject","")
    setinj = '<input type="hidden" name="inject" value="1" />' if inject else ''
    placeholder = "' OR '1" if inject else ''
    
    html = ["""<form method="GET" action="index.py">
<input type="hidden" name="action" value="db" />
<input type="hidden" name="check" value="%(check)s" />
%(setinj)s
学籍番号: <input type="text" name="studentID" value="%(studentID)s"
         placeholder="%(placeholder)s" %(checkjs)s />
<input id="submit" type="submit" name="submit" value="送信" />
</form>

<table border="1">
<tr><th>id</th><th>学籍番号</th><th>名前</th></tr>
"""%{"studentID":studentID,"check":check,"checkjs":checkjs,
     "placeholder":placeholder,"setinj":setinj}]

    if not param.get("submit",""):
        # 一覧表示の場合
        sql = "SELECT * FROM students ORDER BY studentID"
        val = ()
    elif inject:
        # 検索の場合（SQLインジェクション無防備）
        sql = "SELECT * FROM students WHERE studentID='%s' ORDER BY studentID"%(studentID)
        logger(sql)
        val = ()
    else:
        # 検索の場合（SQLインジェクション対策）
        sql = "SELECT * FROM students WHERE studentID=%s ORDER BY studentID"
        val = (studentID,)
        
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, val)
            row = cursor.fetchall()
            if len(row)==0:
                html.append('<tr><td colspan="3">該当者は存在しません</td>')
            else:
                for r in row:
                    # r: {id:10, studentID:"99K9999", name:"名前"}
                    rs = "<tr><td>%(id)s</td><td>%(studentID)s</td><td>%(name)s</td></tr>"%(r)
                    html.append(rs)
    finally:
        conn.close()

    html.append('</table><a href="index.py?action=db&check=%s&inject=%s">一覧画面</a>'%(check,inject))

    return "", "\n".join(html), ""

########################################################################

if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)
    print(doit()[1])
