# Pandas

### Jupyter Notebook Shortcuts

https://youtu.be/2eCHD6f_phE

https://www.youtube.com/watch?v=HW29067qVWk



## Imports and Exports

### sqlite3: Imports

```python
import sqlite3

conn = sqlite3.connect('database.db')
df = pd.read_sql_query('SELECT * FROM table_name WHERE "County"="Dublin" COLLATE NOCASE', conn)
```

### sqlite3: Exports

##### database - sqlalchemy

```python
from sqlalchemy import create_engine

engine = create_engine('sqlite://', echo=False)
df.to_sql('table_name', con=engine)
```

##### database - sqlite3_new table

```python
import sqlite3

conn = sqlite3.connect('sandbox.db')
cur = conn.cursor()
cur.execute(f"DROP TABLE IF EXISTS construction;")
df.to_sql('construction', conn)
df.to_sql(name='raw_mod', con=conn, index=False) # no index col exported
cur.close()
conn.close()
```

##### database - sqlite3_append

```python
query ='''INSERT OR REPLACE into NewTable (ID,Name,Age) values (?,?,?) '''
conn.executemany(query, df.to_records(index=False))
conn.commit()
```

### csv

##### imports

```python
df = pd.read_csv("filename.csv") 
```

##### export

```python
df.to_csv('try.csv')
```

### geojson

#### import

```python
import geopandas as gpd

fname = "Planning_Application_Sites_2010_onwards.geojson"
df = gpd.read_file(fname)
```



## Create Sample Dataframe

##### python dictionary

```python
data = {
  "Name": ["James", "Alice", "Phil", "James"],
  "Age": [24, 28, 40, 24],
  "Sex": ["Male", "Female", "Male", "Male"]
}
df = pd.DataFrame(data)
print(df)

    Name  Age     Sex
0  James   24    Male
1  Alice   28  Female
2   Phil   40    Male
3  James   24    Male
```

##### python list

```python
lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks']
lst2 = [11, 22, 33, 44, 55, 66, 77]
df = pd.DataFrame(list(zip(lst, lst2)), columns =['Name', 'val'])

     Name  val
0   Geeks   11
1     For   22
2   Geeks   33
3      is   44
4  portal   55
5     for   66
6   Geeks   77


lst = [['tom', 'reacher', 25], ['krish', 'pete', 30],
       ['nick', 'wilson', 26], ['juli', 'williams', 22]]
df = pd.DataFrame(lst, columns =['FName', 'LName', 'Age'], dtype = float)

   FName     LName   Age
0    tom   reacher  25.0
1  krish      pete  30.0
2   nick    wilson  26.0
3   juli  williams  22.0
```



### Display Options

```python
pd.set_option("display.max.columns", None)    # set max columns to be displayed
pd.set_option("display.precision", 2)         # set numeric precision
```



### Explore Dataframe

```python
df.info()          # Summary of the dataframe
len(df)            # length of the data frame
list(df.columns)   # list of columns
df.head()          # top few results
df.dtypes          # show column datatypes
df['Column'].apply(lambda x: print(f"{x}: {type(x)}"))   # print column datatypes

# statistics of dataframe
df.describe()
df.describe(include=np.object)

df["game_location"].nunique()   # number of unique values
df['column'].is_unique          # is column values unique
df['col_name'].unique()         # unique values for a column

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

Dates

```python
dfnew['date_mod'] = pd.to_datetime(dfnew['date'], dayfirst=True, format='%d/%m/%Y')


```





### Columns

##### Change column datatype

```python
df["date"] = pd.to_datetime(df["date"])    # convert to date
df['col'] = df['col'].astype('category')   # convert to category
```

##### Add column

```python
df['new_column'] = None          # To end of the dataframe
df.insert(2, 'new-col', None)    # to a specific position     
  2 = column position
  None = data to insert
```

##### Delete column

```python
# Deleting columns
df = df.drop("Area", axis=1)               # Delete the "Area" column from the 
df = df.drop(columns="area")               # delete using the columns parameter of 
df = df.drop(["col_1","col_2"], axis=1)    # Delete multiple columns from the 
df.drop("Area", axis=1, inplace=True)      # delete inplace

# delete if exists
candidates=["col_1","col_2"]
df = df.drop([x for x in candidates if x in df.columns], axis=1)

# remove rows where column value equals
df.drop(df[df['not_full_market_price']=="yes"].index, inplace=True)
df.drop(["not_full_market_price"], axis=1, inplace=True)

