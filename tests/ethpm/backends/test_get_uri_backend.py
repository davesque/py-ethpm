import pytest

from ethpm.backends import get_uri_backend
from ethpm.backends.ipfs import DummyIPFSBackend, IPFSGatewayBackend


@pytest.fixture(autouse=True)
def reset_get_uri_backend_cache():
    get_uri_backend.cache_clear()


def test_get_uri_backend_default():
    backend = get_uri_backend()
    assert isinstance(backend, IPFSGatewayBackend)


def test_get_uri_backend_with_env_variable(monkeypatch):
    monkeypatch.setenv(
        "ETHPM_URI_BACKEND_CLASS", "ethpm.backends.ipfs.DummyIPFSBackend"
    )
    backend = get_uri_backend()
    assert isinstance(backend, DummyIPFSBackend)
