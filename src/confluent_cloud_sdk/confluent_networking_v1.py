#  SPDX-License-Identifier: GPL-2.0-only
#  Copyright 2022 John Mille <john@compose-x.io>


class ConfluentNetworkingV1:
    """
    Class to manipulate Confluent Networking using API v1
    `CMKv2 <https://docs.confluent.io/cloud/current/api.html#tag/Clusters-(cmkv2)>_`
    """

    api_v1_path = "/networking/v1"
    clusters_path = f"{api_v1_path}/networks"

    def __init__(
        self,
        client,
        network_id: str = None,
        display_name: str = None,
        description: str = None,
    ):

        self._client = client
        self._id = network_id
        self._name = display_name
        self._description = description
        self._href = None
        self.api_path = self.clusters_path

    @property
    def obj_id(self):
        return self._id

    @obj_id.setter
    def obj_id(self, id_value):
        self._id = id_value

    @property
    def href(self):
        if self._href:
            return self._href
        return f"{self._client.api_url}{self.api_path}/{self.obj_id}"

    @href.setter
    def href(self, url):
        self._href = url

    def list(self):
        if self.api_path:
            return self._client.get(f"{self._client.api_url}{self.api_path}")
        return None

    def read(self):
        return self._client.get(self.href)

    def update(self, description: str):
        return self._client.patch(self.href, data={"description": description})

    def delete(self):
        return self._client.delete(self.href)
