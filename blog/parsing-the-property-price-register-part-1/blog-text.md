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

Eircodes are quite structured, so there should'nt be a need to normalise the address before extraction.

Threre are 139 eircode routing keys, so we will look for one of these plus 4 succeeding alphanumeric characters.

Eircode routing keys can be found here: https://www.autoaddress.ie/blog/autoaddressblog/2016/09/21/eircode-routing-keys

#### Create funciton for extracting Eircode from end of address

##### tests

```python
def test_extract_eircode(self):
  self.assertEqual(ex.extract_eircode_from_end_of_address('1 Some Place, K67 KR86'), "K67 KR86")
  self.assertEqual(ex.extract_eircode_from_end_of_address('1 Some Place K67 KR86'), "K67 KR86")
  self.assertEqual(ex.extract_eircode_from_end_of_address('1 Some Place, K67KR86'), "K67 KR86")
```

##### function

```python
def extract_eircode_from_end_of_address(address: str):
    address = address.lower().strip(' ,.')
    eircode_routing_keys = [
        'a41', 'a42', 'a45', 'a63', 'a67', 'a75', 'a81', 'a82', 'a83', 'a84', 'a85', 'a86', 'a91', 'a92', 'a94', 'a96',
        'a98', 'c15', 'd01', 'd02', 'd03', 'd04', 'd05', 'd06', 'd6w', 'd07', 'd08', 'd09', 'd10', 'd11', 'd12', 'd13',
        'd14', 'd15', 'd16', 'd17', 'd18', 'd20', 'd22', 'd24', 'e21', 'e25', 'e32', 'e34', 'e41', 'e45', 'e53', 'e91',
        'f12', 'f23', 'f26', 'f28', 'f31', 'f35', 'f42', 'f45', 'f52', 'f56', 'f91', 'f92', 'f93', 'f94', 'h12', 'h14',
        'h16', 'h18', 'h23', 'h53', 'h54', 'h62', 'h65', 'h71', 'h91', 'k32', 'k34', 'k36', 'k45', 'k56', 'k67', 'k78',
        'n37', 'n39', 'n41', 'n91', 'p12', 'p14', 'p17', 'p24', 'p25', 'p31', 'p32', 'p36', 'p43', 'p47', 'p51', 'p56',
        'p61', 'p67', 'p72', 'p75', 'p81', 'p85', 'r14', 'r21', 'r32', 'r35', 'r42', 'r45', 'r51', 'r56', 'r93', 'r95',
        't12', 't23', 't34', 't45', 't56', 'v14', 'v15', 'v23', 'v31', 'v35', 'v42', 'v92', 'v93', 'v94', 'v95', 'w12',
        'w23', 'w34', 'w91', 'x35', 'x42', 'x91', 'y14', 'y21', 'y25', 'y34', 'y35'
    ]
    regex = r"\b(" + '|'.join(eircode_routing_keys) + r") ?([a-z0-9]{4})$"
    regex_result = re.search(regex, address)
    eircode = None
    if regex_result is not None:
        eircode = f"{regex_result.group(1)} {regex_result.group(2)}".upper()
    return eircode
```

Now we can sucessfully extract an Eircode from an address



#### Create a funciton to remove an Eircode from an address

##### tests

```python
def test_parse_address_of_eircode(self):
  self.assertEqual(pr.parse_address_of_eircode('1 Some Place, K67 KR86'), "1 Some Place")
  self.assertEqual(pr.parse_address_of_eircode('1 Some Place K67 KR86'), "1 Some Place")
  self.assertEqual(pr.parse_address_of_eircode('1 Some Place, K67KR86'), "1 Some Place")
```

##### function

