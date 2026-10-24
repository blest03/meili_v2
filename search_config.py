# search_config.py
from config import client, index

print("Настройка локальной векторной модели E5 в Meilisearch...")

config_task = index.update_settings({
    "embedders": {
        "default": {
            "source": "huggingFace",
            "model": "intfloat/multilingual-e5-small",
            # В шаблон стоит включать максимум смысла, но не лишние поля.
            # name тоже полезно добавить: поиск по имени станет семантически сильнее.
            "documentTemplate": (
                "Репетитор {{doc.name}}. "
                "Предмет: {{doc.subject}}. "
                "Описание: {{doc.description}}"
            ),
        }
    },
    "localizedAttributes": [
        {
            "attributePatterns": ["*"],
            "locales": ["rus"],
        }
    ],
    "searchableAttributes": [
        "subject",
        "name",
        "description",
    ],
    "filterableAttributes": [
        "subject",
    ],
    "stopWords": [
        "ищу", "для", "по", "ко", "к", "в", "на", "с",
        "о", "об", "за", "из", "хочу", "нужен",
    ],
})

print(f"Настройки отправлены. ID задачи: {config_task.task_uid}. Ожидаем...")

finished = client.wait_for_task(config_task.task_uid)

if finished.status != "succeeded":
    print(f"❌ Не удалось применить настройки: {finished.status}")
    print(f"   Ошибка: {finished.error}")
else:
    print("✅ Настройки индекса применены.")