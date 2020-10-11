## Run the Program
### Transform the JSON files to db
```console
$ python transform.py
```

### Start the RESTful API server
TODO

## Unittest
### Configure the test database
Create a MySQL database locally
```console
$ mkdir ~/data && mkdir ~/data/mote
$ docker run --name mote -v ~/data/mote/mysql:/var/lib/mysql -p 3306:3306 -p 33060:33060 -e MYSQL_ROOT_PASSWORD="TF0mW3e5pQlMewbQLsQfbSUbEq" --restart=always -d mysql:latest
```

Enter the MySQL database and create the test database
```console
$ docker exec -it mote /bin/bash
$ mysql -u root -p # enter the password here
$ CREATE DATABASE mote_test;
$ exit
```

### Run the unittests
TODO