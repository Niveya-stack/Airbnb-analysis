import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pymongo

client = pymongo.MongoClient("mongodb+srv://niveya:Nive1402@cluster0.gzhucez.mongodb.net/")
db = client.airbnb
collection = db.listingsAndReviews

data = []
for i in collection.find():
  data.append(i)

#data

airbnb = pd.DataFrame(data)

airbnb.to_csv('airbnb.csv', index=False)

airbnb_1 = pd.read_csv('airbnb.csv')

airbnb_1

airbnb_1.drop(columns=['address','host','availability','review_scores','amenities','images','reviews','listing_url','summary','first_review','last_review'], inplace=True)

airbnb_1.drop(columns=['interaction',
'cleaning_fee','space','description','neighborhood_overview','notes','transit','house_rules','access','last_scraped','calendar_last_scraped','security_deposit'], inplace=True)

airbnb_1.head(2)

airbnb_1.shape

airbnb_1.columns

airbnb_1.dtypes

airbnb_1.isnull().sum()

airbnb_1['bedrooms'].fillna(airbnb_1['bedrooms'].mean(), inplace=True)

airbnb_1['beds'].fillna(airbnb_1['beds'].mean(), inplace=True)

airbnb_1['bathrooms'].fillna(airbnb_1['bathrooms'].mean(), inplace=True)

airbnb_1.drop(columns=['weekly_price','monthly_price','reviews_per_month'], inplace=True)

airbnb_1.describe()

Q1 = airbnb_1['minimum_nights'].quantile(0.25)
Q3 = airbnb_1['minimum_nights'].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for outlier detection
lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)


print(lower_bound ,upper_bound)

airbnb_1.minimum_nights=airbnb_1.minimum_nights.clip(upper_bound , lower_bound )

Q1 = airbnb_1['maximum_nights'].quantile(0.25)
Q3 = airbnb_1['maximum_nights'].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for outlier detection
lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)


print(lower_bound ,upper_bound)

Q1 = airbnb_1['accommodates'].quantile(0.25)
Q3 = airbnb_1['accommodates'].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for outlier detection
lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)


print(lower_bound ,upper_bound)

airbnb_1.accommodates=airbnb_1.accommodates.clip(upper_bound , lower_bound )

Q1 = airbnb_1['bedrooms'].quantile(0.25)
Q3 = airbnb_1['bedrooms'].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for outlier detection
lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)


print(lower_bound ,upper_bound)

airbnb_1.accommodates=airbnb_1.accommodates.clip(upper_bound , lower_bound )

Q1 = airbnb_1['beds'].quantile(0.25)
Q3 = airbnb_1['beds'].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for outlier detection
lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)


print(lower_bound ,upper_bound)

airbnb_1.beds=airbnb_1.beds.clip(upper_bound , lower_bound )

Q1 = airbnb_1['number_of_reviews'].quantile(0.25)
Q3 = airbnb_1['number_of_reviews'].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for outlier detection
lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)


print(lower_bound ,upper_bound)

Q1 = airbnb_1['bathrooms'].quantile(0.25)
Q3 = airbnb_1['bathrooms'].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for outlier detection
lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)


print(lower_bound ,upper_bound)

airbnb_1.bathrooms=airbnb_1.bathrooms.clip(upper_bound , lower_bound )

airbnb_1.duplicated().sum()

airbnb_1

ab=airbnb_1
ab.head(1)

airbnb_1.to_csv('airbnb_main.csv', index=False)

a = pd.DataFrame(airbnb['address'])
a

a.to_csv('address_duplicate.csv', index=False)

address = pd.read_csv('address_duplicate.csv')
address

airbnb.address[1].keys()

address = pd.DataFrame(a)


