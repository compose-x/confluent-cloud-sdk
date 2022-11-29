# SPDX-License-Identifier: GPL-2.0-only
# Copyright 2022 John Mille <john@compose-x.io>

"""
Client factory
"""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from requests.models import Response

import base64

import requests

from .errors import evaluate_api_return


class ConfluentClient:
    """
    Class to be the client for connections to Confluent Kafka
    See `Confluent Cloud API Reference <https://docs.confluent.io/cloud/current/api.html>`_
    """

    hostname = "api.confluent.cloud"
    api_url = f"https://{hostname}"

    def __init__(self, username: str, password: str, hostname: str = None):
        self._username = username
        self._password = password

        self._auth_hash = base64.b64encode(
            f"{self._username}:{self._password}".encode()
        ).decode()

        self._url = self.api_url if not hostname else f"https://{hostname}"
        self.headers = {
            "Accept": "application/json",
            "Authorization": f"Basic {self._auth_hash}",
        }

    @evaluate_api_return
    def get(self, url: str, ignore_failure: bool = False, **kwargs) -> Response:
        """
        Requests.GET wrapper
        """
        req = requests.get(url, headers=self.headers, **kwargs)
        return req

    @evaluate_api_return
    def post(
        self, url: str, data: dict, ignore_failure: bool = False, **kwargs
    ) -> Response:
        """
        Requests.POST wrapper
        """
        req = requests.post(url, headers=self.headers, json=data, **kwargs)
        return req

    @evaluate_api_return
    def patch(
        self, url: str, data: dict, ignore_failure: bool = False, **kwargs
    ) -> Response:
        """
        Requests.PATCH wrapper
        """
        req = requests.patch(url, headers=self.headers, json=data, **kwargs)
        return req

    @evaluate_api_return
    def delete(self, url: str, ignore_failure: bool = False, **kwargs) -> Response:
        """
        Requests.DELETE wrapper
        """
        req = requests.delete(url, headers=self.headers, **kwargs)
        return req
