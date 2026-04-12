from typing import Protocol

class AIPort(Protocol):
    def classify(self, text: str) -> dict: ...

