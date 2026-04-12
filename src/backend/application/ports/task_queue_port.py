"""Port for task queuing (Google Cloud Tasks)."""

from typing import Protocol, Optional


class TaskQueuePort(Protocol):
    """Protocol for background task queuing."""

    async def enqueue_task(
        self, queue_name: str, task_name: str, payload: dict, delay_seconds: int = 0
    ) -> str:
        """Enqueue a background task.

        Args:
            queue_name: Name of the task queue
            task_name: Name of the task to execute
            payload: Task payload/parameters
            delay_seconds: Delay before execution in seconds

        Returns:
            Task ID
        """
        ...

    async def get_task_status(self, task_id: str) -> dict:
        """Get status of a queued task.

        Args:
            task_id: The task ID

        Returns:
            Task status dictionary
        """
        ...

    async def cancel_task(self, task_id: str) -> None:
        """Cancel a queued task.

        Args:
            task_id: The task ID to cancel
        """
        ...

    async def enqueue_document_pipeline(
        self, generation_id: str, document_ids: list[str]
    ) -> str:
        """Enqueue document processing pipeline.

        Args:
            generation_id: The generation session ID
            document_ids: List of document IDs to process

        Returns:
            Pipeline execution ID
        """
        ...
