# check_status.py
from config import client

tasks = client.get_tasks({"limit": 5})

print("Статус последних процессов:\n")
for task in tasks.results:
    print(f"— Задача №{task.uid}")
    print(f"  Тип:    {task.type}")
    print(f"  Статус: {task.status}")
    if task.status == "failed":
        print(f"  ❌ Ошибка: {task.error}")
    print()