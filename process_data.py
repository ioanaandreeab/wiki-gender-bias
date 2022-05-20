import pandas as pd


def determine_gender(text):
    male_pronouns = ['he', 'his', 'himself']
    female_pronouns = ['she', 'her', 'hers', 'herself']
    male_count = sum(1 if word in male_pronouns else 0 for word in text.lower().split())
    female_count = sum(1 if word in female_pronouns else 0 for word in text.lower().split())

    target_gender = 'male' if male_count >= female_count else 'female'
    return target_gender


df_1 = pd.read_csv('data/people_bios_1.csv')
df_2 = pd.read_csv('data/people_bios_2.csv')
df_3 = pd.read_csv('data/people_bios_3.csv')
df_4 = pd.read_csv('data/people_data_dbpedia.csv')
df = pd.concat([df_1, df_2, df_3, df_4], ignore_index=True)
# determine gender
df['gender'] = df.apply(lambda row: determine_gender(row['abstract']), axis=1)
df.to_csv('generated/gendered_data.csv')
print(df)
print('male bios: ' + str(list(df.gender).count('male')))
print('female bios: ' + str(list(df.gender).count('female')))

fem_df = df[df['gender'] == 'female']
masc_df = df[df['gender'] == 'male']

with open('generated/fem_bios.txt', 'w') as f:
    for text in fem_df['abstract'].tolist():
        f.write(text + '\n')

with open('generated/masc_bios.txt', 'w') as f:
    for text in fem_df['abstract'].tolist():
        f.write(text + '\n')