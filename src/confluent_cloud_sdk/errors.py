# SPDX-License-Identifier: GPL-2.0-only
# Copyright 2022 John Mille <john@compose-x.io>

"""
Confluent Cloud API SDK Exceptions and error handling
"""

from compose_x_common.compose_x_common import keyisset


class ConfluentException(Exception):
    """
    Generic class handling for the SDK using the request as input
    """

    def __init__(self, msg, code, details):
        """

        :param msg:
        :param code:
        :param details:
        """
        super().__init__(msg, code, details)
        self.code = code
        self.details = details


class GenericNotFound(ConfluentException):
    """
    Generic option for 404 return code
    """

    def __init__(self, code, details):
        super().__init__(details.get("detail", "Resource not found"), code, details)


class GenericConflict(ConfluentException):
    """
    Generic option for 409 return code
    """

    def __init__(self, code, details):
        super().__init__(details.get("detail", "Resources conflict"), code, details)


class GenericUnauthorized(ConfluentException):
    """
    Generic option for 401 return code
    """

    def __init__(self, code, details):
        super().__init__(details.get("detail", "Access unauthorized"), code, details)


class GenericRequestError(ConfluentException):
    """
    Generic option for 400 return code
    """

    def __init__(self, code, details):
        super().__init__(details.get("detail", "Request error"), code, details)


class GenericForbidden(ConfluentException):
    """
    Generic exception for a 403
    """

    def __init__(self, code, details):
        super().__init__(details.get("detail", "403 Forbidden"), code, details)


class ConfluentApiException(ConfluentException):
    """
    Top class for DatabaseUser exceptions
    """

    def __init__(self, code, details):
        if code == 409:
            raise GenericConflict(code, details)
        elif code == 404:
            raise GenericNotFound(code, details)
        elif code == 401:
            raise GenericUnauthorized(code, details)
        elif code == 403:
            raise GenericForbidden(code, details)
        elif code == 400:
            raise GenericRequestError(code, details)
        super().__init__("Something was wrong with the client request.", code, details)


def evaluate_api_return(function):
    """
    Decorator to evaluate the requests payload returned
    """

    def wrapped_answer(*args, **kwargs):
        """
        Decorator wrapper
        """
        payload = function(*args, **kwargs)
        if payload.status_code not in [200, 201, 202, 204] and not keyisset(
            "ignore_failure", kwargs
        ):
            details = payload.json()
            raise ConfluentApiException(payload.status_code, details)

        elif keyisset("ignore_failure", kwargs):
            return payload
        return payload

    return wrapped_answer
