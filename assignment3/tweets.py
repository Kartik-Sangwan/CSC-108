"""Assignment 3: Tweet Analysis"""

from typing import List, Dict, TextIO, Tuple

HASH_SYMBOL = '#'
MENTION_SYMBOL = '@'
URL_START = 'http'

# Order of data in the file
FILE_DATE_INDEX = 0
FILE_LOCATION_INDEX = 1
FILE_SOURCE_INDEX = 2
FILE_FAVOURITE_INDEX = 3
FILE_RETWEET_INDEX = 4

# Order of data in a tweet tuple
TWEET_TEXT_INDEX = 0
TWEET_DATE_INDEX = 1
TWEET_SOURCE_INDEX = 2
TWEET_FAVOURITE_INDEX = 3
TWEET_RETWEET_INDEX = 4


def first_alnum_substring(text: str) -> str:
    """Return all alphanumeric characters in text from the beginning up to the
    first non-alphanumeric character, or, if text does not contain any
    non-alphanumeric characters, up to the end of text."

    >>> first_alnum_substring('')
    ''
    >>> first_alnum_substring('IamIamIam')
    'iamiamiam'
    >>> first_alnum_substring('IamIamIam!!')
    'iamiamiam'
    >>> first_alnum_substring('IamIamIam!!andMore')
    'iamiamiam'
    >>> first_alnum_substring('$$$money')
    ''
    """

    index = 0
    while index < len(text) and text[index].isalnum():
        index += 1
    return text[:index].lower()


def clean_word(word: str) -> str:
    """Return all alphanumeric characters from word, in the same order as
    they appear in word, converted to lowercase.

    >>> clean_word('')
    ''
    >>> clean_word('AlreadyClean?')
    'alreadyclean'
    >>> clean_word('very123mes$_sy?')
    'very123messy'
    """

    cleaned_word = ''
    for char in word.lower():
        if char.isalnum():
            cleaned_word = cleaned_word + char
    return cleaned_word



def extract_mentions(text: str) -> List[str]:
    """Return a list of all mentions in text, converted to lowercase, with
    duplicates included.

    >>> extract_mentions('Hi @UofT do you like @cats @CATS #meowmeow')
    ['uoft', 'cats', 'cats']
    >>> extract_mentions('@cats are #cute @cats @cat meow @meow')
    ['cats', 'cats', 'cat', 'meow']
    >>> extract_mentions('@many @cats$extra @meow?!')
    ['many', 'cats', 'meow']
    >>> extract_mentions('No valid mentions @! here?')
    []
    
    """


    result = []
    for i in range(len(text)):
        if text[i] == MENTION_SYMBOL:
            string = text[i+1:]
            word = first_alnum_substring(string)
            if word != '':
                result.append(word)
    return result


def extract_hashtags(text: str) -> List[str]:
    """Return a list containing only all of the unique hashtags in the text, in 
    the order they appear in the text converted to lowercase.
    
    >>> extract_hashtags('Hi #UofT do you like #cats #CATS #meowmeow')
    ['uoft', 'cats', 'meowmeow']
    >>> extract_hashtags('#cats are #cute #cats #cat meow @meow')
    ['cats', 'cute', 'cat']
    >>> extract_hashtags('@many #cats$extra meow?!')
    ['cats']
    >>> extract_hashtags('No valid hashtags #! here?')
    []
    
    """
    result = []
    for i in range(len(text)):
        if text[i] == HASH_SYMBOL:
            string = text[i+1:]
            word = first_alnum_substring(string)
            if word != '' and word not in result:
                result.append(word)
    return result    


