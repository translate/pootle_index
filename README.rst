Pootle index
============

Integration of django-haystack and search backends for Pootle.


Installation
------------

Currently only installable from git

.. code-block:: bash

  $ pip install -e git@github.com:translate/pootle_index


Configuration
-------------

Add ``haystack`` and ``pootle_index`` to your ``INSTALLED_APPS``:

.. code-block:: python

  INSTALLED_APPS += ["haystack", "pootle_index"]


Add a configuration for your haystack backend, only Elasticsearch is currently tested

.. code-block:: python

  HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack'}}

Add a configuration for a haystack signal processor, to keep your index up to date:

.. code-block:: python

  HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'


Finally set the ``POOTLE_SEARCH_BACKEND`` in your settings to the haystack search backend.

.. code-block:: python

   POOTLE_SEARCH_BACKEND = "pootle_index.search.HaystackSearchBackend"


Indexing your Pootle server
---------------------------

If you wish to clear the index and start again you can do the following:

.. code-block:: bash

  $ pootle rebuild_index

Rebuilding the index will take a very long time on a large site.

To simply update the index:

.. code-block:: bash

  $ pootle update_index

