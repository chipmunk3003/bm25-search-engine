from src.tokeniser import tokenise


def test_lowercase():
    assert tokenise("HELLO")== ["hello"]

def test_punctuation():
    assert tokenise("hello!") == ["hello"]

def test_splits():
    assert tokenise("hello world") == ["hello", "world"]

def test_stopwords():
    assert tokenise("a of on I for with the at from in to") == []

def test_splits_full():
    assert tokenise("The Quick Brown Fox!") == ["quick", "brown", "fox"]

def test_empty_string():
    assert tokenise("") == []

def test_numbers_kept():
    assert tokenise("horse number 24") == ["horse", "number", "24"]