def count_words(text: str, dic: Dict[str, int]) -> None:
    """
    text contains the tweet's text, and dic is a dictionary containing 
    lowercase words as keys and integer counts as values.
    Update the counts of words in the dictionary. If a word is not the 
    dictionary yet, it should be added and count initialised to 1.
    
    >>> a = {}
    >>> count_words('Google Brain re-searcher by day, singer @goodkidband by night!', a)
    >>> a == {'google': 1, 'brain': 1, 'researcher': 1, 'by': 2, 'day': 1, 'singer': 1, 'night': 1}
    True
    >>> count_words('Google the Brain re-searcher by day, singer @goodkidband by night!', a)
    >>> a == {'google': 2, 'brain': 2, 'researcher': 2, 'by': 4, 'day': 2, 'singer': 2, 'night': 2, 'the': 1}
    True
    """

    mentions = extract_mentions(text)
    hashtags = extract_hashtags(text)
    total = mentions + hashtags
    lst = text.split(' ')
    for word in lst:
        word = clean_word(word)
        if word not in total:
            if word not in dic:
                dic[word] = 1
            else:         
                dic[word] = dic[word] + 1
      
            
            
def common_words(dic: Dict[str, int], n: int)-> None:
    """Update the given dictionary dic so that it only includes the most common 
    atmost N words.If including all words with a particular word count would 
    result in a dictionary with more than N words, then none of the words with 
    that word count should be included. 

    >>> a = {'frosst': 4, 'google': 3, 'brain': 3, 'researcher': 5, 'by': 1}
    >>> common_words(a,3)
    >>> a == {'frosst': 4, 'researcher': 5}
    True
    >>> a = {'frosst': 4, 'google': 3, 'brain': 3, 'researcher': 5, 'by': 1}
    >>> common_words(a,4)
    >>> a == {'frosst': 4, 'google': 3, 'brain': 3, 'researcher': 5}
    True
    
    
    """
    i = 0
    while len(dic) > n:
        remove = []
        for key in dic:
            if dic[key] == i:
                remove.append(key)
        for item in remove:
            del dic[item]
        i += 1
        

    


def read_tweets(fil: TextIO) -> Dict[str, List[tuple]]:
    """ The keys of the dictionary should be Twitter usernames converted to 
    lowercase, and the items in the list associated with each username are 
    tuples representing the tweets that user has sent.
    
    """
   
    
    dic = {}
    line = fil.readline()
    while line != '':
        if line != '\n' and line[-2] == ':':
            usr = clean_word(line)
            dic[usr] = []
            line = fil.readline()
        if line[-2] == ':':
            dic[usr] = []
        else:
            lst = line.split(',')
            trc = lst[FILE_RETWEET_INDEX]
            rc = int(trc[:-1])
            text = ''
            line = fil.readline()
            while line != '<<<EOT\n':
                text = text + line[:]
                line = fil.readline()
            line = fil.readline()  
            tup = (text.strip(), int(lst[FILE_DATE_INDEX]), \
                   lst[FILE_SOURCE_INDEX], int(lst[FILE_FAVOURITE_INDEX]), rc)
            dic[usr].append(tup)        
    return dic        
        


def most_popular(dic: Dict[str, List[tuple]], idate: int, fdate: int) -> str:
    """dic is a dictionary produced by read_tweets. 
   idate and fdate are dates (expressed in the same int format
    as in the data file).This function returns the username of the Twitter 
    user who was most popular on Twitter between idate and fdate inclusive.
    Precondition : idate <= fdate
    
    >>> a = {'uoftcompsci': [('RT @_AlecJacobson: @UofTCompSci St. George (Downtown) Campus is hiring in Computational Geometry for a Tenure Stream Faculty Position. Tell your friends!\\n\\nhttps://t.co/O9Oui82dEA', 20181108132750, 'Twitter for Android', 0, 5), ('Congratulations to all our fall graduates!  https://t.co/iRXYwYUAKa', 20181106202405, 'Twitter for Android', 6, 1), ("RT @UaigUoft: And... it's a wrap!\\n\\nThank you to all our speakers, sponsors, and attendees for making #StartAI an unforgettable experience for us. We hope you feel the same. \\n\\nTweet us your StartAI photos! https://t.co/5zi4AAAyfS", 20181104014855, 'Twitter for Android', 0, 2), ('Today! @nickfrosst is a panelist at #StartAI!  #uoftalumni #UofT https://t.co/k50ea9qKhb (via @UofTNews)', 20181103122515, 'Twitter for Android', 5, 0)], 'uoftartsci': [('From a family of 12 kids in a Kenyan village, this #UofT grad is working to help other women get an education https://t.co/UnUMe9zMn4', 20181109193619, 'Twitter Web Client', 2, 0)]}
    >>> most_popular(a, 20181109193620, 20181113193619)
    'tie'
    >>> most_popular(a, 20181104014855, 20181109193619)
    'uoftcompsci'
    >>> most_popular(a, 20181106202405, 20181109193619)
    'uoftcompsci'
    
    """
    hc = []
    users = []
    for user in dic:
        tweets = dic[user]
        temp = 0
        for t in tweets:
            if idate <= t[TWEET_DATE_INDEX] <= fdate:
                temp += t[TWEET_FAVOURITE_INDEX] + t[TWEET_RETWEET_INDEX]
        hc.append(temp)
        users.append(user)
    maxhc = max(hc)
    uindex = hc.index(maxhc)
    hc.remove(maxhc)
    for val in hc:
        if maxhc in (val, 0):
            return 'tie'
  
    return users[uindex] 
    

