import json
from typing import Any, Dict
from urllib import parse

from eth_utils import to_text

from ethpm.backends.ipfs import get_ipfs_backend
from ethpm.exceptions import UriNotSupportedError

IPFS_SCHEME = "ipfs"

INTERNET_SCHEMES = ["http", "https"]

SWARM_SCHEMES = ["bzz", "bzz-immutable", "bzz-raw"]


def get_manifest_from_content_addressed_uri(uri: str) -> Dict[str, Any]:
    """
    Return manifest data stored at a content addressed URI.
    """
    parse_result = parse.urlparse(uri)
    scheme = parse_result.scheme

    if scheme == IPFS_SCHEME:
        ipfs_backend = get_ipfs_backend()
        if ipfs_backend.can_handle_uri(uri):
            raw_manifest_data = ipfs_backend.fetch_uri_contents(uri)
            manifest_data = to_text(raw_manifest_data)
            return json.loads(manifest_data)
        else:
            raise TypeError(
                "The IPFS Backend: {0} cannot handle the given URI: {1}.".format(
                    type(ipfs_backend).__name__, uri
                )
            )

    if scheme in INTERNET_SCHEMES:
        raise UriNotSupportedError("Internet URIs are not yet supported.")

    if scheme in SWARM_SCHEMES:
        raise UriNotSupportedError("Swarm URIs are not yet supported.")

    raise UriNotSupportedError("The URI scheme:{0} is not supported.".format(scheme))
