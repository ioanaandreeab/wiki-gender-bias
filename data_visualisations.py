import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from nltk.tokenize import word_tokenize
from collections import Counter
import string


def visualize_gender_distribution():
    df_gendered_data = pd.read_csv('gendered_data.csv')
    # compute count by gender
    # visualize graph
    gender_counts = df_gendered_data.value_counts(subset=['gender']).sort_values(ascending=False)
    print(gender_counts)
    print("In total there are {} different genders".format(gender_counts.count()))
    # dataframe to pandas

    pl = gender_counts.plot(kind="bar", x="gender", y="count", figsize=(10, 5), log=True, \
                                       alpha=0.5, color="purple", rot=0)
    for p in pl.patches:
        disp = '{:d}'.format(p.get_height())
        pl.annotate(disp, (p.get_x() + 0.16, p.get_height() * 1.1))

    pl.set_xlabel("Gender")
    pl.set_ylabel("Number of biographies (Log scale)")
    pl.set_title("Number of biographies by gender")
    plt.show()


def word_cloud(gender):
    df_gendered_data = pd.read_csv('gendered_data.csv')
    df_specific_gender = df_gendered_data[df_gendered_data['gender'] == gender]
    print(df_specific_gender)
    all_abstracts = df_specific_gender['abstract'].tolist()

    token_all_abstracts = [word_tokenize(i) for i in all_abstracts]
    flat_alldes = [item for sublist in token_all_abstracts for item in sublist]

    useless_words = list(STOPWORDS) + list(string.punctuation)
    clean_flat = [w for w in flat_alldes if not w in useless_words and len(w) > 1]
    clean_flat = [word for line in clean_flat for word in line.split('.')]
    clean_flat_string = " ".join(clean_flat)
    print(Counter(clean_flat).most_common(30))
    wcloud = WordCloud(
        width=3000,
        height=2000,
        background_color='white').generate(clean_flat_string)
    # make figure to plot
    plt.figure()
    # plot words
    plt.imshow(wcloud, interpolation="bilinear")
    # remove axes
    plt.axis("off")
    # add title
    plt.title(f'Most common words in wiki abstracts of gender: {gender}')
    # show the result
    plt.show()


# visualize_gender_distribution()
word_cloud('male')
word_cloud('female')