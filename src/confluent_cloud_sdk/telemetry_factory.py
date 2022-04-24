#  SPDX-License-Identifier: GPL-2.0-only
#  Copyright 2022 John Mille <john@compose-x.io>

from __future__ import annotations

"""
Client factory for the confluent cloud telemetry API
"""
import base64

import requests

from .errors import evaluate_api_return


class ConfluentTelemetry:
    """
    Class to be the client for connections to Confluent Kafka Telemetry API
    See `Confluent Cloud Telemetry API Reference <https://api.telemetry.confluent.cloud/docs>`_
    """

    hostname = "api.telemetry.confluent.cloud"
    api_url = f"https://{hostname}"

    def __init__(self, username: str, password: str, hostname: str = None):
        self._username = username
        self._password = password

        self._auth_hash = base64.b64encode(
            f"{self._username}:{self._password}".encode()
        ).decode()

        self._url = self.api_url if not hostname else f"https://{hostname}"
        self.headers = {
            "Accept": "application/json, text/plain",
            "Authorization": f"Basic {self._auth_hash}",
        }

    @evaluate_api_return
    def get(self, url: str, ignore_failure: bool = False, **kwargs):
        """
        Requests.GET wrapper

        :param url:
        :param ignore_failure: whether or not ignore failure error codes
        :param kwargs:
        :return:
        """
        req = requests.get(url, headers=self.headers, **kwargs)
        return req

    @evaluate_api_return
    def post(self, url: str, data: dict, ignore_failure: bool = False, **kwargs):
        """
        Requests.GET wrapper

        :param url:
        :param ignore_failure: whether or not ignore failure error codes
        :param kwargs:
        :return:
        """
        req = requests.post(url, headers=self.headers, json=data, **kwargs)
        return req

    @evaluate_api_return
    def patch(self, url: str, data: dict, ignore_failure: bool = False, **kwargs):
        """
        Requests.GET wrapper

        :param url:
        :param ignore_failure: whether or not ignore failure error codes
        :param kwargs:
        :return:
        """
        req = requests.patch(url, headers=self.headers, json=data, **kwargs)
        return req

    @evaluate_api_return
    def delete(self, url: str, ignore_failure: bool = False, **kwargs):
        """
        Requests.GET wrapper

        :param url:
        :param ignore_failure: whether or not ignore failure error codes
        :param kwargs:
        :return:
        """
        req = requests.delete(url, headers=self.headers, **kwargs)
        return req

    def export_metrics(self, clusters: list[str]):
        """
        `export <https://api.telemetry.confluent.cloud/docs#tag/Version-2/paths/~1v2~1metrics~1{dataset}~1export/get>`_
        """
        clusters_query = "&".join(
            [f"resource.kafka.id={cluster}" for cluster in clusters]
        )
        _url = f"{self.api_url}/v2/metrics/cloud/export?{clusters_query}"
        return self.get(_url)
