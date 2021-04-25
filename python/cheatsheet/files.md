# Files and Directories

#### os module

```python
import os

os.environ							         # list of environmental vars
os.getenv('name')                # get environmental var
os.getcwd()                      # get name of current directory
os.listdir(path='.')             # get list of directories
os.stat('file.txt').st_size      # get file size
next(os.walk(os.getcwd()))[2]    # get all files in dir
[f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))] # get all files in dir

os.chdir('../')          # change to parent directory
os.chdir(os.pardir)			 # change to parent directory
os.mkdir('path')         # create directory
os.makedirs('new/path')  # create new directory and subdirectories
os.rename('old', 'new')  # rename file

os.remove('file_path')   # delete file
os.rmdir('path')         # delete empty directory

os.path.isfile('path')   # 
os.path.isdir('path')

os.path.getsize('path')  # get file size
os.stat('path').st_size  # get file size
```



#### pathlib - Object-oriented filesystem paths

```python
from pathlib import Path

p = Path(os.getcwd())	                   # create path object

p								                         # current dir
p.parent				                         # get parent dir
p.parent.name                            # get parent dir name
[x for x in p.iterdir()]                 # list of files and sub dirs
[x for x in p.iterdir() if x.is_dir()]   # list of sub dirs
```

