# Koki Yoshikawa — Portfolio

生成AIを活用したシステム開発・教材制作・映像制作のポートフォリオ。

## 更新方法

- content.json：プロフィール、実績、連絡先
- template.html：ページ構成
- style.css：デザインとレスポンシブ表示
- app.js：実績の絞り込み

Python標準ライブラリのみでビルドできます。

```sh
python build.py
python -m http.server 8765 --bind 127.0.0.1 --directory public
```

mainへpushするとGitHub Actionsがビルドし、public/のみGitHub Pagesへ配信します。
変更はGit履歴に記録されます。戻す場合は対象コミットをgit revertしてpushします。
顧客の成果物・内部資料・秘密情報はこのリポジトリへ追加しません。
