from search.vector_compare import VectorCompare
from search.documents import DOCUMENTS

def build_index(vc: VectorCompare, documents: dict) -> dict:
  return {doc_id: vc.concordance(text.lower()) for doc_id, text in documents.items()}

def search(vc: VectorCompare, index: dict, documents: dict, query: str) -> list:
  query_vector = vc.concordance(query.lower())
  results = []
  for doc_id, doc_vector in index.items():
    score = vc.relation(query_vector, doc_vector)
    if score > 0:
      results.append((score, documents[doc_id][:100]))
  results.sort(reverse=True)
  return results


def main():
  vc = VectorCompare()
  index = build_index(vc, DOCUMENTS)

  query = input("Enter search term: ")
  results = search(vc, index, DOCUMENTS, query)

  if not results:
    print("No matches found.")
  for score, snippet in results:
    print(f"{score:.4f}  {snippet}")


if __name__ == "__main__":
  main()