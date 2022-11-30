#  SPDX-License-Identifier: GPL-2.0-only
#  Copyright 2022 John Mille <john@compose-x.io>

from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Union

from pydantic import BaseModel, Extra

from .confluent_cloud_api import ResourcesList

if TYPE_CHECKING:
    from .client_factory import ConfluentClient

from .confluent_cloud_api.environmentv2 import Spec as ConfluentEnvironmentV2


class ConfluentEnvironment:
    """
    Class to manipulate Confluent Cloud environments
    See `org/v2 <https://docs.confluent.io/cloud/current/api.html#tag/Environments-(orgv2)>`_
    """

    api_path = "/org/v2/environments"

    def __init__(self, client: ConfluentClient, env_id: str = None, spec: dict = None):
        self._client = client
        self._resource = None
        self._resource_class = ConfluentEnvironmentV2

        if env_id and not spec:
            req = self._client.get(f"{self._client.api_url}/{self.api_path}/{env_id}")
            import json

            print(json.dumps(req.json(), indent=2))
            self._resource = self._resource_class(**req.json())
        elif spec:
            self._resource = self._resource_class(**spec)

    @property
    def resource(self) -> ConfluentEnvironmentV2:
        return self._resource

    @property
    def obj_id(self) -> Union[None, str]:
        if self._resource:
            return self._resource.id.__root__
        return None

    def read(self):
        return self._client.get(self.resource.metadata.self)

    def update(self, description: str):
        return self._client.patch(
            self.resource.metadata.self, data={"display_name": description}
        )

    def delete(self):
        return self._client.delete(self.resource.metadata.self)

    def create(self, name: str):
        self._client.post(
            f"{self._client.api_url}{self.api_path}", json={"display_name": name}
        )
