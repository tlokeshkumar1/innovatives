import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
import re

lemmatizer = WordNetLemmatizer()

# function to convert nltk tag to wordnet tag
def nltk_tag_to_wordnet_tag(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

# function to lemmatize sentence
def lemmatize_sentence(sentence):
    # tokenize the sentence and find the POS tag for each token
    nltk_tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
    # tuple of (token, wordnet_tag)
    wordnet_tagged = map(lambda x: (x[0], nltk_tag_to_wordnet_tag(x[1])), nltk_tagged)
    lemmatized_sentence = []
    for word, tag in wordnet_tagged:
        if tag is None:
            # if there is no available tag, append the token as is
            lemmatized_sentence.append(word)
        else:
            # else use the tag to lemmatize the token
            lemmatized_sentence.append(lemmatizer.lemmatize(word, tag))
    return " ".join(lemmatized_sentence)

# function to parse user input
def parse_input(user_input):
    # lemmatize user input
    lemmatized_input = lemmatize_sentence(user_input)
    # tokenize lemmatized input
    tokens = nltk.word_tokenize(lemmatized_input)
    # create list of verb tags
    verb_tags = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
    # create list of noun tags
    noun_tags = ['NN', 'NNS', 'NNP', 'NNPS']
    # create list of verb and noun tags
    verb_noun_tags = verb_tags + noun_tags
    # create empty lists
    verbs = []
    nouns = []
    # loop through tokens
    for token, tag in nltk.pos_tag(tokens):
        # check if tag is verb
        if tag in verb_tags:
            # append verb to verb list
            verbs.append(token)
        # check if tag is noun
        elif tag in noun_tags:
            # append noun to noun list
            nouns.append(token)
    # create dict of verb and noun lists
    verb_noun_dict = {'verbs': verbs, 'nouns': nouns}
    # return dict
    return verb_noun_dict

# function to make decision based on user input
def make_decision(user_input):
    # parse user input
    parsed_input = parse_input(user_input)
    # get verbs and nouns from parsed input
    verbs = parsed_input['verbs']
    nouns = parsed_input['nouns']
    # check if user input contains verb
    if len(verbs) > 0:
        # get first verb
        verb = verbs[0]
        # check if verb is 'turn'
        if verb == 'turn':
            # check if user input contains noun
            if len(nouns) > 0:
                # get first noun
                noun = nouns[0]
                # check if noun is 'on'
                if noun == 'on':
                    # turn on electronic system
                    print('Turning on electronic system...')
                    # return True
                    return True
                # check if noun is 'off'
                elif noun == 'off':
                    # turn off electronic system
                    print('Turning off electronic system...')
                    # return True
                    return True
    # return False
