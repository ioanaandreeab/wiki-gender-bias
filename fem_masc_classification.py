import random
import pickle
import nltk
from words_processing import tokenize_remove_stopwords


# finds the most common words in the documents, marking their presence
def find_features(document, word_features):
    words = tokenize_remove_stopwords(document)
    features = {}
    for word in word_features:
        features[word] = (word in words)
    return features

# get all bios
# fem_bios = open('generated/fem_bios.txt', 'r').read()
# masc_bios = open('generated/masc_bios.txt', 'r').read()
#
# documents = []
#
# mark each bio as female/male acc to gender
# for bio in fem_bios.split('\n'):
#     documents.append((bio, 'female'))
#
# for bio in masc_bios.split('\n'):
#     documents.append((bio, 'male'))
#
# tokenization, create arr w/ all words
# all_words = []
# female_words = tokenize_remove_stopwords(fem_bios)
# male_words = tokenize_remove_stopwords(masc_bios)
#
# for word in female_words:
#     all_words.append(word.lower())
#
# for word in male_words:
#     all_words.append(word.lower())
#
# all_words = nltk.FreqDist(all_words)
# top 5000 most commonly used words
# word_features = list(all_words.keys())[:5000]
#
# save word features
# save_word_features = open("pickle/word_features.pickle", "wb")
# pickle.dump(word_features, save_word_features)
# save_word_features.close()


# find the most common words in all bios, saving the feature boolean values & gender
# features & tags
# featuresets = [(find_features(bio, word_features), gender) for (bio, gender) in documents]
# random.shuffle(featuresets)
#
# split the featureset into training and testing data
# training_set = featuresets[:1400]
# testing_set = featuresets[1400:]
#
# train classifier and save
# classifier = nltk.NaiveBayesClassifier.train(training_set)
# save_classifier = open("pickle/naivebayes.pickle", "wb")
# pickle.dump(classifier, save_classifier)
# save_classifier.close()
#
# display accuracy
# print("NB Classifier accuracy percent:", (nltk.classify.accuracy(classifier, testing_set))*100)


# test from pickle files

word_features_pickle_file = open('pickle/word_features.pickle', 'rb')
word_features_pickle = pickle.load(word_features_pickle_file)
word_features_pickle_file.close()

pickle_classifier_file = open("pickle/naivebayes.pickle", "rb")
pickle_classifier = pickle.load(pickle_classifier_file)
pickle_classifier_file.close()

str_test_masc = 'Rafael Nadal Parera is a Spanish professional tennis player. He is ranked world No. 5 in singles by the Association of Tennis Professionals (ATP); he has been ranked world No. 1 for 209 weeks and finished as the year-end No. 1 five times. Nadal has won 21 Grand Slam mens singles titles, the most in history, including a record 13 French Open titles. He has won 91 ATP singles titles (including 36 Masters titles), with 62 of these on clay. Nadals 81 consecutive wins on clay is the longest single-surface win streak in the Open Era.'
feats_masc = find_features(str_test_masc, word_features=word_features_pickle)
str_test_fem = 'Simone Lucie Ernestine Marie Bertrand de Beauvoir (UK: /də ˈboʊvwɑːr/, US: /də boʊˈvwɑːr/;[3][4] French: [simɔn də bovwaʁ] (listen); 9 January 1908 – 14 April 1986) was a French existentialist philosopher, writer, social theorist, and feminist activist. Though she did not consider herself a philosopher, and even though she was not considered one at the time of her death,[5][6][7] she had a significant influence on both feminist existentialism and feminist theory.'

feats_fem = find_features(str_test_fem, word_features=word_features_pickle)
print(pickle_classifier.classify(feats_masc))
print(pickle_classifier.classify(feats_fem))