address['street'] = address['address'].apply(lambda x: x['street'])
address['suburb'] = address['address'].apply(lambda x: x['suburb'])
address['government_area'] = address['address'].apply(lambda x: x['government_area'])
address['market'] = address['address'].apply(lambda x: x['market'])
address['country'] = address['address'].apply(lambda x: x['country'])
address['country_code'] = address['address'].apply(lambda x: x['country_code'])
address['type'] = address['address'].apply(lambda x: x['location']['type'])
#address['coordinates'] = address['address'].apply(lambda x: x['location']['coordinates'])
address['Latitude'] = address['address'].apply(lambda x: x['location']['coordinates'][1])
address['Longitude'] = address['address'].apply(lambda x: x['location']['coordinates'][0])
address['is_location_exact'] = address['address'].apply(lambda x: x['location']['is_location_exact'])

# Drop the original 'address' column if not needed
address.drop(columns=['address'], inplace=True)

print(address['street'].value_counts())

print(address['suburb'].value_counts())

address.duplicated().sum()

address = pd.DataFrame(address)

address.to_csv('address_duplicate.csv', index=False)

address = pd.read_csv('address_duplicate.csv')
address

df = pd.read_csv('address_duplicate.csv')

# Split the 'street' column by comma and select the first part
#df['street'] = df['street'].str.split(',').str[0]
#df['government_area'] = df['government_area'].str.split(',').str[0]
#df = pd.DataFrame(data)

# Custom function to fill NaN values in 'suburb' using 'market'
def fill_suburb_with_market(row):
    if pd.isna(row['suburb']):
        return row['market']
    else:
        return row['suburb']

# Apply the custom function to fill NaN values in 'suburb' column
df['suburb'] = df.apply(fill_suburb_with_market, axis=1)

missing_values = df.isnull().sum()
#print("Missing Values:")
missing_values

df['market'].fillna(df['market'].mode(), inplace=True)

df['suburb'].fillna(df['suburb'].mode(), inplace=True)

df.drop(columns=['suburb','market'], inplace=True)

missing_values = df.isnull().sum()
#print("Missing Values:")
missing_values

df['street'] = df['street'].str.split(',').str[0]

df['government_area'] = df['government_area'].str.split(',').str[0]

df.describe()

df

#HOST
b = pd.DataFrame(airbnb['host'])
b

host = pd.DataFrame(b)

# Extract 'host_id' and 'host_name' from 'host' dictionary
host['host_id'] = host['host'].apply(lambda x: x['host_id'])
host['host_url'] = host['host'].apply(lambda x: x['host_url'])
host['host_name'] = host['host'].apply(lambda x: x['host_name'])
host['host_location'] = host['host'].apply(lambda x: x['host_location'])
host['host_about'] = host['host'].apply(lambda x: x['host_about'])
host['host_response_time'] = host['host'].apply(lambda x: x.get('host_response_time','null'))
host['host_thumbnail_urlt'] = host['host'].apply(lambda x: x['host_thumbnail_url'])
host['host_picture_url'] = host['host'].apply(lambda x: x['host_picture_url'])
host['host_neighbourhood'] = host['host'].apply(lambda x: x['host_neighbourhood'])
host['host_response_rate'] = host['host'].apply(lambda x: x.get('host_response_rate',0))
host['host_is_superhost'] = host['host'].apply(lambda x: x['host_is_superhost'])
host['host_has_profile_pic'] = host['host'].apply(lambda x: x['host_has_profile_pic'])
host['host_identity_verified'] = host['host'].apply(lambda x: x['host_identity_verified'])
host['host_listings_count'] = host['host'].apply(lambda x: x['host_listings_count'])
host['host_total_listings_count'] = host['host'].apply(lambda x: x['host_total_listings_count'])
#host['host_verifications'] = host['host']['host_verifications'].apply(len)
host['host_verifications'] = host['host'].apply(lambda x: x['host_verifications'])
host['host_verifications'] = host['host_verifications'].apply(len)
# Drop the original 'host' column if not needed
host.drop(columns=['host'], inplace=True)

