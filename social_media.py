from text_analyzer import Document
from collections import Counter


# Define a SocialMedia class that is a child of the `Document class`
class SocialMedia(Document):
    def __init__(self, text):
        Document.__init__(self, text)
        self.hashtag_counts = self._count_hashtags()
        self.mention_counts = self._count_mentions()

    def _count_hashtags(self):
        # Filter attribute so only words starting with '#' remain
        return SocialMedia.filter_word_counts(self.word_counts, first_char='#')  ###########################################

    def _count_mentions(self):
        # Filter attribute so only words starting with '@' remain
        return SocialMedia.filter_word_counts(self.word_counts, first_char='@')


'''def filter_word_counts(word_count, first_char):
    #num = 0
    mark_count = dict()
    for i, j in word_count.items():
        if i[0] == first_char:  ###########################################################################################
            #num += j
            mark_count[i] = j
    return mark_count'''
