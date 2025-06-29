# AWS Bedrock Docker開発環境セットアップ手順

このリポジトリは、AWS BedrockのAPIをDockerコンテナ上で安全かつ効率的に利用するための開発環境テンプレートです。

---

## セットアップ手順

### 1. 必要なもの
- AWSアカウント（Bedrock利用申請・承認済み）
- IAMユーザー（BedrockモデルのInvoke権限付与済み）
- Docker / Docker Compose
- 有効なAWS認証情報（`~/.aws/credentials`）

### 2. リポジトリのクローン & 初期化
```sh
git clone <このリポジトリのURL>
cd aws-bedrock-app
```

### 3. AWS認証情報の準備
- `~/.aws/credentials` に、利用するプロファイル（例：`default`）のアクセスキー・シークレットキーを記載してください。
- Bedrockモデル（例：Claude 2.1）へのアクセス申請・承認が完了していることをAWSコンソールで確認してください。
- IAMユーザーに `AmazonBedrockFullAccess` など必要な権限が付与されていることを確認してください。

### 4. .envファイルの作成（任意）
- プロファイル名を切り替えたい場合は `.env` ファイルを作成し、
  ```
  AWS_PROFILE=default
  ```
  などと記載してください。

### 5. Dockerイメージのビルド
```sh
docker compose build
```

### 6. コンテナの起動
```sh
docker compose up -d
```

### 7. コンテナに入って作業
```sh
docker exec -it aws-bedrock-app-bedrock-1 bash
```

### 8. サンプルスクリプトの実行
```sh
python main.py
```

---

## ファイル構成
- `Dockerfile` : Python + AWS SDK環境のDockerイメージ定義
- `docker-compose.yml` : AWS認証情報・ローカルマウント設定済み
- `requirements.txt` : 必要なPythonパッケージ
- `main.py` : Bedrock API呼び出しサンプル
- `.gitignore` : 開発用

---

## 必ず確認すること
- **Bedrockモデル（例：Claude 2.1）の「モデルアクセス申請・承認」がAWSコンソールで「有効」になっているか**
- **IAMユーザーに `AmazonBedrockFullAccess` など必要な権限が付与されているか**
- **`aws sts get-caller-identity` で認証情報が正しく認識されているか**
- **boto3/botocoreが最新バージョンか**
- **`aws bedrock list-foundation-models --region us-east-1` でモデル一覧が取得できるか**

---

## トラブルシュート
- `AccessDeniedException` → モデルアクセス申請・IAM権限・認証情報を再確認
- `UnrecognizedClientException`/`InvalidClientTokenId` → 認証情報が間違っている/無効
- `ValidationException` → APIリクエストのbodyやパラメータを再確認
- S3は見れるがBedrockだけ失敗 → Bedrock用の権限・申請状況を再確認

---

## その他
- ローカルのファイルは`./`→`/app`としてコンテナにマウントされ、即時反映されます。
- 依存パッケージを追加した場合は再ビルドが必要です。

---

## 参考

- <https://qiita.com/icoxfog417/items/869e2093e672b2b8a139>
- <https://qiita.com/minorun365/items/33d063bc62bbca1824a9>
- <https://zenn.dev/akkie1030/articles/aws-cli-setup-tutorial>
- <https://zenn.dev/ibaraki/articles/4189b05c7abd6c>
