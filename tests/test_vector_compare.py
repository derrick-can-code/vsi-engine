import math
import pytest
from search.vector_compare import VectorCompare


@pytest.fixture
def vc():
  return VectorCompare()


def test_concordance_counts_words(vc):
  result = vc.concordance("the cat sat on the mat")
  assert result["the"] == 2
  assert result["cat"] == 1


def test_magnitude_of_simple_vector(vc):
  assert vc.magnitude({"a": 3, "b": 4}) == 5.0


def test_identical_documents_have_similarity_one(vc):
  a = vc.concordance("cats and dogs")
  b = vc.concordance("cats and dogs")
  assert math.isclose(vc.relation(a, b), 1.0)


def test_unrelated_documents_have_similarity_zero(vc):
  a = vc.concordance("cats and dogs")
  b = vc.concordance("rockets and planets")
  assert vc.relation(a, b) == 0.0


def test_empty_document_does_not_crash(vc):
  a = vc.concordance("")
  b = vc.concordance("something")
  assert vc.relation(a, b) == 0.0