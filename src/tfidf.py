import math

class TFIDF():
    """
    Represents a TFIDF ranking model.
    Uses an inverted index to calculate document relevance scores for a query.
    """

    def __init__(self, index):
        self.index = index

    def calc_idf(self, term):
        """
        Calculate the inverse document frequency for a term
        """
        doc_freq = self.index.get_doc