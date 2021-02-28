import requests
import json
import sys
import inspect

from common import get_resp, build_query


class apiVersionException(Exception):
    pass


class invalidMethod(Exception):
    pass


class History:
    def __init__(
        self,
        api_version="v2",
        server="wax.eosphere.io",
    ):
        self.limit = 100
        valid_api_versions = ["v1", "v2"]
        if api_version not in valid_api_versions:
            raise apiVersionException("Specified API version is invalid")
        # TODO: Support v1 api:
        if api_version == "v1":
            apiVersionException("v1 APIs are not yet supported")
        self.api_version = api_version  # use v2 apis unless explicitely overriden
        self.server = server
        self.url_base = f"https://{self.server}/{self.api_version}/history"

    def get_abi_snapshot(
        self,
        contract: str,
        block: int = None,
        limit: int = None,
    ) -> requests.models.Response:
        endpoint = inspect.currentframe().f_code.co_name
        url = f"https://{self.server}/{self.api_version}/{endpoint}?contract={contract}"
        if block is not None:
            url += f"&block={int(block)}"
        if limit is not None:
            self.limit = limit
        return get_resp(url)

    def get_actions(
        self,
        limit: int = None,
        skip: int = None,
        account: str = None,
        track: int = None,
        filter: str = None,
        sort: str = None,
        after: str = None,
        before: str = None,
        simple: bool = None,
        noBinary: bool = None,
        checkLib: bool = None,
    ) -> requests.models.Response:
        endpoint = inspect.currentframe().f_code.co_name
        url = f"{self.url_base}/{endpoint}"
        args = locals()
        query = build_query(args)
        if query is None:
            raise Exception("Must provide at least one query parameter")

        return get_resp(f"{url}?{query}")

    def get_deltas(
        self,
        limit: int = None,
        skip: int = None,
        code: str = None,
        scope: str = None,
        table: str = None,
        payer: str = None,
    ) -> requests.models.Response:
        endpoint = inspect.currentframe().f_code.co_name
        url = f"{self.url_base}/{endpoint}"
        args = locals()
        query = build_query(args)
        if query is None:
            raise Exception("Must provide at least one query parameter")

        return get_resp(f"{url}?{query}")

    def get_schedule(
        self,
        producer: str = None,
        key: str = None,
        after: str = None,
        before: str = None,
        version: int = None,
    ):
        endpoint = inspect.currentframe().f_code.co_name
        url = f"{self.url_base}/{endpoint}"
        args = locals()
        query = build_query(args)
        if query is None:
            raise Exception("Must provide at least one query parameter")

        return get_resp(f"{url}?{query}")

    def get_transaction(self, id: str):
        endpoint = inspect.currentframe().f_code.co_name
        url = f"{self.url_base}/{endpoint}"
        args = locals()
        query = build_query(args)
        if query is None:
            raise Exception("Must provide at least one query parameter")

        return get_resp(f"{url}?{query}")

    # def get_block(self):
