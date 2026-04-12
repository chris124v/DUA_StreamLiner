from typing import Protocol

class TaskQueuePort(Protocol):
    def enqueue(self, task_name: str, payload: dict) -> None: ...

