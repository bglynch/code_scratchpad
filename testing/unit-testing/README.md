# Python - Unit Testing

CoreyMS Video: [Unit Testing Your Code with the unittest Module](https://youtu.be/6tNS--WetLI?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)

### Naming
- Files:- convention to start test files with 'test_'  
e.g: test_calc.py  

- Functions:- must start test functions with 'test_'  
e.g: def test_add()  


### Run Tests
add the following to the bottom of the test script
```python
if __name__ == '__main__':
    unittest.main()
``` 
enter
```
$ python3 test_file.py
```
---
Else you can use this command

```
$ python3 -m unittest test_file.py
```