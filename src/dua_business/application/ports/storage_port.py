from typing import Protocol

class StoragePort(Protocol):
    def upload_file(self, path: str, content: bytes) -> str: ...

