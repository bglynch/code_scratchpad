# AWS Cloud 9 - Snippits

### Creating Virtual Enviornments
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