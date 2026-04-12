"""Port for message publishing (Google Cloud Pub/Sub)."""

from typing import Protocol


class MessageBusPort(Protocol):
    """Protocol for event/message publishing."""

    async def publish(self, topic_name: str, message: dict) -> str:
        """Publish message to topic.

        Args:
            topic_name: Name of the Pub/Sub topic
            message: Message payload

        Returns:
            Message ID
        """
        ...

    async def subscribe(self, topic_name: str, subscription_name: str) -> None:
        """Subscribe to a topic.

        Args:
            topic_name: Name of the topic to subscribe to
            subscription_name: Name of the subscription
        """
        ...

    async def acknowledge_message(self, ack_id: str) -> None:
        """Acknowledge message processing.

        Args:
            ack_id: Message acknowledgement ID
        """
        ...

    async def publish_domain_event(self, event: dict) -> str:
        """Publish domain event.

        Args:
            event: Domain event object

        Returns:
            Event ID
        """
        ...
