import pandas as pd


def determine_gender(text):
    male_pronouns = ['he', 'his', 'himself']
    female_pronouns = ['she', 'her', 'hers', 'herself']
    male_count = sum(1 if word in male_pronouns else 0 for word in text.lower().split())
    female_count = sum(1 if word in female_pronouns else 0 for word in text.lower().split())

    target_gender = 'male' if male_count >= female_count else 'female'
    return target_gender


df = pd.read_csv('people_bios.csv')
# determine gender
df['gender'] = df.apply(lambda row: determine_gender(row['abstract']), axis=1)
df.to_csv('gendered_data.csv')
print(df)
print('male bios: ' + str(list(df.gender).count('male')))
print('female bios: ' + str(list(df.gender).count('female')))