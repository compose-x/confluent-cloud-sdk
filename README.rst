
.. meta::
    :description: Confluent Cloud SDK
    :keywords: kafka, confluent, cloud, sdk

=======================
Confluent Cloud SDK
=======================

SDK to interact with Confluent Cloud API

Installation
=============

.. code-block:: bash

    pip install confluent-cloud-sdk

Usage examples
==================

For more details, see docs/usage.rst

Imports
---------

To use Confluent Admin API SDK in a project


.. code-block:: python

    from confluent_cloud_sdk.client_factory import ConfluentClient
    from confluent_cloud_sdk.confluent_iam_v2 import ApiKey
    from confluent_cloud_sdk.confluent_iam_v2 import ServiceAccount



Initialize connection
----------------------


.. code-block:: python

    client = ConfluentClient(
        "cloud_key_key",
        "cloud_key_secret",
    )


List all service accounts
--------------------------

.. code-block:: python

    accounts_request = ServiceAccount(client, None).list()
    for account in accounts_request.json()["data"]
        print(account)


Create a new service account
-----------------------------

.. code-block:: python

    new_service_account = ServiceAccount(
        client, display_name="test_client", description="A simple service account"
    )
    try:
        new_service_account.create() # we try to create the user. If already exists, there will be conflict.
    except GenericConflict:
        new_service_account.set_from_read()

    print("SVC ACCOUNT ID IS", new_service_account.obj_id)


List all API Keys of the service account
---------------------------------------------

.. code-block:: python

    new_service_account.import_api_keys()
    for key in new_service._api_keys:
        print(key.id)


Create a new API Key for the service account for a given resource
-------------------------------------------------------------------

.. code-block:: python

    new_api_key = ApiKey(client, display_name="new-test-key")
    new_api_key.create(
        owner_id=new_service_account.obj_id,
        resource_id="cluster_id",
    )
