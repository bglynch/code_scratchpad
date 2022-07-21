# Shell Commands

[Advanced Bash-Scripting Guide](https://tldp.org/LDP/abs/html/)

[Baeldung Linux](https://www.baeldung.com/linux/)

## Commands

| Command | Description                                     |
| ------- | ----------------------------------------------- |
| man     |                                                 |
| ls      | List files and dirs                             |
| cat     | View contents                                   |
| less    | View contents in interactive UI                 |
| echo    | Print contents                                  |
| dirname |                                                 |
| history |                                                 |
|         |                                                 |
| mkdir   |                                                 |
| remdir  |                                                 |
| cp      |                                                 |
| mv      |                                                 |
|         |                                                 |
| grep    | **G**lobal **R**egular **E**xpression **P**rint |
| sed     | **S**tream **Ed**itor                           |
| find    |                                                 |
| curl    |                                                 |
| tail    |                                                 |
| wget    |                                                 |



### Curl

```bash
curl https://www.baeldung.com/
```



### Sed

```bash
-E   Interpret regular expressions as extended regular expressions 
-r   Same as -E for compatibility with GNU sed.
-i   replace inplace
# ================================================================
\d does not work for sed, use [0-9] or [[:digit:]]

echo employee_id=1234 


sed -E 's/employee_id=([0-9]+)/\1/g'  # 1234         # extract group
sed 's/employee/emp/'                 # emp_id=1234  # replace employee with emp

# Option if backslashes are hard to read, can use #
echo "/home/example" | sed  's/\/home\/example/\/usr\/local\/example/'
echo "/home/example" | sed 's#/home/example#/usr/local/example#'
```



### Grep 

##### line-by-line search utility

```bash
-i ignore case              -o only matching part of line
-r recursive                -n see line number
-e regex pattern
# ================================================================

echo employee_id=1234 

grep employee           # employee_id=1234
grep -o employee        # employee

#  find all files containing specific text
grep -rnw '/path/to/somewhere/' -e 'pattern'
-r or -R is recursive,
-n is line number, and
-w stands for match the whole word.
-l (lower-case L) can be added to just give the file name of matching files.
-e is the pattern used during the search
--exclude
--include
--exclude-dir

# get files that match the word "test_log_audit_data_success"
grep -rnw src/tests -e test_log_audit_data_success 
# > Binary file src/tests/helpers_tests/__pycache__/test_queue_events.cpython-38-pytest-7.1.2.pyc matches
# > Binary file src/tests/helpers_tests/__pycache__/test_queue_events.cpython-38-pytest-6.2.5.pyc matches
# > src/tests/helpers_tests/test_queue_events.py:145:    def test_log_audit_data_success(
# > src/tests/.pytest_cache/v/cache/nodeids:74:  "helpers_tests/test_queue_events.py::TestQueueEvents::test_log_audit_data_success",
# > src/tests/.pytest_cache/v/cache/lastfailed:2:  "helpers_tests/test_queue_events.py::TestQueueEvents::test_log_audit_data_success": true

# only get .py files
grep -rnw src/tests --include=\*.py -e test_log_audit_data_success   
# > src/tests/helpers_tests/test_queue_events.py:145:    def test_log_audit_data_success(

# get filename only
grep -rwl src/tests --include=\*.py  -e test_log_audit_data_success
# > src/tests/helpers_tests/test_queue_events.py


```

#### Tree

```bash
tree
tree -L 2
```

