from dataclasses import dataclass


@dataclass
class Document:
    document_id: str
    filename: str
    mime_type: str
    category: str | None = None
