from typing import Protocol

class MessageBusPort(Protocol):
    def publish(self, event_name: str, payload: dict) -> None: ...

