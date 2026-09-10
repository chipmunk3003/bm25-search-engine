from collections import defaultdict

from src.tokeniser import tokenise


class InvertedIndex():
    """
    An inverted index mapping terms to the documents in which they occur
    """

    def __init__(self):
        self.index = dict(dict())
        self.doc_count = 0
        self.doc_length = dict()


    def add_document(self, doc_id, text):
        """
        Adds a document to the inverted index
        """
        tokens = tokenise(text)
        self.doc_length[doc_id] = len(tokens)
        self.doc_count += 1
        term_count = defaultdict(int)

        for token in tokens:
            term_count[token] += 1

        for term, freq in term_count.items():
            self.index[term][doc_id] = freq


    def get_matches(self, term):
        """
        Returns documents containing a term
        """
        return self.index.get(term, {})

        
    def get_doc_length(self, doc_id):
        """
        Returns number of tokens in a document
        """
        return self.doc_length.get(doc_id, 0)
   

    def get_average_doc_length(self):
        """
        Calculates the average doc length
        """
        if self.doc_count == 0:
            return 0

        total_len = sum(self.doc_length.values())
        return total_len/self.doc_count
        

    def get_number_of_docs_found_in(self, term):
        """
        Returns the number of documents a token is present in.
        """
        return len(self.get_matches(term))


    def get_all_doc_ids(self):
        """
        Returns all the document ids stored
        """

        return set(self.doc_length.keys())
    