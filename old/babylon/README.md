Description
====================

Babylon api

Usage
============================

Installation
----------------
Assuming you have virtualenvwrapper installed on the system

```
mkvirtualenv babylon --python=/usr/bin/python3.5
cd babylon
pip install -r requirements.txt
python setup.py install
sudo mkdir -p /etc/web/
This will define the configuration of your application, you can change it, except it location, which is on web/constants.py
sudo cp contrib/settings.yaml /etc/web/settings.yaml

This can be change in settings file and you won't need to creat the file.
sudo mkdir -p /var/log/babylon/
```

Run
-----------------

Assuming you have created the virtualenv, switched to that virtualenv and you are on the repository
 folder:

 
### Babylon Api as a python script
```
python web/wsgi.py 
```

###Babylon Api with uwsgi serving http directly
```
uwsgi --socket 0.0.0.0:5000 --protocol=http -w web.wsgi:app --processes 4
```

Manager
-----------------
To see the different options:
```
python web/manager --help
```

### Bdd

```
python web/manager bdd
```