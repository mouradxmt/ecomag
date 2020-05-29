# Django Project Template

ECOMAG is a  Django based plateform for e-commerce, it was made initially by _(MTOUAA Mourad, RAMDANI Chaimae, KHADDAM Allah Hajar) in 2019/2020 as final year's project guided by Pr. CHETIOUI Kaouthar, and it is intended to be started as a real life plateform .
## Getting Started
### Prerequisites
* Python  >=3.7
* pip
* git
* PostgreSQL
* and a working internet connection


Clone the project from github
```
$ git clone https://github.com/mouradxmt/ecomag.git
Cloning into 'ecomag'...
remote: Enumerating objects: 6981, done.
remote: Counting objects: 100% (6981/6981), done.
remote: Compressing objects: 100% (3994/3994), done.
remote: Total 6981 (delta 2052), reused 6869 (delta 1942), pack-reused 0
Receiving objects: 100% (6981/6981), 24.13 MiB | 1.07 MiB/s, done.
Resolving deltas: 100% (2052/2052), done.
$ cd ecomag
```
Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ python -m venv venv
```
### Activating _venv_ (Virtual Environment)
##### For Linux/macOS
```bash
$ source venv/bin/activate
```
##### For Windows
```bash
$ venv\Scripts\activate
```
### Installing requirements (Needed Packages)
```
$ pip install -r requirements.txt
```
and edit the file `ecomag/settings.py` _(Ligne `81` to `88`)_ to the according PostgreSQL database credentials. 

Then update the database content and run the server by these commands
```
$ python manage.py migrate
$ python manage.py runserver
```

Create a superuser
```
$ python manage.py createsuperuser
Nom d’utilisateur (leave blank to use 'u20908'): admin
Adresse électronique: monemail@gmail.com
Password:
Password (again):
Superuser created successfully.
```
And we can access the admin panel via : `http://localhost:8080/admin` and fill in the credentials we just created.
