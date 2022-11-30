#  SPDX-License-Identifier: GPL-2.0-only
#  Copyright 2022 John Mille <john@compose-x.io>

from __future__ import annotations

import json
import warnings
from typing import List, Optional, Union

from pydantic import BaseModel, Extra

from .confluent_cloud_api import ResourcesList
from .confluent_cloud_api.cluster_v2 import SpecModel as ClusterV2


class KafkaClusterV2:
    """
    Class to manipulate Confluent Cluster using API v2
    `CMKv2 <https://docs.confluent.io/cloud/current/api.html#tag/Clusters-(cmkv2)>_`
    """

    api_path = "/cmk/v2/clusters"

    def __init__(
        self,
        client,
        resource_id: str = None,
        environment_id: str = None,
        spec: dict = None,
    ):
        self._client = client
        self._resource = None
        self._resource_class = ClusterV2

        if resource_id and environment_id and not spec:
            req = client.get(
                f"{self._client.api_url}{self.api_path}/{resource_id}?environment={environment_id}"
            )
            # print(json.dumps(req.json(), indent=2))
            self._resource = self._resource_class(**req.json())
        elif spec:
            self._resource = self._resource_class(**spec)

    @property
    def resource(self) -> ClusterV2:
        return self._resource

    @property
    def obj_id(self) -> Union[None, str]:
        if self._resource:
            return self._resource.id.__root__
        return None

    def read(self):
        return self._client.get(self.resource)

    def update(self, description: str):
        warnings.warn(NotImplemented("Update cluster not implemented"))

    def delete(self, no_dry_run: bool = False):
        if no_dry_run:
            return self._client.delete(self.resource.metadata.self)
