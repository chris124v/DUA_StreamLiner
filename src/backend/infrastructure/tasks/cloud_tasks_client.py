from dua_business.application.ports.task_queue_port import TaskQueuePort

class CloudTasksQueueAdapter(TaskQueuePort):
    def enqueue(self, task_name: str, payload: dict) -> None:
        _ = task_name
        _ = payload
        raise NotImplementedError("Contract only")

