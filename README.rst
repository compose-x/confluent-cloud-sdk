
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

Example with secret in AWS And list all assets
------------------------------------------------

.. code-block:: python

    import json
    from os import environ

    from boto3.session import Session
    from confluent_cloud_sdk.client_factory import ConfluentClient
    from confluent_cloud_sdk.confluent_iam_v2 import ServiceAccount
    from confluent_cloud_sdk.confluent_org_v2 import ConfluentEnvironment
    from confluent_cloud_sdk.confluent_cluster_v2 import KafkaClusterV2

    from compose_x_common.aws import get_session


    def get_confluent_admin_secret(
        secret_arn: str,
        session: Session = None,
        key_id: str = "ApiKey",
        secret_id: str = "ApiSecret",
    ) -> ConfluentClient:
        session = get_session(session)
        client = session.client("secretsmanager")
        value = json.loads(client.get_secret_value(SecretId=secret_arn)["SecretString"])
        return ConfluentClient(value[key_id], value[secret_id])


    cclient = get_confluent_admin_secret(environ.get("SECRET_ARN"))

    envs = cclient.list_all(ConfluentEnvironment)

    for env in envs:
        print(env.obj_id)
        clusters = cclient.list_all(KafkaClusterV2, url_args=f"?environment={env.obj_id}")
        for cluster in clusters:
            print(cluster.obj_id)

    svc_accounts = cclient.list_all(ServiceAccount)
    for svc_account in svc_accounts:
        print(svc_account.obj_id)
        svc_account.import_api_keys()
        print([key.obj_id for key in svc_account.api_keys.values()])

Usage examples
==================

For more details, see docs/usage.rst
