import requests


class apiException(Exception):
    pass


class emptyQuery(Exception):
    pass


def get_resp(url: str) -> requests.models.Response:
    resp = requests.get(url)
    resp.raise_for_status()
    if resp.json().get("error"):
        raise apiException(resp.json().get("error"))
    if resp.json().get("total").get("value") < 1:
        raise emptyQuery("No results found for query")
    return resp


def build_query(args: dict) -> str:
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
