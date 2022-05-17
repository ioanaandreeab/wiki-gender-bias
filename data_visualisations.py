import pandas as pd
import matplotlib.pyplot as plt

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