host['host_response_time'].value_counts()

print(host['host_response_rate'].value_counts())

host.duplicated().sum()

host.drop_duplicates(inplace=True)

host.describe()

Q1 = host['host_response_rate'].quantile(0.25)
Q3 = host['host_response_rate'].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for outlier detection
lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)


print(lower_bound ,upper_bound)

host.host_response_rate = host.host_response_rate.clip(upper_bound , lower_bound )

Q1 = host['host_listings_count'].quantile(0.25)
Q3 = host['host_listings_count'].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for outlier detection
lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

print(lower_bound ,upper_bound)

host.host_listings_count = host.host_listings_count.clip(upper_bound , lower_bound )

Q1 = host['host_total_listings_count'].quantile(0.25)
Q3 = host['host_total_listings_count'].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for outlier detection
lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)


print(lower_bound ,upper_bound)

host.host_total_listings_count = host.host_total_listings_count.clip(upper_bound , lower_bound )

Q1 = host['host_verifications'].quantile(0.25)
Q3 = host['host_verifications'].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for outlier detection
lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)
print(lower_bound ,upper_bound)

host.host_verifications = host.host_verifications.clip(upper_bound , lower_bound )

host

a1=host.to_csv('host_duplicates.csv', index=False)

df_1 = pd.read_csv('host_duplicates.csv')
df_1

df_1.columns

df_1.drop(columns=['host_neighbourhood'], inplace=True)

missing_values = df_1.isnull().sum()
#print("Missing Values:")
print(missing_values)

df_1.drop(columns=['host_response_time'], inplace=True)

df_1['host_location'].fillna(df_1['host_location'].mode(), inplace=True)

df_1.dropna(subset=['host_location'],inplace=True)

missing_values = df_1.isnull().sum()
#print("Missing Values:")
print(missing_values)

df_1

df_1.to_csv('host_main.csv', index=False)

c = pd.DataFrame(airbnb['amenities'])
c

amenities = pd.DataFrame(c)

# Calculate lengths of each 'amenities' list and create a new column
amenities['amenities_length'] = amenities['amenities'].apply(len)

# Print the DataFrame
#print(amenities)
amenities = amenities.drop(columns=['amenities'])
amenities= pd.DataFrame(amenities)
amenities

amenities.to_csv('amenities', index=False)

df_2 = pd.read_csv('amenities')
df_2

d=pd.DataFrame(airbnb['availability'])
d

d['availability'][0]

availability = pd.DataFrame(d)

availability['availability_30'] = availability['availability'].apply(lambda x: x['availability_30'])
availability['availability_60'] = availability['availability'].apply(lambda x: x['availability_60'])
availability['availability_90'] = availability['availability'].apply(lambda x: x['availability_90'])
availability['availability_365'] = availability['availability'].apply(lambda x: x['availability_365'])

availability.drop(columns=['availability'], inplace=True)

availability.isnull().sum()

availability.duplicated().sum()

availability.drop_duplicates(inplace=True)

availability.describe()

Q1 = availability['availability_30'].quantile(0.25)
Q3 = availability['availability_30'].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for outlier detection
lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)


print(lower_bound ,upper_bound)

availability.availability_30 = availability.availability_30.clip(upper_bound , lower_bound )

Q1 = availability['availability_60'].quantile(0.25)
Q3 = availability['availability_60'].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for outlier detection
lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)
print(lower_bound ,upper_bound)

availability.availability_60 = availability.availability_60.clip(upper_bound , lower_bound )

Q1 = availability['availability_90'].quantile(0.25)
Q3 = availability['availability_90'].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for outlier detection
lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)
print(lower_bound ,upper_bound)

availability.availability_90 = availability.availability_90.clip(upper_bound , lower_bound)

Q1 = availability['availability_365'].quantile(0.25)
Q3 = availability['availability_365'].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for outlier detection
lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)
print(lower_bound ,upper_bound)

