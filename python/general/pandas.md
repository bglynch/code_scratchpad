# Pandas

### Imports

```python
%matplotlib inline

import pandas as pd
import matplotlib.pyplot as plt
import numpy as mp
import re
```



### Imports

sqlite3

```python
import sqlite3

cnx = sqlite3.connect('pprALL.db')
df = pd.read_sql_query('SELECT * FROM soldProperties WHERE "County"="Dublin" COLLATE NOCASE', cnx)
```

csv

```python
df = pd.read_csv("filename.csv") 
```

geojson

```python
import geopandas as gpd

fname = "Planning_Application_Sites_2010_onwards.geojson"
df = gpd.read_file(fname)
```



### Explore Dataframe

Display options

```python
# set max columns to be displayed
pd.set_option("display.max.columns", None)

# set numeric precision
pd.set_option("display.precision", 2)
```



```python
# Summary of the dataframe
df.info()

# length of the data frame
len(df)

# top few results
df.head()

# statistics of dataframe
df.describe()
df.describe(include=np.object)

# number of unique values
df["game_location"].nunique()

# is column values unique
df['column'].is_unique

# list of columns
list(df.columns)

# unique values for a column
df['col_name'].unique()


# show column datatypes
df.dtypes

# print column datatypes
df['Column'].apply(lambda x: print(f"{x}: {type(x)}"))

# number of unique value for each column
for column in list(rathmines_df.columns):
    print(column)
    print(f"  unique: {len(rathmines_df[column].unique())}")
    if(len(rathmines_df[column].unique())) < 10:
        print(f"  {rathmines_df[column].unique()}")
    print("")
```

Get value from column

```python
df[df['colum01'] == 'value']['column02'].values[0]
```



### Columns

Change column datatype

```python
# convert to date
df["date_game"]    = pd.to_datetime(df["date_game"])
df['construction'] = df['construction'].astype('category')
```

Add column

```python
# To end of the dataframe
df['new_column'] = None

# to a specific position
df.insert(2, 'new-col', None)         2 = column position
                                   None = data to insert
```

Delete column

```python
# Deleting columns
df = df.drop("Area", axis=1)   # Delete the "Area" column from the dataframe

# alternatively, delete columns using the columns parameter of drop
df = df.drop(columns="area")

# Delete the Area column from the dataframe in place
# Note that the original 'data' object is changed when inplace=True
df.drop("Area", axis=1, inplace=True) 

# Delete multiple columns from the dataframe
df = df.drop(["Y2001", "Y2002", "Y2003"], axis=1)

# remove rows where column value equals
df.drop(df[df['not_full_market_price']=="yes"].index, inplace=True)
df.drop(["not_full_market_price"], axis=1, inplace=True)

```

Rename column

```python
# Rename multiple columns
df.rename(columns={'ExistingName':'NewName', 'ExistingName2':'NewName2'}, inplace=True)
```



#### Query Dataframe

```python
# product column where Product == Apples
df['Product'] == 'Apples'


# dataframe where price > €100,000 and less than €6,500,000
(df.price < 100000.0) | (df.price > 6500000.0)
(df['Sale'] > 30) & (df['Sale'] < 33)


# 
df['Address'].str.contains('dublin ?6$')
~df['Address'].str.contains(r"[&-]")
(df['Address'].str.contains('dublin ?6$')) | (df['Postcode'].str.contains('dublin ?6'))

# dataframe of duplicates of street and area combined
df.duplicated(['street', 'area'])

# dataframe of duplicates of street and area combined
df['Product'].isin(['Mangos', 'Grapes'])

# Select rows for which 'Product' column contains either 'Grapes' or 'Mangos'
df['Address'].apply(lambda x: bool(re.match(r'.*(dublin 6)',x, re.IGNORECASE)))
```



#### Edit data in column

