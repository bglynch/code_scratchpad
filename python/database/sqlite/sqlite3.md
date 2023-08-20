# sqlite3 - python

### Links

[https://docs.python.org/3/library/sqlite3.html](https://docs.python.org/3/library/sqlite3.html)



### Import

No need to install, sqlite3 is part of the default python packages

```python
import sqlite3
```



#### Typical Flow 

```python
conn = sqlite3.connect('database.db')     # create connection to database
cur = conn.cursor()                       # create cursor
cur.execute('''SQL COMMAND''')            # execute sql command with cursor
conn.commit()          										# commit the changes
c.close()          										    # close the cursor
conn.close()          										# close the connection
```



### Memory Database

> ```python
> conn = sqlite3.connect(':memory:') 
> ```
>

### Use connecition as context manager

> This removes the necissity to use the commit() command
>
> ```python
> with conn:
>   c.execute("INSERT INTO table VALUES (?,?,?)", (variable1, var2, var3)) 
> ```
>

### SELECT

> ```sqlite
> cur.execute('''SELECT * FROM table WHERE column="string"''').fetchall()
> 
> cur.fetchone()    # get the first result
> cur.fetchall()    # get a list of results
> ```

### INSERT

> ```sqlite
> cur.execute("INSERT INTO table VALUES (?,?,?)", (variable1, var2, var3)) 
> cur.execute("INSERT INTO table(col1, col2, col3) VALUES (?,?,?)", (variable1, var2, var3)) 
> 
> cur.commit()
> ```

### UPDATE

> https://www.sqlitetutorial.net/sqlite-update/
>
> ```sqlite
> cur.execute('''UPDATE table_name SET col1=? WHERE col2=?''', ('val1', 'val2'))
> cur.execute('''UPDATE table_name 
> 								SET col1=?, col2=? 
> 								WHERE col3=?''', ('val1', 'val2', 'val3'))
> ```
>
> ##### update with counter
>
> ```python
> # print 
> table = 'origional_mod'
> update_statement = f'''UPDATE {table} SET dummy=? WHERE uuid=?'''
> with conn:
>     counter, multiplier, step = 0,1,100
>     for row in db_rows:
>       	update_payload = ('test', row[-3])
>         cur.execute(update_statement, update_payload)
>         counter+=1
>         if counter == step:
>             print(f"{counter*multiplier} rows updates")
>             counter = 0
>             multiplier +=1
> ```
>



---



**todo**

- test update speed of differernt methods of sqlite
- https://www.programmersought.com/article/52904969389/
- https://stackoverflow.com/questions/24375531/make-sqlite3-column-update-faster
- https://stackoverflow.com/questions/38208224/sqlite3-slow-update
