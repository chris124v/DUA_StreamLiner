from dua_business.application.ports.message_bus_port import MessageBusPort

class PubSubMessageBusAdapter(MessageBusPort):
    def publish(self, event_name: str, payload: dict) -> None:
        _ = event_name
        _ = payload
        raise NotImplementedError("Contract only")

