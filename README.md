# Sound Builder

小学4〜6年生向けのフォニックス学習アプリ（Chromebook の Chrome で動作）。
文字や文字のまとまり（sh, ai, oo など）を選ぶと、その音が鳴ります。並べて「音をつなげる」で順に聞けます。

- 単一の HTML ファイル（`index.html`）。外部サーバー・有料API・個人情報の収集はありません。
- フォニックスの音は、下記の音声から切り出した録音のみを使用（合成音声では代用しません）。
- 「ことばを読む」は、ブラウザの音声合成（英語）を使用します。

## 使い方
`index.html` を Chrome で開くか、GitHub Pages で公開して開きます。

## フォルダ
- `index.html` … アプリ本体（音声は base64 で埋め込み済み）
- `tools/sound-marker.html` … 長い音声から音の範囲を登録する作業用ツール
- `tools/marks.json` … 登録した範囲（A1/A3/A4 の秒数）
- `tools/build.py` … 範囲から音を切り出してアプリに埋め込むスクリプト（ffmpeg が必要）

## 音声素材の出典とライセンス
フォニックスの音は、The Open University（TESSA）の「Teaching with Phonics」音声（A1・A3・A4）から、
このアプリ用に切り出し、音量調整と短いフェードを加えて使用しています（改変あり）。
元の音声のライセンス: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)。
このリポジトリに含まれる音声データ（`index.html` 内の埋め込み音声）も、同じ CC BY-SA 4.0 で提供されます。
