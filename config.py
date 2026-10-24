# config.py
import os
import meilisearch
from dotenv import load_dotenv

load_dotenv()

MEILI_URL = os.getenv("MEILI_URL", "http://localhost:7700")
MEILI_API_KEY = os.getenv("MEILI_API_KEY")

if not MEILI_API_KEY:
    raise RuntimeError(
        "Не задан MEILI_API_KEY. Создайте .env по образцу .env.example."
    )

client = meilisearch.Client(MEILI_URL, MEILI_API_KEY)
index = client.index("tutors")