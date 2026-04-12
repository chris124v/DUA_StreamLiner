from typing import Protocol

class OCRPort(Protocol):
    def extract(self, file_uri: str) -> dict: ...