```python
def parse_address_of_eircode(address: str):
    address = address.strip(' ,.')
    eircode_routing_keys = [
        'a41', 'a42', 'a45', 'a63', 'a67', 'a75', 'a81', 'a82', 'a83', 'a84', 'a85', 'a86', 'a91', 'a92', 'a94', 'a96',
        'a98', 'c15', 'd01', 'd02', 'd03', 'd04', 'd05', 'd06', 'd6w', 'd07', 'd08', 'd09', 'd10', 'd11', 'd12', 'd13',
        'd14', 'd15', 'd16', 'd17', 'd18', 'd20', 'd22', 'd24', 'e21', 'e25', 'e32', 'e34', 'e41', 'e45', 'e53', 'e91',
        'f12', 'f23', 'f26', 'f28', 'f31', 'f35', 'f42', 'f45', 'f52', 'f56', 'f91', 'f92', 'f93', 'f94', 'h12', 'h14',
        'h16', 'h18', 'h23', 'h53', 'h54', 'h62', 'h65', 'h71', 'h91', 'k32', 'k34', 'k36', 'k45', 'k56', 'k67', 'k78',
        'n37', 'n39', 'n41', 'n91', 'p12', 'p14', 'p17', 'p24', 'p25', 'p31', 'p32', 'p36', 'p43', 'p47', 'p51', 'p56',
        'p61', 'p67', 'p72', 'p75', 'p81', 'p85', 'r14', 'r21', 'r32', 'r35', 'r42', 'r45', 'r51', 'r56', 'r93', 'r95',
        't12', 't23', 't34', 't45', 't56', 'v14', 'v15', 'v23', 'v31', 'v35', 'v42', 'v92', 'v93', 'v94', 'v95', 'w12',
        'w23', 'w34', 'w91', 'x35', 'x42', 'x91', 'y14', 'y21', 'y25', 'y34', 'y35'
    ]
    regex = r"\b(" + '|'.join(eircode_routing_keys) + r") ?[a-z0-9]{4}$"
    address = re.sub(regex, '', address, flags=re.IGNORECASE).rstrip(', ')

    return address
```

Now we can sucessfully remove an Eircode from an address



#### Extract Eircode

Now we will loop over the database and extract/remove eircode from address containing them

```python
conn = sqlite3.connect('../data/database.db')
df = pd.read_sql_query('SELECT * FROM temp;', conn)
df.set_index('uuid', inplace=True)

for row in df.copy().itertuples():
    eircode = ex.extract_eircode_from_end_of_address(row.address_mod)
    if eircode is not None:
        df.at[row.Index, 'ex_eircode'] = eircode
        df.at[row.Index, 'address_mod'] = pr.parse_address_of_eircode(row.address_mod)

cur = conn.cursor()
cur.execute(f"DROP TABLE IF EXISTS temp;")
df.to_sql('temp', conn)
cur.close()
conn.close()
```

![image-20210426105039237](/Users/br20069521/Library/Application Support/typora-user-images/image-20210426105039237.png)

Now after opening the db with DB Browser for Sqlite, we can see we have sucessfully extracted 35 eircode. 

Considering Eircodes were introduced in July 2015, which accounts for over half of the rows in the database, this is a disapointing return.

Its is approximatly 0.0001% of address.



---



### Extract County

County naming is not as structured as eircodes, so we will need to normalise county naming formatting before extracting.

Threre are 26 countiess, so we will look for one of these surrounded by an longhand/shorthand naming of county..



##### Normalise function (e.g. 1 Some Place, co cork => 1 Some Place, co_cork )

From scanning through the database, we have extracted some tests for our normalisation function.
We are attempting to normalise county to **co_{county_name}**

##### tests

```python
def test_parse_address_of_eircode(self):
  self.assertEqual(nm.normalise_county_name('1 Some Place, co cork'),    "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place, co. cork'),   "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place, co.cork'),    "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place co cork'),     "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place  co cork'),    "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place county cork'), "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place countycork'),  "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place  cork'),       "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place  cork.'),      "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place, cork'),       "1 some place, co_cork")
```

##### function

```python
def normalise_county_name(address: str):
    counties = ['carlow', 'cavan', 'clare', 'cork', 'donegal', 'down', 'dublin', 'fermanagh', 'galway', 'kerry',
                'kildare', 'kilkenny', 'laois', 'leitrim', 'limerick', 'longford', 'louth', 'mayo', 'meath', 'monaghan',
                'offaly', 'roscommon', 'sligo', 'tipperary', 'waterford', 'westmeath', 'wexford', 'wicklow']
    address = address.lower().strip(' ,.')
    counties_regex = r"(" + '|'.join(counties) + r")"
    address = re.sub(r"[ ,]+(county|co\.|co) *\.?" + counties_regex, r", co_\2", address)
    address = re.sub(r"[ ,]" + counties_regex + r" ?(county|co\.|co)\b", r", co_\1", address)
    address = re.sub(r"  +" + counties_regex + r"$", r", co_\1", address)
    address = re.sub(r", ?" + counties_regex + r"$", r", co_\1", address)

    return address
```

