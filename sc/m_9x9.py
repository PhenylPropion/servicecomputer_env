# -*- coding: utf-8 -*-

from mylib import *

_help = """<pre class="exercise">
演習問題：
m_9x9.py の doit()関数をdoit1()ないしdoit2()のどちらかに切り替えて
http://localhost/sc/index.html をリロードしてみましょう。
<pre>
"""

def doit1(title="",cookie={},param={}):
    """CSS,HTML,SCRIPTをタプルにして返す"""
    
    html = """
<table style="table-layout:fixed;width:240px;text-align:right;">
<tr><td></td><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th></tr>
<tr><th>1</th><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr>
<tr><th>2</th><td>2</td><td>4</td><td>6</td><td>8</td><td>10</td><td>12</td><td>14</td><td>16</td><td>18</td></tr>
<tr><th>3</th><td>3</td><td>6</td><td>9</td><td>12</td><td>15</td><td>18</td><td>21</td><td>24</td><td>27</td></tr>
<tr><th>4</th><td>4</td><td>8</td><td>12</td><td>16</td><td>20</td><td>24</td><td>28</td><td>32</td><td>36</td></tr>
<tr><th>5</th><td>5</td><td>10</td><td>15</td><td>20</td><td>25</td><td>30</td><td>35</td><td>40</td><td>45</td></tr>
<tr><th>6</th><td>6</td><td>12</td><td>18</td><td>24</td><td>30</td><td>36</td><td>42</td><td>48</td><td>54</td></tr>
<tr><th>7</th><td>7</td><td>14</td><td>21</td><td>28</td><td>35</td><td>42</td><td>49</td><td>56</td><td>63</td></tr>
<tr><th>8</th><td>8</td><td>16</td><td>24</td><td>32</td><td>40</td><td>48</td><td>56</td><td>64</td><td>72</td></tr>
<tr><th>9</th><td>9</td><td>18</td><td>27</td><td>36</td><td>45</td><td>54</td><td>63</td><td>72</td><td>81</td></tr>
</table>
"""[1:-1]

    return "", html + _help, ""

# 9x9ではなく10x10の表を生成するように変えた
def doit2(title="",cookie={},param={}):
    """CSS,HTML,SCRIPTをタプルにして返す"""

    # ヘッダー行を生成する(",1,2,3,4,5,6,7,8,9")    
    header = ["<td></td>"]
    for i in range(1,11):
        header.append("<th>%d</th>"%(i))
    header = "<tr>" + "".join(header) + "</tr>"

    matrix = []
    for i in range(1,11):
        row = ["<th>%d</th>"%(i)]
        # 第n行を計算する(ex. "3,3,6,9,12,15,18,21,24,27")    
        for j in range(1,11):
            row.append("<td>%d</td>"%(i*j))
        # 第n行を生成する
        matrix.append("<tr>" + "".join(row) + "</tr>")

    # table要素を生成する
    table = ['<table style="table-layout:fixed;width:240px;text-align:right;">',
             header,
             *matrix,
             '</table>']
    html = "\n".join(table)

    return "", html + _help, ""

########################################################################
# ２つの表示方法を切り替えてみる
# doit = doit1 あるいは doit = doit2 としてみる
doit = doit2

########################################################################

if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)
    print(doit()[1])
