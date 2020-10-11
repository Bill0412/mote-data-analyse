### Test
Create a MySQL database locally
```console
$ mkdir ~/data && mkdir ~/data/mote
$ docker run --name mote -v ~/data/mote/mysql:/var/lib/mysql -p 3306:3306 -p 33060:33060 -e MYSQL_ROOT_PASSWORD="TF0mW3e5pQlMewbQLsQfbSUbEq" --restart=always -d mysql:latest
```

Enter the MySQL database and create the test database
```console
$ docker exec -it mote /bin/bash
$ mysql -u root -p # enther the password here
$ CREATE DATABASE mote_test;
$ exit
```