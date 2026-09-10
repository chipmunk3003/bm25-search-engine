from src.index import InvertedIndex


def test_add_document():
    index = InvertedIndex()
    index.add_document(1,"The aircraft is flying")

    assert index.num_documents == 1


def test_postings_contain_correct_document():
    index = InvertedIndex()
    index.add_document(1,"The aircraft is flying")
    postings = index.get_postings("aircraft")

    assert 1 in postings


def test_term_frequency():
    index = InvertedIndex()
    index.add_document(1,"The aircraft is flying")
    postings = index.get_postings("aircraft")

    assert postings[1] == 2


def test_document_length():
    index = InvertedIndex()
    index.add_document(1,"The aircraft is flying")
    
    assert index.get_document_length(1) == 2


def test_document_frequency():
    index = InvertedIndex()
    index.add_document(1,"The aircraft is flying")
    index.add_document(2,"aircraft wings")

    assert index.get_document_frequency("aircraft") == 2
    assert index.get_document_frequency("design") == 1


def test_unknown_term():
    index = InvertedIndex()
    index.add_document(1,"The aircraft is flying")

    assert index.get_postings("banana") == {}


def test_average_document_length():
    index = InvertedIndex()
    index.add_document(1,"aircraft design")
    index.add_document(2,"aircraft wings are useful")

    assert index.get_average_document_length() == 3


def test_get_all_document_ids():
    index = InvertedIndex()
    index.add_document(1,"aircraft design")
    index.add_document(2,"aircraft wings")
    index.add_document(3,"engine design")

    assert index.get_all_document_ids() == {1, 2, 3}




