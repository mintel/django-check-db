django-check-db
===============

.. image:: https://img.shields.io/pypi/v/django-check-db.svg
    :alt: PyPI
    :target: https://pypi.org/project/django-check-db/

A Django management command to check that connections can be established to all databases.

.. code-block:: bash

    $ ./manage.py check_db_connections --timeout=1
    default OK

Install
-------

.. code-block:: bash

    $ pipenv install django-check-db


Add `django_check_db` to your Django `INSTALLED_APPS`.


Changes
-------

**0.1.0-dev**

* Initial release
