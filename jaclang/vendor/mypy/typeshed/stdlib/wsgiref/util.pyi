import sys
from _typeshed.wsgi import WSGIEnvironment
from collections.abc import Callable
from typing import IO, Any

__all__ = [
    "FileWrapper",
    "guess_scheme",
    "application_uri",
    "request_uri",
    "shift_path_info",
    "setup_testing_defaults",
]

class FileWrapper:
    filelike: IO[bytes]
    blksize: int
    close: Callable[[], None]  # only exists if filelike.close exists
    def __init__(self, filelike: IO[bytes], blksize: int = 8192) -> None: ...
    if sys.version_info < (3, 11):
        def __getitem__(self, key: Any) -> bytes: ...

    def __iter__(self) -> FileWrapper: ...
    def __next__(self) -> bytes: ...

def guess_scheme(environ: WSGIEnvironment) -> str: ...
def application_uri(environ: WSGIEnvironment) -> str: ...
def request_uri(environ: WSGIEnvironment, include_query: bool = True) -> str: ...
def shift_path_info(environ: WSGIEnvironment) -> str | None: ...
def setup_testing_defaults(environ: WSGIEnvironment) -> None: ...
def is_hop_by_hop(header_name: str) -> bool: ...
