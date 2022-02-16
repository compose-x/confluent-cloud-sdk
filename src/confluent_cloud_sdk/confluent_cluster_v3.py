#   -*- coding: utf-8 -*-
#  SPDX-License-Identifier: GPL-2.0-only
#  Copyright 2022 John Mille <john@compose-x.io>

from .client_factory import ConfluentClient


class KafkaClusterV3(object):
    """
    Class to represent kafka cluster
    The confluent client must be using Cluster API keys, not Global/Cloud API keys
    """

    def __init__(
        self, client: ConfluentClient, cluster_id: str, region: str, provider: str
    ):
        self._client = client
        self.cluster_id = cluster_id
        self.region = region
        self.provider = provider

        self.url = (
            f"https://{self.cluster_id}.{self.region}.{self.provider}.confluent.cloud"
        )
        self.api_path = f"/kafka/v3/clusters/{self.cluster_id}"

    def read(self):
        url = f"{self.url}{self.api_path}"
        return self._client.get(url)