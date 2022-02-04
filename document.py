# Import function to perform tokenization   ### from .token_utils import tokenize
from token_utils import tokenize
from collections import Counter
import matplotlib.pyplot as plt


# Define Document class
class Document:
    """A class for text analysis

    :param text: string of text to be analyzed
    :ivar text: string of text to be analyzed; set by `text` parameter
    """
    # Method to create a new instance of MyClass
    def __init__(self, text):
        # Store text parameter to the text attribute
        self.text = text
        # pre tokenize the document with non-public tokenize method
        self.tokens = self._tokenize()
        # pre tokenize the document with non-public count_words
        self.word_counts = self._count_words()

    def _tokenize(self):
        #return tokenize(self.text)
        return self.text.split()

    # non-public method to tally document's word counts with Counter
    def _count_words(self):
        #return Counter([i.string for i in self.tokens])
        return Counter(self.tokens)


    def plot_counter(self, n_most_common=5):
        # Subset the n_most_common items from the input Counter object
        self.top_items = self.most_common(n_most_common)
        # Plot `top_items`
        #plot_counter_most_common(top_items)  ##########################################################################

        plt.style.use('bmh')

        fig, ax = plt.subplots(figsize=(12,8))

        ax.bar([i[0] for i in self.top_items],
               [i[1] for i in self.top_items])

        #plt.title(self, fontsize=14)  how to set the title of each plot?  thinking
        #ax.set_xticklabels([i[0] for i in self.top_items], rotation=45)
        ax.set_ylabel('Number of counts')

        plt.show()



    def filter_word_counts(self, first_char):
        """Pass in a Counter object, filter with 'first_char'"""
        return Counter({ k: v for k, v in self.items() if first_char in k})  ####################################
