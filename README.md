How to run:

```
$ docker-compose up --build
```

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
from `docker/nginx` to locally trusted certs.


ToDos:
======

* add tests (see tox.ini)
* use redis for sessions
* serve media from nginx
