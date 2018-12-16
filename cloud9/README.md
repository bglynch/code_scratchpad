# AWS Cloud 9 - Snippits

## Creating Virtual Enviornments
#### Python 2
```bash
sudo pip install virtualenv
virtualenv venv
source venv/bin/activate
```
#### Python 3.4
```bash
sudo pip install virtualenv
virtualenv -p /usr/bin/python3.4 venv
source venv/bin/activate
```
#### Python 3.6
```
sudo apt update
sudo apt install python3.6-venv
python3.6 -mvenv venv
source venv/bin/activate
```
---
## Create own file for Enviornment Variables
### OPTION 01: Link to a Single file
Create file to store the variables
```
name:~/workspace (master) $ touch .env
```
Adding an enviornment varible
###### ~/workspace/.env
```
export HELLO='foobar'
```
Add code to the base of the  **~/.profile** file to link to the .env file
```bash
if [ -n "$BASH_VERSION" ]; then
    # include .env file if it exists
    if [ -f "$HOME/workspace/.env" ]; then
	. "$HOME/workspace/.env"
    fi
fi
```
Restart the **~/.profile** file
```
name:~/workspace (master) $ source ~/.profile
````
Check that it worked
```bash
name:~/workspace (master) $ env
```
```bash
...
APACHE_RUN_USER=ubuntu
SHELL=/bin/bash
C9_PORT=8080
METEOR_IP=0.0.0.0
USER=ubuntu
HOME=/home/ubuntu
GOPATH=/home/ubuntu/workspace
PORT=8080
IP=0.0.0.0
HELLO='foobar'
...
```

### OPTION 02: Auto add Env Variables from corrent dir .env file

Add code to the base of the  **~/.profile** file to link to the .env file
```bash
# function to add enviornment variables from the .env file of the current directory
function auto_env() {
    if [ -n "$BASH_VERSION" ]; then
        # include .bashrc if it exists
        if [ -f "$PWD/.env" ]; then
    	. "$PWD/.env"
        fi
    fi
}

# runs auto_env function every time a bash command is entered
export PROMPT_COMMAND="auto_env;$PROMPT_COMMAND"
```
Restart the **~/.profile** file
```
name:~/workspace (master) $ source ~/.profile
````
Now if there is a file named "**.env**" in the current directory, 
it's Enviorn Variables will be added.   
  

Sample file layout
```
.

├── project1
│   └── .env
├── project2
│   └── .env
└── project3
    └── .env
```