```

##### Rename column

```python
# Rename multiple columns
df.rename(columns={'ExistingName':'NewName', 'ExistingName2':'NewName2'}, inplace=True)
```



### Rows





#### Query Dataframe

```python
df['Product'] == 'Apples'              # product column where Product == Apples
(df.price < 10.0) | (df.price > 65.0)  # dataframe where price > €10 and less than €64
(df['Sale'] > 30) & (df['Sale'] < 33)

# using str.contains
df['Address'].str.contains('dublin ?6$')
~df['Address'].str.contains(r"[&-]")
(df['Address'].str.contains('dublin ?6$')) | (df['Postcode'].str.contains('dublin ?6'))

df['Product'].isin(['Mangos', 'Grapes'])  # 'Product' column contains either 'Grapes' or 'Mangos'
df['Address'].apply(lambda x: bool(re.match(r'.*(dublin 6)',x, re.IGNORECASE))) # using regex
```



#### Filter e.g. get Dublin sales

```python
#Filter pandas dataframe by column value
newdf = df[(df.origin == "JFK") & (df.carrier == "B6")] #Method 1 : DataFrame Way
newdf = df.query('origin == "JFK" & carrier == "B6"') # Method 2 : Query Function
newdf = df.loc[(df.origin == "JFK") & (df.carrier == "B6")] # Method 3 : loc function

newdf = df[df.origin.isin(["JFK", "LGA"])]   #Selecting multiple values of a column
newdf = df.loc[(df.origin != "JFK") & (df.carrier == "B6")] # Select rows whose column value does not equal a specific value
newdf = df[~((df.origin == "JFK") & (df.carrier == "B6"))] # negate the whole condition
newdf = df[df.origin.notnull()] # Select Non-Missing Data in Pandas Dataframe

df[df['var1'].str[0] == 'A']  # Select rows having values starting from letter 'A'
df[df['var1'].str.len()>3]    # Filter rows having string length greater than 3
df[df['var1'].str.contains('A|B')] # Select string containing letters A or B
```



#### Regex

```python
df['first_five_Letter']=df['Country (region)'].str.extract(r'(^w{5})')  # new column with 1st 5 characters of each country
df[df['Country (region)'].str.match('^P.*')== True]                     # countries starting with P
df[df['Country (region)'].str.count('^[pP].*')>0]												# countries starting with P or p
df[df['Country (region)'].str.contains('^I.*')==True]

df_updated = df.replace(to_replace ='[nN]ew', value = 'New_', regex = True)
df['New'].replace('(-\d)','',regex=True, inplace = True)

def regex_replace(string):
    string = re.sub(r'regex', '', string)
    return string
df['br_address'] = df['br_address'].apply(regex_replace)
```



##### duplicates  

[**duplicated**(subset=None,keep='first')](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html)              : Return boolean Series denoting duplicate rows

[**drop_duplicates**(subset=None, keep='first' , inplace=False , ignore_index=False)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html)    : Return DataFrame with duplicate rows removed.

```python
dup_df = df.duplicated(['street', 'area'])    # dataframe of duplicates of street and area combined
df = df.drop_duplicates() # remove duplicates
df = df.sort_values('Age', ascending=False)           # sort values before removing duplicates
df = df.drop_duplicates(subset='Name', keep='first')  # remove duplicates based on Name column, and keeping the first one
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



##### Remove rows

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





#### GIS Data - Json to GeoJson

imports

```python
import geopandas as gpd
import json
import os
```

load json

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



---

## Some solved problems

### find most common placenames at the end of addresses

```python
import collections
import re

no_loc = df[df['locality'].apply(lambda x: x==None)]
end_of_address_places = no_loc.address.apply(lambda x: re.sub(r'^.+, (\w+)$', r'\1', x))
group_places = end_of_address_places.value_counts()

# placenames that appear more than 10 times
my_dict = group_places.to_dict()

# remove place that appear less than 10 time
for k, v in my_dict.copy().items():
    if v < 10:
        del my_dict[k]

# sorted by placename
collections.OrderedDict(sorted(my_dict.items()))
```



[PYTHON : 10 WAYS TO FILTER PANDAS DATAFRAME](https://www.listendata.com/2019/07/how-to-filter-pandas-dataframe.html)

[How to use Regex in Pandas](https://kanoki.org/2019/11/12/how-to-use-regex-in-pandas/)