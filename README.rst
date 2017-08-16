Python 3 REST API template
**************************


.. contents:: **Contents of this document**
   :depth: 2


Description
===========
This is a template project for creating REST APIs using Python 3 and Flask.


Requirements
============
See requirements.txt


Installation
============
Run the install.sh script to install the app's dependencies:

.. code:: shell

  ./install.sh


Usage
=====
.. code:: shell

  python app.py


Tests
=====
Run the install-tests-dependencies.sh script to install the app's tests dependencies:

.. code:: shell

  ./install-tests-dependencies.sh

Run the following command to run smoke tests (server must be running):

.. code:: shell

  newman run tests/smoke-tests.json -e tests/local-environment.json
