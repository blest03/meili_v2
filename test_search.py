# test_search.py
from config import client, index

QUERY = "хочу стать крутым программистом"
SEMANTIC_RATIO = 0.7  # 0.0 — только keyword, 0.5 — баланс, 1.0 — только вектор


def hybrid_search(query: str, semantic_ratio: float):
    return index.search(query, {
        "hybrid": {
            "semanticRatio": semantic_ratio,
            "embedder": "default",
        },
        "limit": 10,
    })


def keyword_fallback(query: str):
    """Обычный поиск на случай, если векторный embedder недоступен."""
    return index.search(query, {"limit": 10})


print(f"\nЗапрос: {QUERY!r}")
print(f"Режим: hybrid, semanticRatio={SEMANTIC_RATIO}\n")

try:
    results = hybrid_search(QUERY, SEMANTIC_RATIO)
except Exception as exc:
    print(f"⚠️ Гибридный поиск не удался: {exc}")
    print("Пробуем обычный keyword-поиск...\n")
    results = keyword_fallback(QUERY)

hits = results.get("hits", [])

if not hits:
    print("Ничего не найдено. Попробуйте изменить запрос или semanticRatio.")
else:
    print(f"Найдено документов: {len(hits)}\n")
    for rank, hit in enumerate(hits, start=1):
        print(
            f"{rank}. ID: {hit['id']} | "
            f"{hit['name']} | {hit['subject']}"
        )
        print(f"   📝 {hit['description']}")