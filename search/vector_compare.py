from collections import Counter
import math 
class VectorCompare:
  def concordance(self, document: str) -> Counter:
    if not isinstance(document, str):
      raise TypeError("Document must be a string")
    return Counter(document.split())

  def magnitude(self, concordance: Counter) -> float:
    if not isinstance(concordance, dict):
      raise ValueError("concordance must be a dict-like object")
    return math.sqrt(sum(count**2 for count in concordance.values()))

  def relation(self, concordance1: Counter, concordance2: Counter) -> float:
    dot_product = sum(
      count * concordance2.get(word, 0)
      for word, count in concordance1.items()
    )
    denominator = self.magnitude(concordance1) * self.magnitude(concordance2)
    if denominator == 0:
      return 0.0
    return dot_product/denominator #returns cosine value from 0 to 1