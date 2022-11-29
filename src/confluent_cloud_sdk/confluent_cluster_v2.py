#  SPDX-License-Identifier: GPL-2.0-only
#  Copyright 2022 John Mille <john@compose-x.io>

from __future__ import annotations

import warnings
from typing import Union

from .confluent_cloud_api.cluster_v2 import SpecModel as ClusterV2


class KafkaClusterV2:
    """
    Class to manipulate Confluent Cluster using API v2
    `CMKv2 <https://docs.confluent.io/cloud/current/api.html#tag/Clusters-(cmkv2)>_`
    """

    api_v2_path = "/cmk/v2"
    clusters_path = f"{api_v2_path}/clusters"

    def __init__(
        self,
        client,
        environment_id: str,
    ):
        self.api_path = self.clusters_path
        self._client = client
        self._resource = None
        self._resource_class = ClusterV2

    @property
    def resource(self) -> ClusterV2:
        return self._resource

    @property
    def obj_id(self) -> Union[None, str]:
        if self._resource:
            return self._resource.id.__root__
        return None

    def list(self, environment_id: str) -> list:
        if self.api_path:
            return self._client.get(
                f"{self._client.api_url}{self.api_path}?environment={environment_id}"
            )
        return []

    def read(self):
        return self._client.get(self.resource)

    def update(self, description: str):
        warnings.warn(NotImplemented("Update cluster not implemented"))

    def delete(self):
        return self._client.delete(self.resource.metadata.self)
