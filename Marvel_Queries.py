# import libraries #
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read lbgtq rights by country csv into dataframe.
lgbtq_df = pd.read_csv('/Users/jaceellis/anaconda_projects/db/lgbtq_rights_by_country.csv')
# rename 'Territory' column in order to merge with country by continent dataset.
lgbtq_df.rename(columns={'Territory': 'Country'}, inplace=True)

# read countries by continent into dataframe.
country_bycontinent = pd.read_csv('/Users/jaceellis/anaconda_projects/db/Countries_by_continents.csv')

#LGBTQ_w_territory.info()
#country_bycontinent.info()

# merge dataframes on 'Country' column
combined_df = pd.merge(lgbtq_df, country_bycontinent, on='Country')

sns.countplot(x=combined_df['Same-sex marriage'])
plt.xlabel('Same-sex marriage legality')
plt.show()
