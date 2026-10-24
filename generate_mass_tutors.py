# generate_mass_tutors.py
import random
from config import client, index

first_names = [
    "Иван", "Ольга", "Сергей", "Анна",
    "Владимир", "Елена", "Дмитрий", "Наталья",
]
last_names = [
    "Петров(а)", "Сидоров(а)", "Кузнецов(а)",
    "Смирнов(а)", "Попов(а)", "Васильев(а)",
]
subjects = [
    "Математика", "Физика", "Химия",
    "Биология", "История", "Информатика",
]

phrases = [
    "Подготовка к ОГЭ и ЕГЭ на высокие баллы.",
    "Помощь с домашними заданиями и подтягивание успеваемости.",
    "Опыт работы более 5 лет, индивидуальный подход к каждому ученику.",
    "Углубленное изучение предмета для участия в олимпиадах.",
    "Объясняю сложные темы простыми словами и наглядными примерами.",
]

big_tutors_list = []

for i in range(1, 51):  # ровно 50 документов
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    subject = random.choice(subjects)
    # Две разные фразы, без повторов
    phrase_1, phrase_2 = random.sample(phrases, k=2)
    description = (
        f"Преподаватель по предмету {subject}. {phrase_1} {phrase_2}"
    )

    big_tutors_list.append({
        "id": i,
        "name": name,
        "subject": subject,
        "description": description,
    })

task = index.add_documents(big_tutors_list)
print(
    f"Отправлено {len(big_tutors_list)} репетиторов. "
    f"ID задачи: {task.task_uid}. Ожидаем индексацию..."
)

# add_documents не блокирует выполнение: документы не сразу доступны для поиска.
# В официальном клиенте wait_for_task дожидается завершения задачи.
finished = client.wait_for_task(task.task_uid)

if finished.status != "succeeded":
    print(f"❌ Задача завершилась со статусом: {finished.status}")
    print(f"   Ошибка: {finished.error}")
else:
    print("✅ Индексация завершена, документы доступны для поиска.")