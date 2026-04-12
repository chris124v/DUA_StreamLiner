from dataclasses import dataclass

from dua_business.domain.events.domain_event import DomainEvent


@dataclass
class DuaCreatedEvent(DomainEvent):
    pass


@dataclass
class DocumentsUploadedEvent(DomainEvent):
    pass


@dataclass
class GenerationStatusChangedEvent(DomainEvent):
    pass
