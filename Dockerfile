FROM httpd:2.4

# Python3のインストール
RUN apt-get update && apt-get install -y python3 && apt-get clean

# CGIモジュールのコメントアウトを外して有効化（より確実な置換処理）
RUN sed -i 's/#LoadModule cgi_module modules\/mod_cgi.so/LoadModule cgi_module modules\/mod_cgi.so/' /usr/local/apache2/conf/httpd.conf && \
    sed -i 's/#LoadModule cgid_module modules\/mod_cgid.so/LoadModule cgid_module modules\/mod_cgid.so/' /usr/local/apache2/conf/httpd.conf

# ドキュメントルート全体に対してCGIの実行を許可する設定を追記
RUN echo '<Directory "/usr/local/apache2/htdocs">' >> /usr/local/apache2/conf/httpd.conf && \
    echo '    Options +ExecCGI' >> /usr/local/apache2/conf/httpd.conf && \
    echo '    AddHandler cgi-script .py' >> /usr/local/apache2/conf/httpd.conf && \
    echo '</Directory>' >> /usr/local/apache2/conf/httpd.conf