availability.availability_365 = availability.availability_365.clip(upper_bound , lower_bound )

availability = pd.DataFrame(availability)
availability

df_3=availability.copy()
df_3

missing_values = df_3.isnull().sum()
#print("Missing Values:")
print(missing_values)

e = pd.DataFrame(airbnb['review_scores'])
e

rating = pd.DataFrame(e)

# Extract review scores from nested 'review_scores' dictionary
rating['review_scores_accuracy'] = rating['review_scores'].apply(lambda x: x.get('review_scores_accuracy',0))
rating['review_scores_cleanliness'] = rating['review_scores'].apply(lambda x: x.get('review_scores_cleanliness',0))
rating['review_scores_checkin'] = rating['review_scores'].apply(lambda x: x.get('review_scores_checkin',0))
rating['review_scores_communication'] = rating['review_scores'].apply(lambda x: x.get('review_scores_communication',0))
rating['review_scores_location'] = rating['review_scores'].apply(lambda x: x.get('review_scores_location',0))
rating['review_scores_value'] = rating['review_scores'].apply(lambda x: x.get('review_scores_value',0))
rating['review_scores_rating'] = rating['review_scores'].apply(lambda x: x.get('review_scores_rating',0))

# Drop the original 'review_scores' column if not needed
rating.drop(columns=['review_scores'], inplace=True)

rating.to_csv('rating_dup', index = False)

df_4 = pd.read_csv("rating_dup")
df_4

df_4.isnull().sum()

df_4.duplicated().sum()

df_4.drop_duplicates(inplace=True)

airbnb_1

df #address

df_1  #host

df_2  #amenities

df_3  #availability

df_4  #reviews

airbnb_1

import seaborn as sns
tc=airbnb_1.groupby(['property_type'])['price'].sum().sort_values(ascending=False).nlargest(10).to_frame()

tc=tc.reset_index()
tc

airbnb_data10=pd.concat([airbnb_1,df,df_1,df_2,df_3,df_4],axis=1)

airbnb_data10

airbnb_data10.isnull().sum()

airbnb_data10['host_location'].fillna(airbnb_data10['host_location'].mode(), inplace=True)

airbnb_data10['name'].fillna(airbnb_data10['name'].mode(), inplace=True)

airbnb_data10=airbnb_data10.drop(columns=['host_id','host_is_superhost','host_has_profile_pic','host_identity_verified'],axis=1)

airbnb_data10['host_response_rate'].fillna(airbnb_data10['host_response_rate'].mean(), inplace=True)
#'host_listings_count','host_total_listings_count','host_verifications'

airbnb_data10['host_listings_count'].fillna(airbnb_data10['host_listings_count'].mean(), inplace=True)
airbnb_data10['host_total_listings_count'].fillna(airbnb_data10['host_total_listings_count'].mean(), inplace=True)
airbnb_data10['host_verifications'].fillna(airbnb_data10['host_verifications'].mean(), inplace=True)

airbnb_data10.dropna(subset=['host_name','host_location'],inplace=True)
airbnb_data10.dropna(subset=['name'],inplace=True)

airbnb_data10['availability_365'].fillna(airbnb_data10['availability_365'].mean(), inplace=True)
airbnb_data10=airbnb_data10.drop(columns=['_id'],axis=1)

airbnb_data10=airbnb_data10.drop(columns=['review_scores_accuracy','review_scores_cleanliness','review_scores_checkin','review_scores_communication','review_scores_location','review_scores_value'],axis=1)

airbnb_data10['review_scores_rating'].fillna(airbnb_data10['review_scores_rating'].mean(), inplace=True)

airbnb_data10.isnull().sum()

airbnb_data1=airbnb_data10
airbnb_data1 #/content/sample_data

#airbnb_data = pd.DataFrame(airbnb_data1)

#airbnb_data.to_csv('airbnb_data.csv', index=False)

airbnb_data.duplicated().sum()




