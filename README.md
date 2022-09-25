# iKYC System

A database system that implemented face recognition using python and mysql.

*******

## Useage

### Environment

Create virtual environment using Anaconda.
```
conda create -n face python=3.x
conda activate face
pip install -r requirements.txt
```

### MySQL Install

[Mac](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/macos-installation.html)

[Ubuntu](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/linux-installation.html)

[Windows](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/windows-installation.html)

You'll obtain an account and password after installation, then you should modify the `faces.py`, with the corresponding
`user` and `passwd`:
```
# create database connection
myconn = mysql.connector.connect(host="localhost", user="root", passwd="xxxxx", database="facerecognition")
```

*******

## Run


### 2. Database Design

#### 2.1 Define Database



#### 2.2 Import Database
Open mysql server and import the file `facerecognition.sql`.
```
# login the mysql command
mysql -u root -p

# create database.  'mysql>' indicates we are now in the mysql command line
mysql> CREATE DATABASE sysDB;
mysql> USE sysDB;

# import from sql file
mysql> source createDB.sql
```



### 3. Login Interface

