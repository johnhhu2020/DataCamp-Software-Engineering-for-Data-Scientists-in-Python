# Import the class to test
from text_analyzer import Document
from collections import Counter


# Test tokens attribute on DOcument class
def test_document_tokens():
    doc = Document('Hello, my name is John, nice to meet you.')

    assert doc.tokens == ['Hello,', 'my', 'name', 'is', 'John,', 'nice', 'to', 'meet', 'you.']


# Test edge case of blank document
def test_document_empty():
    doc = Document('')

    assert doc.tokens == []
    assert doc.word_counts == Counter()
