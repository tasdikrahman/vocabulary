

============
Installation
============

Option 1: installing through `pip <https://pypi.python.org/pypi/vocabulary>`__ (Suggested way)
==============================================================================================

`pypi package link <https://pypi.python.org/pypi/vocabulary>`__

.. code-block:: bash

    $ pip install vocabulary

If you are behind a proxy

.. code-block:: bash

    $ pip --proxy [username:password@]domain_name:port install vocabulary

.. Note:: If you get ``command not found`` then

.. code-block:: bash

    $ sudo apt-get install python-pip

should fix that

Option 2: Installing from source
================================

.. code-block:: bash

    $ git clone https://github.com/prodicus/vocabulary.git
    $ cd vocabulary/
    $ pip install -r requirements.txt
    $ python setup.py install

Upgrade
=======

You can update to the latest version by doing a

.. code-block:: bash

    $ pip install --upgrade vocabulary

Uninstalling
============

.. code-block:: bash

    $ pip uninstall vocabulary
