#  SPDX-License-Identifier: GPL-2.0-only
#  Copyright 2022 John Mille <john@compose-x.io>

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .client_factory import ConfluentClient


class ConfluentEnvironment:
    """
    Class to manipulate Confluent Cloud environments
    See `org/v2 <https://docs.confluent.io/cloud/current/api.html#tag/Environments-(orgv2)>`_
    """

    api_path = "/org/v2/environments"

    def __init__(self, client: ConfluentClient, name: str = None):
        self._client = client
        self._id = None
        self._name = name
        self._href = None

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

    def create(self, name: str = None):
        if not name and not self._name:
            raise ValueError("You must specify a name for the environment")
        if name:
            self._name = name
        self._client.post(
            f"{self._client.api_url}{self.api_path}", json={"display_name": self._name}
        )
