## Parsing the Price Property Register Part 01: 

## Normalising and Extracting address Eircode, County and Postcode



### Preface

Anyone who has attempted to work with the data from Ireland's Price Property Register will know that the dataset is not very clean. It's very dirty in places. In this blog we will attempt to make it a bit less dirty. We will extract structured data from the address.

Currently the dataset has approximatly 450,000 rows. The columns in the dataset are:

- Date of Sale
- Address
- Postal Code
- County
- Price
- Not Full Market Price
- VAT Exclusive
- Property Size Description
- Description of Property

The ones we are interested in are **Address**, **Postal Code** and **County**.

In many rows in the dataset, the Address can contain County information Postal Code information........ or both!



### Aim

Our aim is to remove this information from the address and update the Postal Code or County information where necessary.

##### Examples

| Address                                       | Cleaned Data                                                 |
| --------------------------------------------- | ------------------------------------------------------------ |
| 1 MEADOW AVENUE, DUNDRUM, DUBLIN 14           | **address** = 1 Meadow Avenue, Dundrum <br />**postcode**=Dublin 14 |
| 44 ALLEN PARK ROAD, STILLORGAN, COUNTY DUBLIN | **address** = 44 Allen Park Road, Stillorgan <br />**county** = Dublin |
| 1 INFIRMARY RD, DUBLIN 7, DUBLIN              | **address** = 1 Infirmary rd<br />**postcode** = Dublin 7<br />**county** = Dublin |



### Tools for the job

- python
- pandas
- regex
- sqlite3
- Jupyter Notebooks
- DB Browser for sqlite



### Method

#### Data preperation

PPR data is attained as a csv file. Pandas will be used to load the data, modify the column names and create a uuid for each row. Then this will be exported to a sqlite database after setting the index to uuid.



#### Address cleaning

First we will normalise the eircode, county and postal code substrings in each address. Each will be normalised to an easily extractable pattern.

Testing will be used to create the normalisation and extraction functions



---

### Prepare the Data

Data can be downloaded here: https://propertypriceregister.ie/Website/NPSRA/pprweb.nsf/page/ppr-home-en

We will use pandas to prepare the data and save it to a sqlite database

```python
import sqlite3
import pandas as pd
from hashlib import blake2b

# load data
df = pd.read_csv("../data/raw/PPR-ALL.csv", encoding='latin-1')
# rename columns
df = df.rename(columns={
    'Date of Sale (dd/mm/yyyy)': 'date',
    'Address': 'address',
    'Postal Code': 'postcode',
    'County': 'county',
    'Price (\x80)': 'price',
    'Not Full Market Price': 'not_full_market_price',
    'VAT Exclusive': 'vat_exclusive',
    'Property Size Description': 'floor_area',
    'Description of Property': 'construction',
})

# create uuid for each row
for row in df.copy().itertuples():
    hash_id_string = f"{row.date}{row.address}{row.postcode}{row.county}{row.price}{row.not_full_market_price}{row.vat_exclusive}{row.floor_area}{row.construction}"
    df.at[row.Index, 'uuid'] = blake2b(bytes(hash_id_string, "utf-8"), digest_size=5).hexdigest()

# remove duplicates
df.drop_duplicates(inplace=True)

# set index to 'uuid'
df.set_index('uuid', inplace=True)

db_url = "../data/database.db"
conn = sqlite3.connect(db_url)
cur = conn.cursor()
df.to_sql('ppr_all', conn)
cur.close()
conn.close()
```

Now we have the PPR data is a sqlite database.

![image-20210425104203993](/Users/br20069521/Library/Application Support/typora-user-images/image-20210425104203993.png)



---

#### Create tempoary data table

We will create a temporary table to iterate over while we are creating the functions to normalise and extract data.

To do this, we will again use pandas.

```python
conn = sqlite3.connect('../data/database.db')
df = pd.read_sql_query('SELECT * FROM ppr_all', conn)
df.set_index('uuid', inplace=True)

df = df.drop(["date","price","not_full_market_price","construction","floor_area","vat_exclusive"], axis=1)
df.insert(3, 'ex_eircode', None)
df.insert(3, 'ex_county', None)
df.insert(3, 'ex_postcode', None)
df.insert(3, 'address_mod', None)
df.address


cur = conn.cursor()
cur.execute(f"DROP TABLE IF EXISTS temp;")
df.to_sql('temp', conn)
cur.close()
conn.close()
```



![image-20210425110822447](/Users/br20069521/Library/Application Support/typora-user-images/image-20210425110822447.png)



---



### Extract Eircode

Eircodes are quite structured, so there shouldnt be a need to normalise the address before extraction.

Threre are 139 eircode routing keys, so we will look for one of these plus 4 succeeding alphanumeric characters.

Eircode routing keys can be found here: https://www.autoaddress.ie/blog/autoaddressblog/2016/09/21/eircode-routing-keys

```python

```



#### Useful PPR Links





Load the register into the 

- create uuid
- extract uuid, address, postcode, county
- create new columns: address_mod, ext_eircode, ext_postcode, ext_county
- extract eircode
- normalise county 
- extract countyhe
- normalise dublin postcode
- extact dublin postcode
- compare dublin postcode
- compare county
- remove dublin postcode when extracted county == county

