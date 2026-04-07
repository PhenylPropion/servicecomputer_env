# -*- coding: utf-8 -*-

A. 展開されたファイル一覧が正しいかどうか確認する
   (FILETREE.txtファイルを参照)

B. index.py をWindows環境に応じて正しく設定する

(1) コマンドプロンプトで以下のwhereコマンドを実行する
    
    > where python
    C:¥Software¥Python¥Python-3.6.0¥python.exe
    C:¥Users¥YOURNAME¥...¥python.exe
    ...
    
    このような文字列が得られたら、先頭のコマンドパスを採用する
    ※ 何も得られなければ、Anaconda3環境等での解決策を参照のこと

(2) index.py の先頭行を(1)で得られたコマンドパスで書き換える
    (先頭の #! を忘れずに)
                                                             
    #!C:/Python3/python.exe
      ↓
    #!C:¥Software¥Python¥Python-3.6.0¥python.exe

(3) コマンドプロンプトで scフォルダに移動して index.py を実行してみる
    HTML風のテキストが表示されて、エラーがでなければOK
    ※ scフォルダに移動して実行しないと必ずエラーになるので注意