def detect_author(dic: Dict[str, List[tuple]], text: str) -> str:
    """dic represents a dictionary in the format produced by 
    read_tweets and text is a tweet's text. This function returns the username 
    (in lowercase) of the most likely author of that tweet, based on the 
    hashtags they use. If all hashtags in the tweet are uniquely used by a 
    single user, then return that user's username. Otherwise, return 
    the string 'unknown'.
    
    >>> a = {'uoftcompsci': [('RT @_AlecJacobson: @UofTCompSci St. George (Downtown) Campus is hiring in Computational Geometry for a Tenure Stream Faculty Position. Tell your friends!\\n\\nhttps://t.co/O9Oui82dEA', 20181108132750, 'Twitter for Android', 0, 5), ('Congratulations to all our fall graduates!  https://t.co/iRXYwYUAKa', 20181106202405, 'Twitter for Android', 6, 1), ("RT @UaigUoft: And... it's a wrap!\\n\\nThank you to all our speakers, sponsors, and attendees for making #StartAI an unforgettable experience for us. We hope you feel the same. \\n\\nTweet us your StartAI photos! https://t.co/5zi4AAAyfS", 20181104014855, 'Twitter for Android', 0, 2), ('Today! @nickfrosst is a panelist at #StartAI!  #uoftalumni #UofT https://t.co/k50ea9qKhb (via @UofTNews)', 20181103122515, 'Twitter for Android', 5, 0)], 'uoftartsci': [('From a family of 12 kids in a Kenyan village, this #UofT grad is working to help other women get an education https://t.co/UnUMe9zMn4', 20181109193619, 'Twitter Web Client', 2, 0)]}
    >>> detect_author(a, 'buddy and no hashtags uoft')
    'unkown'
    >>> detect_author(a, '#uoft single common hashtag')
    'unkown'
    >>> detect_author(a, '#STARTai single hashtag case sensitive')
    'uoftcompsci'
    >>> detect_author(a,'#uoft and #startai one common and both hashtags in one')
    'unkown'
    >>> detect_author(a,'#uoftsas and #startai random hashtag and one common')
    'unkown'
    """
    hashtags = extract_hashtags(text)
    u_hashtags = {}
    for user in dic:
        tweets = dic[user]
        u_hashtags[user] = []
        for tweet in tweets:
            t = tweet[TWEET_TEXT_INDEX]
            u_hashtags[user] = u_hashtags[user] + extract_hashtags(t)
    f = 0
    for user in u_hashtags:
        lst = u_hashtags[user]
        for item in hashtags:
            if item in lst:
                f += 1
                tuser = user
    if f == len(hashtags) and f != 0:
        return tuser
    else:
        return 'unkown'
    
    
    
   
if __name__ == '__main__':
    pass

    # If you add any function calls for testing, put them here.
    # Make sure they are indented, so they are within the if statement body.
    # That includes all calls on print, open, and doctest.

    #import doctest
    #doctest.testmod()
