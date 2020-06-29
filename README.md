How to run:

```
$ docker-compose build
```


```
$ docker-compose up
$ docker-compose up
```
^ call it twice 
(Database starts slower than prepare_database does. Fix is in todo: 
*make wait script to run `prepare_database` image*.)


In another tab do:
```
$ docker-compose exec app /bin/sh
$ django-admin createsuperuser
```

Follow the instructions.
Then go to `http://0.0.0.0:8000/admin/`, login, add some categories, 
subcategories & products.
Then you can go back to `0.0.0.0:8000` and make orders. Don't forget to fill in 
the address here: `0.0.0.0:8000/users/profile_address/`

There may be some SSL certificate issues. In this case, just add cert 
from `docker/nginx` to locally trusted certs or try in older Chrome version 
(this is much easier).


ToDos:
======

* add tests (see tox.ini)
* use redis for sessions
* serve media from nginx
* refactor nginx.conf (remove duplicates)
* cleanup code
* make wait script to run `prepare_database` image
