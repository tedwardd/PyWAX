import requests
import json
import sys
import inspect


class apiVersionException(Exception):
    pass


class invalidMethod(Exception):
    pass


class apiException(Exception):
    pass


class emptyQuery(Exception):
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

    def __get(self, url: str) -> requests.models.Response:
        resp = requests.get(url)
        resp.raise_for_status()
        if resp.json().get("error"):
            raise apiException(resp.json().get("error"))
        if resp.json().get("total").get("value") < 1:
            raise emptyQuery("No results found for query")
        return resp

    def __build_query(self, args: dict) -> str:
        # Remove non-query related args
        args.pop("endpoint")
        args.pop("url")
        args.pop("self")
        query = None
        for arg in args:
            if args.get(arg) is not None:
                if query is None:
                    query = f"{arg}={args.get(arg)}"
                else:
                    query = f"&{arg}={args.get(arg)}"
        return query

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
        return self.__get(url)

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
        query = self.__build_query(args)
        if query is None:
            raise Exception("Must provide at least one query parameter")

        return self.__get(f"{url}?{query}")

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
        query = self.__build_query(args)
        if query is None:
            raise Exception("Must provide at least one query parameter")

        return self.__get(f"{url}?{query}")

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
        query = self.__build_query(args)
        if query is None:
            raise Exception("Must provide at least one query parameter")

        return self.__get(f"{url}?{query}")

    def get_transaction(self, id: str):
        endpoint = inspect.currentframe().f_code.co_name
        url = f"{self.url_base}/{endpoint}"
        args = locals()
        query = self.__build_query(args)
        if query is None:
            raise Exception("Must provide at least one query parameter")

        return self.__get(f"{url}?{query}")

    # def get_block(self):
