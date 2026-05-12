# -*- coding: utf-8 -*-

from mylib import *

def doit(title="",cookie={},param={}):
    """HTMLコンテンツ出力部を記述"""

    html = """<h4>Happy! World!</h4>"""
    
    vscode_monaco = """
    <div style="margin-top: 15px;">
        <div id="vscode-container" style="width: 100%; height: 500px; border: 1px solid #2d2d2d; box-shadow: 0 4px 10px rgba(0,0,0,0.2);"></div>
    </div>
    
    <!-- VS Codeのコアエンジン「Monaco Editor」をCDNから読み込みます -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.44.0/min/vs/loader.min.js"></script>
    <script>
        require.config({ paths: { 'vs': 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.44.0/min/vs' } });
        require(['vs/editor/editor.main'], function() {
            monaco.editor.create(document.getElementById('vscode-container'), {
                value: 'def hello_world():\\n    print("Happy! World!")\\n\\nhello_world()',
                language: 'python',
                theme: 'vs-dark',
                automaticLayout: true,
                minimap: { enabled: false }
            });
        });
    </script>
    """
    
    return '', html + vscode_monaco, ''

########################################################################

if __name__ == '__main__':
    import sys
    argv = sys.argv
    argc = len(argv)
    print(doit()[1])
