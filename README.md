# サービスコンピューティング Web演習用 Docker環境

XAMPPの代わりにDockerを用いて、Apache + Python3 (CGI) の環境を構築・起動するためのプロジェクトです。

## 1. 起動する前の準備

必ず **Docker Desktop** アプリケーションを起動し、バックグラウンドで動いている状態（メニューバーのアイコンが緑色など）にしてください。

## 2. 環境の起動

ターミナル（コマンドプロンプト）でこのフォルダ（`docker-compose.yml`がある階層）を開き、以下のコマンドを実行します。

docker compose up -d

## 3. アクセス方法

ブラウザを開き、以下のURLにアクセスしてください。

<http://localhost:8080/sc/index.html>

## 4. 実行権限の付与（Mac向け・エラーが出た場合）

新しいPythonファイル（`.py`）を追加したり、ログファイルにエラーが出たりした場合は、コンテナ内で以下のコマンドを実行して権限を付与してください。

docker compose exec web bash -c "chmod a+x htdocs/sc/*.py && chmod a+w htdocs/sc/log/SC.log"

## 5. 環境の停止

演習が終わってWebサーバーを終了させたい場合は、以下のコマンドを実行します。

docker compose down

## トラブルシューティング

* **プログラムのソースコードがそのまま画面に表示される**
  ブラウザの古いキャッシュが残っています。`Command` + `Shift` + `R` (Mac) または `Ctrl` + `Shift` + `R` (Windows) で「ハード再読み込み」を実行してください。
* **Internal Server Errorが表示される**
  エディタでPythonファイル（`.py`）を保存する際、改行コードが「CRLF」になっているとLinux環境のDockerではエラーになります。必ず **LF** に設定して保存し直してください。
  