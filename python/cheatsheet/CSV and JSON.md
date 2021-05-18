# CSV and JSON

## CSV

```python
import csv
```



### Reading files

#### csv.reader

```
name,department,birthday month
John Smith,Accounting,November
Erica Meyers,IT,March
```

```python
# read using csv.reader
with open('employee_birthday.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count ==0:
            print(f'Column names are \n\t{",".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}')
            line_count += 1
    print(f'Processed {line_count} lines.')
    

Column names are 
	name,department,birthday month
	John Smith works in the Accounting department, and was born in November
	Erica Meyers works in the IT department, and was born in March
Processed 3 lines.
```

#### csv.DictReader

```
name,department,birthday month
John Smith,Accounting,November
Erica Meyers,IT,March
```

```python
with open('employee_birthday.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count ==0:
            print(f'Column names are \n\t{",".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}')
        line_count += 1
    print(f'Processed {line_count} lines.')

Column names are 
	name,department,birthday month
	John Smith works in the Accounting department, and was born in November
	Erica Meyers works in the IT department, and was born in March
Processed 3 lines.    
```

#### different delimeter

```
name|address|date joined
John Smith|1234 Somewhere, Cork|Jan 01
Erica Meyers|5678 Elsewhere, Dublin|Feb 02
```

```python
with open('different_delim.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='|')
    line_count = 0
    for row in csv_reader:
        if line_count ==0:
            print(f'Column names are \n\t{",".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}')
            line_count += 1
    print(f'Processed {line_count} lines.')

Column names are 
	name,address,date joined
	John Smith works in the 1234 Somewhere, Cork department, and was born in Jan 01
	Erica Meyers works in the 5678 Elsewhere, Dublin department, and was born in Feb 02
Processed 3 lines.
```



```
name,address,date joined
John Smith,"1234 Somewhere, Cork",Jan 01
Erica Meyers,"5678 Elsewhere, Dublin",Feb 02
```

```python
with open('quote_wrapping.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    line_count = 0
    for row in csv_reader:
        if line_count ==0:
            print(f'Column names are \n\t{",".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}')
            line_count += 1
    print(f'Processed {line_count} lines.')
```



Useful article on encoding errors

https://stackoverflow.com/questions/21504319/python-3-csv-file-giving-unicodedecodeerror-utf-8-codec-cant-decode-byte-err

https://docs.python.org/3/library/codecs.html#standard-encodings

```
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x80 in position 60: invalid start byte
```





### Writing files

#### csv.writer

```python
with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Veb Smite', 'IT', 'March'])
```

#### csv.DictWriter

```python
with open('employee_file_dict.csv', mode='w') as employee_file:
    fieldnames = ['name', 'dept', 'birth_month']
    employee_writer = csv.DictWriter(employee_file, fieldnames=fieldnames)
    
    employee_writer.writeheader()
    employee_writer.writerow({'name':'John Smith', 'dept':'Accounting', 'birth_month':'November'})
    employee_writer.writerow({'name':'Veb Smite', 'dept':'IT', 'birth_month':'March'})
```
