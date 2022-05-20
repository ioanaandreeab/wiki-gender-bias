import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from collections import Counter
from words_processing import tokenize_remove_stopwords
import seaborn as sns
import time


def visualize_gender_distribution():
    df_gendered_data = pd.read_csv('generated/gendered_data.csv')
    # compute count by gender
    # visualize graph
    gender_counts = df_gendered_data.value_counts(subset=['gender']).sort_values(ascending=False)
    print(gender_counts)
    print("In total there are {} different genders".format(gender_counts.count()))

    pl = gender_counts.plot(kind="bar", x="gender", y="count", figsize=(10, 5), log=True, \
                                       alpha=0.5, color="purple", rot=0)
    for p in pl.patches:
        disp = '{:d}'.format(p.get_height())
        pl.annotate(disp, (p.get_x() + 0.16, p.get_height() * 1.1))

    pl.set_xlabel("Gender")
    pl.set_ylabel("Number of biographies (Log scale)")
    pl.set_title("Number of biographies by gender")
    plt.savefig('generated/gender_distribution.png')
    plt.show()


def word_cloud(gender):
    df_gendered_data = pd.read_csv('generated/gendered_data.csv')
    df_specific_gender = df_gendered_data[df_gendered_data['gender'] == gender]
    print(df_specific_gender)
    all_abstracts = df_specific_gender['abstract'].tolist()

    token_all_abstracts = [tokenize_remove_stopwords(i) for i in all_abstracts]
    flat_alldes = [item for sublist in token_all_abstracts for item in sublist]

    clean_flat = [w for w in flat_alldes]

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
    plt.savefig('generated/' + gender + '_wordcloud.png')
    # show the result
    plt.show()


# visualize_gender_distribution()
# word_cloud('male')
# word_cloud('female')

df = pd.read_csv('generated/gendered_data.csv')

genders = df['gender'].unique()
columns=['Gender', 'Number of Bios', 'Number of Words', 'Word/Bio Ratio',
         'Number of Unique Words', 'Unique Words', 'Words']
data = pd.DataFrame(columns=columns)
data['gender'] = genders
data.set_index('gender', inplace=True)

# Extracting bios for different genders
complete_bios = dict()  # All bios in one string
texts = df.groupby('gender')['abstract'].apply(' '.join).reset_index()

for gender in genders:
    complete_bios[gender] = texts[texts['gender'] == gender]['abstract'].values[0]
    n = len(complete_bios[gender])
    data.loc[gender, 'Number of Bios'] = sum(df['gender'] == gender)
    data.loc[gender, 'Number of Words'] = n
    data.loc[gender, 'Word/Bio Ratio'] = n / sum(df['gender'] == gender)


print(data['Number of Bios'])

# Plot number of bios per gender
sns.set_style('darkgrid')
sns.set_palette('PuBuGn_d')
plt.figure(figsize=(7, 5))
sns.barplot(y=data['Number of Bios'], x=data.index, palette='PuBuGn_d')
plt.xticks(rotation='vertical')
plt.title('Number of Bios per Gender')
plt.tight_layout()
savename = time.strftime("generated/%d%m%y_%H%M%S_") + 'BiosPerGender.png'
plt.savefig(savename, dpi=600)
plt.show()

# Plot number of words per gender
plt.figure(figsize=(7, 5))
sns.barplot(x=data.index, y=data['Number of Words'], palette='PuBuGn_d')
plt.xticks(rotation='vertical')
plt.title('Number of Words per Gender')
plt.tight_layout()

savename = time.strftime("generated/%d%m%y_%H%M%S_") + 'WordsPerGender.png'
plt.savefig(savename, dpi=600)
plt.show()

# Plot average words per bio per gender
plt.figure(figsize=(7, 5))
sns.barplot(x=data.index, y=data['Word/Bio Ratio'], palette='PuBuGn_d')
plt.xticks(rotation='vertical')
plt.title('Average Number of Words per Bio per Gender')
plt.tight_layout()

savename = time.strftime("generated/%d%m%y_%H%M%S_") + 'AverageWordsPerGender.png'
plt.savefig(savename, dpi=600)
plt.show()

for gender in genders:
    print('Currently processing %s' % gender)
    data.loc[gender, 'Words'] = tokenize_remove_stopwords(complete_bios[gender])
    data.loc[gender, 'Unique Words'] = list(set(data.loc[gender, 'Words']))
    data.loc[gender, 'Number of Unique Words'] = len(data.loc[gender, 'Unique Words'])

print(data)

savename = time.strftime("generated/%d%m%y_%H%M%S_") + 'data.pickle'
data.to_pickle(savename)

data = pd.read_pickle('pickle/processed_data.pickle')
# Plot number of unique words
plt.figure(figsize=(7, 5))
sns.barplot(x=data.index, y=data['Number of Unique Words'], palette='PuBuGn_d')
plt.xticks(rotation='vertical')
plt.title('Number of Unique Words per gender')
plt.tight_layout()

savename = time.strftime("generated/%d%m%y_%H%M%S_") + 'UniqueWordsPerGender.png'
plt.savefig(savename, dpi=600)
plt.show()