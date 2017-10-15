Python 3 Flask RESTful API template
***********************************

.. image:: https://travis-ci.org/stepgazaille/flask-restful-api-template.svg?branch=master
    :target: https://travis-ci.org/stepgazaille/flask-restful-api-template

.. contents:: **Contents of this document**
   :depth: 2


Description
===========
This is a template project for creating REST APIs using Python 3 and Flask.


Requirements
============
See `requirements.txt <https://github.com/stepgazaille/flask-restful-api-template/blob/master/requirements.txt>`_.


Installation
============
Run the install.sh script to install the app's dependencies:

.. code:: shell

  ./install.sh


Usage
=====
Run the following commands start the server (assumes activated Python3 virtual env):

.. code:: shell

  python app.py


Tests
=====
Run the install-dev-dependencies.sh script to install the app's dev/tests dependencies (assumes activated Python3 virtual env):

.. code:: shell

  sudo ./install-dev-dependencies.sh
  pip install -r dev-requirements.txt

Run the following command to run smoke tests (server must be running):

.. code:: shell

  newman run tests/smoke-tests.json -e tests/local-environment.json
