from typing import Protocol

from dua_business.domain.entities.document import Document


class DocumentRepository(Protocol):
    def save(self, document: Document) -> None: ...
