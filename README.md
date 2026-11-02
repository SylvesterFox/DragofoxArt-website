# DragofoxArt

## Запуск через Docker

Для локального запуска с SQLite и сохранением загруженных изображений:

```sh
cp .env.example .env
docker compose up --build -d
```

Сайт будет доступен на <http://localhost:8000>. База данных и папка `media` хранятся в Docker volumes и переживают пересоздание контейнеров. Перед публикацией измените `DJANGO_SECRET_KEY` в `.env` на случайный секрет.

Для развёртывания задайте переменные окружения:

```sh
DJANGO_SECRET_KEY='случайный-длинный-секрет' \
DJANGO_ALLOWED_HOSTS='example.com' \
DJANGO_CSRF_TRUSTED_ORIGINS='https://example.com' \
docker compose up -d
```

## Публикация образа в GHCR

Workflow `.github/workflows/publish-container.yml` публикует `ghcr.io/sylvesterfox/dragofoxart-website:main` после push в ветку `main`. Для версии создайте и отправьте тег SemVer:

```sh
git tag v1.2.3
git push origin v1.2.3
```

Для такого тега workflow опубликует `v1.2.3`, `1.2.3`, `1.2`, `1` и `latest`. Образ версии можно получить так:

```sh
docker pull ghcr.io/sylvesterfox/dragofoxart-website:v1.2.3
```

При первом запуске workflow GitHub создаст пакет в Container Registry. Доступ к приватному пакету настраивается в настройках самого пакета GitHub.
