# Import parent class for inheritance
from text_analyzer import SocialMedia


# Define a Tweet class that inherits from SocialMedia
class Tweets(SocialMedia):
    def __init__(self, text):
        # Call parent's __init__ with super()
        super().__init__(text)   ###
        # Define retweets attribute with non-public method
        self.retweets = self._process_retweets() #---------------------------------------
                        #------------------- "self._process_retweets" meaning our aproach correct ------------------
    def _process_retweets(self):
        # Filter tweet text to only include retweets
        retweet_text = self.filter_lines(first_char='RT')  ##----------------------------
        # Return retweet_text as a SocialMedia object
        #return SocialMedia(retweet_text)
        print(retweet_text)
        return retweet_text


    def filter_lines(self, first_char):
        # The function work a filter, keep input 'text' start with 'RT'
        #print(self.text)     This is a tweet['text'], the string
        if self.text[:2]==first_char:  # The self is the object, we need to use its attribute - 'text' -------------
            return self
'''
        rt = str()
        for i in self:
            if i[:2] == first_char:
                rt = rt + ' ' + str(i)

        return rt
'''
