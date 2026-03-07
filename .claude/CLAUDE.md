# CLAUDE.md

live coding用

## 目的

live codingで徐々にコードをお駆逐していくためのリポジトリ

## 概要

### backend/

- python 3.14
- uv プロジェクト
- FastAPI

### postgresql/

ローカル実行用の PostgreSQL コンテナ

### redis/

ローカル実行用の Redis コンテナ

### frontend/

未定

## テスト

### backend
backendディレクトリで `uv run pytest` で backend のテストが走るようにする