We run this function through or database to see how many address were normalised and search for outliers that aren't replresented in our tests.

```python
conn = sqlite3.connect('data/database.db')
df = pd.read_sql_query('SELECT * FROM temp;', conn)
df.set_index('uuid', inplace=True)

df.address_mod = df.address_mod.apply(nm.normalise_county_name)

cur = conn.cursor()
cur.execute(f"DROP TABLE IF EXISTS temp;")
df.to_sql('temp', conn)
cur.close()
conn.close()
```



![image-20210426121342089](/Users/br20069521/Library/Application Support/typora-user-images/image-20210426121342089.png)

Looking at the database, we can see that 162,353 rows have been normalised. This is 34.65% of rows which is a very good return.

Now we will look for outliers.

DB Browser for Sqlite allows for regex seaching which is extremely useful for this.

###### Search for County in address

![image-20210426121830279](/Users/br20069521/Library/Application Support/typora-user-images/image-20210426121830279.png)

###### Seach for county names at the end of the address preceeded by a space

![image-20210426122635022](/Users/br20069521/Library/Application Support/typora-user-images/image-20210426122635022.png)

Between, these two searches, we have found almost 1,000 outliers. We will add some of these to our tests to try impove the normalise function

#####  tests

```python
def test_parse_address_of_eircode(self):
  self.assertEqual(nm.normalise_county_name('1 Some Place, co cork'),    "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place, co. cork'),   "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place, co.cork'),    "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place co cork'),     "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place  co cork'),    "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place county cork'), "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place countycork'),  "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place  cork'),       "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place  cork.'),      "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place, cork'),       "1 some place, co_cork")
  # part of a county
  self.assertEqual(nm.normalise_county_name('1 Some Place, west cork'),        "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place, nr cork'),          "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place, near cork'),        "1 some place, co_cork")  
  self.assertEqual(nm.normalise_county_name('1 Some Place, north dublin'),     "1 some place, co_dublin")
  self.assertEqual(nm.normalise_county_name('1 Some Place, north tipperary'),  "1 some place, co_tipperary")
  self.assertEqual(nm.normalise_county_name('1 Some Place, south tipperary'),  "1 some place, co_tipperary")
  self.assertEqual(nm.normalise_county_name('1 Some Place, west cork'),        "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place, west cork'),        "1 some place, co_cork")
  # county misspelling
  self.assertEqual(nm.normalise_county_name('1 Some Place, ci cork'),        "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place, cp cork'),        "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place, clo cork'),        "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place, col cork'),        "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place, ci cork'),        "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place, ci cork'),        "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place, c cork'),        "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place, c0. cork'),        "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place, cco. cork'),        "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place, o cork'),        "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place, cointy cork'),        "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place, ccunty cork'),        "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place, cunty cork'),        "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place, cointy cork'),        "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place, couty cork'),        "1 some place, co_cork")
  self.assertEqual(nm.normalise_county_name('1 Some Place, couny cork'),        "1 some place, co_cork")
  
  
  
```

##### function

```python
def normalise_county_name(address: str):
    counties = ['carlow', 'cavan', 'clare', 'cork', 'donegal', 'down', 'dublin', 'fermanagh', 'galway', 'kerry',
                'kildare', 'kilkenny', 'laois', 'leitrim', 'limerick', 'longford', 'louth', 'mayo', 'meath', 'monaghan',
                'offaly', 'roscommon', 'sligo', 'tipperary', 'waterford', 'westmeath', 'wexford', 'wicklow']
    address = address.lower().strip(' ,.')
    counties_regex = r"(" + '|'.join(counties) + r")"
    address = re.sub(r"[ ,]+(county|co\.|co) *\.?" + counties_regex, r", co_\2", address)
    address = re.sub(r"[ ,]" + counties_regex + r" ?(county|co\.|co)\b", r", co_\1", address)
    address = re.sub(r"  +" + counties_regex + r"$", r", co_\1", address)
    address = re.sub(r", ?" + counties_regex + r"$", r", co_\1", address)

    return address
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

