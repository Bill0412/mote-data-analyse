# Data Engineering Pipeline
## Transform the JSON files to MySQL database
```console
$ python transform.py
```

## Run the RESTful API server
```console
$ python api.py
```

### `GET` outlets who sell certain brands
Following returns a list of outlets that has coca inside its brand name.
```console
$ curl http://localhost:5000/outlets/brand/contains/coca
```

### `GET` a list of outlets
```console
$ curl http://localhost:5000/outlets/source/ubereats
```
 
### `GET` menu items above a certain price
```console
$ curl http://localhost:5000/menus/price/above/40
```

### `POST` a new outlet
```console
$ curl http://localhost:5000/outlets -d "id_outlet=1029912390213" -d "name=hello_world" -d "source=ubereats" -d "address=unknown" -d "country=CN" -d "phone=+852 123 1234" -d "reviews_nr=123" -X POST -v
```

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
pass