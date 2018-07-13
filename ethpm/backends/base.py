from abc import ABC, abstractmethod


class BaseURIBackend(ABC):
    """
    Abstract base URI backend.

    To handle a URI, a backend must be able to:

    * Say if it knows how to handle it
    * Be able to fetch contents for it

    URI backends can be stateful.  That is, they may set up any resources they
    need to complete their function in their ``__init__`` method.
    """

    @abstractmethod
    def can_handle_uri(self, uri: str) -> bool:
        """
        Return a bool indicating whether this backend class can handle the given URI.
        """
        pass

    @abstractmethod
    def fetch_uri_contents(self, uri: str) -> bytes:
        """
        Fetch the contents stored at a URI.
        """
        pass
