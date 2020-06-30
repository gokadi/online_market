How to run:

For the first run do:
```
$ docker-compose build
$ docker-compose up
```

This will run all needed containers and app will be accessible on `0.0.0.0:80`.
Also, dump will be loaded. 
For clean run (empty db with only dump loaded), before every new application start do: 

```
$ docker-compose rm
```

You can login with these creds:

```
gokadi@yandex.ru
qwe123qwe
```

This is superuser with access to the admin panel (`/admin/`).

Go to `http://0.0.0.0:80/admin/`, add some categories, 
subcategories & products.
Then you can go back to `0.0.0.0:80` and make orders. Don't forget to fill in 
the address here: `0.0.0.0:80/users/profile_address/`

There may be some SSL certificate issues. In this case, just add cert 
from `docker/nginx` to locally trusted certs or try in older Chrome version 
(this is much easier).


ToDos:
======

* add tests (see tox.ini & Makefile)
* use redis for sessions
* serve media from nginx (add volume to docker-compose)
* refactor nginx.conf (remove duplicates)
* cleanup code
* prettify css
