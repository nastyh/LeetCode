"""
functions to calculate term frequency and inverse document frequency in a library of docs/strings.

Term frequency = count of term t in doc d / total num of terms in doc d: how often a term t appears in doc d
Inverse doc frequency = log(tot num of docs / num of docs w/ term t) + 1: importance of a term, reduce the weight of terms that appear in many docs
Multi
"""
import math
from collections import Counter

class TextAnalyzer:
    def __init__(self, documents):
        """
        Initialize with a list of documents (strings).
        """
        self.documents = documents
        self.doc_count = len(documents)
        self.term_doc_counts = self._calculate_term_doc_counts()

    def _calculate_term_doc_counts(self):
        """
        Calculate how many documents each term appears in.
        """
        term_doc_counts = Counter()
        for doc in self.documents:
            unique_terms = set(doc.split())
            for term in unique_terms:
                term_doc_counts[term] += 1
        return term_doc_counts

    def term_frequency(self, term, document):
        """
        Calculate term frequency (TF) for a given term in a document.
        """
        words = document.split()
        term_count = words.count(term)
        return term_count / len(words) if len(words) > 0 else 0

    def inverse_document_frequency(self, term):
        """
        Calculate inverse document frequency (IDF) for a given term.
        """
        doc_count_with_term = self.term_doc_counts.get(term, 0)
        if doc_count_with_term == 0:
            return 0
        return math.log(self.doc_count / doc_count_with_term) + 1

    def tf_idf(self, term, document):
        """
        Calculate TF-IDF for a given term in a document.
        """
        tf = self.term_frequency(term, document)
        idf = self.inverse_document_frequency(term)
        return tf * idf

# Sample documents
documents = [
    "the cat sat on the mat",
    "the dog barked at the cat",
    "the bird sang a song",
]

# Initialize TextAnalyzer
analyzer = TextAnalyzer(documents)

# Calculate TF for a term in a specific document
term = "the"
doc_index = 0
tf = analyzer.term_frequency(term, documents[doc_index])
print(f"TF('{term}', doc[{doc_index}]): {tf:.4f}")

# Calculate IDF for a term
idf = analyzer.inverse_document_frequency(term)
print(f"IDF('{term}'): {idf:.4f}")

# Calculate TF-IDF for a term in a specific document
tf_idf = analyzer.tf_idf(term, documents[doc_index])
print(f"TF-IDF('{term}', doc[{doc_index}]): {tf_idf:.4f}")
