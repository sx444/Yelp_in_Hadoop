# q5 final conclusion

import pandas as pd
from datetime import datetime

# review stars data
data1 = pd.read_table("q5_1", header=None) # load the txt file to pandas
df_star = pd.DataFrame(data1)
df_star.columns = ['business_id','month','total_stars','number_review','average_stars'] # rename the columns

# business data
data2 = pd.read_csv("20_businesses.csv", header=None)
df_business = pd.DataFrame(data2)
df_business.columns = ['stars','business_name','business_id']

# merge the two dataframes
df = pd.merge(df_business, df_star, on='business_id')
df.drop('business_id', axis=1, inplace=True)

# change the month name to number
for i in range(len(df['month'])):
	df['month'][i] = datetime.strptime(df['month'][i], "%B").strftime('%m')

result = df.sort_values(by=['stars','business_name','month'],ascending=[True,True,True])
result.to_csv('q5ans', sep='\t')