```python
dub_addresses = df['Address'][df['Address'].str.contains('dublin', flags=re.IGNORECASE, regex=True)].values
Dub_multisale = df[df['prop_type'].str.contains('multi', na=False)]

# remove dublin reference from end of string
df["Address"] = df["Address"].apply(mc.remove_dublin)
df["Address"] = df["Address"].apply(mc.removeDoubleSpaces)

# modify with regex
df['Address'] = df['Address'].str.replace(r' (&|-|/) ', r'\g<1>')
df['Address'] = df['Address'].str.replace(r'(\d) and (\d)', r'\g<1>&\g<2>')
df['Address'] = df['Address'].str.replace(r'(apartment)(\d{1,3}[a-z]?,)', r'\1 \2')

# reindex the dataset
df_singlesale = df_singlesale.reset_index()

# change case
df['br_address'] = df['Address'].str.lower()

# set default values for Null
df["column"].fillna(value="default value",inplace=True)


df['col1']=( df.col1.str.split()
              .apply(lambda x: ', '.join(x[::-1]).rstrip(','))
              .where(df['col1'].str.contains(','),df['col1']) 
              .str.replace(',','') )



dfmin['reverse']  = dfmin['_address'].apply(lambda x:x[::-1].replace(".","").replace(",","").replace(" ",""))



# map housetype to an int
df['house_type_id'] = df.house_type.map({'house':1, 'apartment':2, 'duplex':3, 'bungalow':4, 'site':5})

```

Looping over dataframe

```python
# loop over dataframe
for index, row in df.iterrows():
    print(row['c1'], row['c2'])

# iterate over the dataframe row by row and update value
for index_label, row_series in df.iterrows():
   # For each row update the 'Bonus' value to it's double
   df.at[index_label , 'Column'] = row_series['Column'] * 2

for row in df.itertuples(): 
    df.at[row.Index, 'Address'] = pl.normalize_apartment_address(row.Address)


Looping checks
-------------------
pd.isnull(postcode)
pd.notnull(postcode

```

Remove rows

```python
# ================= Option 01: reindex to a column and remove using list
# get list of manual duplicates
conn = sql.connect('data/utility/manual_changes.db')
c = conn.cursor()
duplicates = [x[0] for x in c.execute(f"SELECT id from duplicates;").fetchall()]
c.close()
conn.close()

df.set_index('id', inplace=True)
df.drop(duplicates, inplace=True)

# =================== Option 02 create dataframe with rows to be removes
# get list of multisales
conn = sql.connect('sandbox/sandbox.db')
c = conn.cursor()
issues = {x[0] for x in c.execute(f"SELECT id from issues;").fetchall()}
c.close()
conn.close()
#create df of row id's to be deleted
issues_df = pd.DataFrame(issues, columns=['id'])

# remove multisales
df = df[~df['id'].isin(issues_df['id'])]

```



#### Apply function to dataframe

```python
def reverse_address(string):
    address = string.split(', ')
    address.reverse()
    reversed_address = ", ".join(address)
    return reversed_address


# no need to put the variable in the apply function
test['br_address'] = test['br_address'].apply(reverse_address)
```



#### Grouping

```python
group_by_county = df.groupby('county')
```



#### Combining dataframe

Same columns

```python
pd.concat([df1, df2]).sort_values(['address'])
```



#### Export dataframe

csv

```python
df_singlesale.to_csv('try.csv')
```

database

```python
from sqlalchemy import create_engine

engine = create_engine('sqlite://', echo=False)
df.to_sql('table_name', con=engine)

------

import sqlite3 as sql

conn = sql.connect('sandbox.db')
c = conn.cursor()
c.execute(f"DROP TABLE IF EXISTS construction;")
dfmin.to_sql('construction', conn)
c.close()
conn.close()
```



#### GIS Data - Json to GeoJson

imports

```python
import geopandas as gpd
import json
import os
```

load son

```python
file = "location-of-file"

with open(file) as f:
  data = json.load(f)
```

json to geojson

```python
geojson = {
    "type": "FeatureCollection",
    "features": [
    {
        "type": "Feature",
        "geometry" : {
            "type": "Point",
            "coordinates": [d["Longitude"], d["Latitude"]],
            },
        "properties" : d,
     } for d in data]
}

for g in geojson['features']:
    del g['properties']['Longitude']
    del g['properties']['Latitude']
```

geopandas df

```python
df = gpd.GeoDataFrame.from_features(geojson["features"])
```

write to geojson

```python
df.to_file("countries.geojson", driver='GeoJSON')
```

