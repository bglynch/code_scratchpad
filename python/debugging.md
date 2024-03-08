# Debugging

## Option 1: Print statements

> Quick and easy but not interactive
>
> ```python
> print(f'something here')
> 
> # Add color
> # Colors
> RED='\033[31m'
> GRN='\033[32m'
> YLW='\033[33m'
> BLU='\033[36m'
> RST='\033[0m'
> 
> import inspect
> print('')
> print(f"{GRN}file_name {BLU}{inspect.stack()[0].filename}{RST}")
> print(f"{GRN}function  {BLU}{inspect.stack()[0].function}{RST}")
> 
> print(f"{GRN}file_name {BLU}try safe_authenticate{RST}")
> print(f"  {YLW}variable: {RST}{var}")
> print(f"  {GRN}file_name. {BLU} check 3")
> ```
>



## Option 2: IPython `embed()` session

> ###### Benefits
>
> - Interactive Ipython session
> - All modifications will persist when closed
>
> ###### Shortcommings
>
> - Cant execute following lines of code like a typical debugger
>
> Documentation: [Embedding IPython](https://ipython.readthedocs.io/en/stable/interactive/reference.html#embedding-ipython)
>
> ```bash
> pip install ipython
> ```
>
> ###### Add the following line(s) to code
>
> ```python
> # basic
> from IPython import embed; embed()
> 
> # fix issue with lack of colors
> from IPython import embed
> from traitlets.config import get_config
> c = get_config()
> c.InteractiveShellEmbed.colors = "Linux"
> embed(config=c)
> ```



## Option 3: Python builtin `breakpoint()`

> ###### Official Docs
>
> - [`pdb`](https://docs.python.org/3/library/pdb.html#module-pdb) — The Python Debugger
> - [breakpoint()](https://docs.python.org/3/library/functions.html#breakpoint) builtin
>
> ```python
> # Add the following 
> breakpoint()  # puts you in a pdb debugger
> ```
>
> ###### Commands
>
> ``` python
> help         # list of all commands
> c(continue)  # stops debugging and continue running the code
> l(list)      # shows where in the code you are
> list .       # show origion location
> ll           # same as list but shows more code
> where        # stacetrace or where you are
> 
> # useful commands
> locals()     # 
> globals()    #
> p ENVIRONMENT_DIR  # print enviornment variable
> pp <object>        # pretty print
> 
> 
> # step through code
> n(next)   # jump to next line
> s(step)   # if function call, will jump into function call
> r(return) # jump out of function
> ```
>
> ### Customise
>
> ```bash
> # use ipyhton as breakpoint debugger
> export PYTHONBREAKPOINT='IPython.core.debugger.set_trace'
> export PYTHONBREAKPOINT=ipdb.set_trace
> ```
>
> #### Django
>
> ```python
> # update django manage.py settings to use ipdb as default breakpoint() debugger
> def main():
>      os.environ.setdefault("PYTHONBREAKPOINT", "ipdb.set_trace")           # <= added
>      os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example.settings")
>      try:
>          from django.core.management import execute_from_command_line
>          ...
> ```



## Option 4: Use `ipdb`

> This is the same as above, but with an ipython wrapper
>
> ```
> pip install ipdb
> ```
>
> Use the following in your code
>
> ```python
> import ipdb; ipdb.set_trace()
> ```



## Options 5: Remote debugging with `ripdb`

> Install the following packages
>
> ```bash
> pip install ripdb rich
> apt-get install netcat
> apt-get install rlwrap
> ```
>
> Add the following breakpoint to code
>
> ```python
> import ripdb;ripdb.set_trace(addr='127.0.0.1', port=4444)
> ```
>
> Get into interactive debugging console
>
> ```bash
> rlwrap netcat 127.0.0.1 4444
> ```
>
> Gotchas
>
> - kill previous session that access the `127.0.0.1:4444` address
>
> ```bash
> ps -fA       # view processes
> kill <pid>   # kill the pid
> # or craete alias
> kill `ps -fA | grep '/pythonlibs/bin/uwsgi' | grep -v grep | awk \'{print $2}\' | tail -1`
> echo alias k='kill `ps -fA | grep "/pythonlibs/bin/uwsgi" | grep -v grep | awk ''{print $2}'' | tail -1`'' >> .bashrc
> 
> inspect.__globals__['_console'].width= 140  # update width of rich console
> ```

### TODO

- .pdbrc ?

  - > I prefer placing breakpoints in my `.pbdrc` bc then I never have to worry about forgetting to remove them.

- try web-pdb

- [Debugging by attaching over a network connection](https://code.visualstudio.com/docs/python/debugging#_debugging-by-attaching-over-a-network-connection)

- `pytest --pdb`

---

### Links

- [5 Ways of Debugging with IPython](https://switowski.com/blog/ipython-debugging/) : Blog
- [Breakpoint-induced interactive debugging of Python with IPython](https://stackoverflow.com/questions/14635299/breakpoint-induced-interactive-debugging-of-python-with-ipython): Stackover flow post
- [IPython.embed() does not use terminal colors](https://stackoverflow.com/questions/53933400/ipython-embed-does-not-use-terminal-colors): Stackover flow, fixing issue with no ipython colors
- [Python breakpoint()](https://www.digitalocean.com/community/tutorials/python-breakpoint): Digital Ocean tutorial on pythons breakpoint
- [Debugging Python programs without an IDE](https://bastien-antoine.fr/2022/06/debugging-python-programs-without-an-ide/): Blog post
- [Debugging a Containerized Django App in VS Code](https://testdriven.io/blog/django-debugging-vs-code/): Blog post

### Pip installs

```
ipython
ipdb
ripdb
pudb
remote-pudb
remote-pdb
web-pdb
```
