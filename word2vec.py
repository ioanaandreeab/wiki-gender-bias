import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
import numpy as np
import nltk
from words_processing import tokenize_remove_stopwords
import gensim

# MODELS
# bios = pd.read_csv('generated/gendered_data.csv')
# dict for storing the texts
# texts = dict()
# genders = list(bios['gender'].unique())
# for gender in genders:
#     text = []
#     abstracts = bios[bios['gender'] == gender]['abstract'].values
#     for abstract in abstracts:
#         token = tokenize_remove_stopwords(abstract)
#         token = [word.lower() for word in token if word.isalpha()]
#         text.append(token)
#     texts[gender] = text

# models = dict()
# savename = time.strftime("generated/w2v_model_")
# for gender in genders:
#     print('Creating model for %s' % gender)
#     model = gensim.models.Word2Vec(texts[gender], vector_size=150, window=10, min_count=5)
#     print('Finished creating model, moving to training')
#     model.train(token, total_examples=len(token), epochs=10)
#     print('Finished training model on %s' % gender)
#     models[gender] = model
#     model.wv.save_word2vec_format(savename + gender + '.txt', binary=False)
# print('Finished Training')


# load the models
models = dict()
genders = ['male', 'female']
savename = 'generated/w2v_model_'
for gender in genders:
    models[gender] = gensim.models.KeyedVectors.load_word2vec_format(savename + gender + '.txt',
                                                                    binary=False)


def extract_words(most_similar):
    words = []
    for entry in most_similar:
        words.append(entry[0])
    return words


def show_context(word, models, topn=10):
    topn = int(topn)
    context = pd.DataFrame(columns=list(models.keys()))
    for gender in models:
        if word not in models[gender].key_to_index:
            print('Error! Word %s not in vocabulary of %s' % (word, gender))
        else:
            words = extract_words(models[gender].most_similar(positive=word, topn=topn))
            context[gender] = words
    return context


print(show_context('work', models))