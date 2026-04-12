from dataclasses import dataclass


@dataclass
class DomainEvent:
    event_name: str
    aggregate_id: str
