"""Value object for document types."""

from enum import Enum


class DocumentType(str, Enum):
    """Enumeration of supported document types."""

    IMAGE = "image"
    EXCEL = "excel"
    WORD = "word"
    PDF = "pdf"


class DocumentCategory(str, Enum):
    """Enumeration of document categories for classification."""

    COMMERCIAL_INVOICE = "commercial_invoice"
    TRANSPORT_DOCUMENT = "transport_document"
    CERTIFICATE_OF_ORIGIN = "certificate_of_origin"
    PACKING_LIST = "packing_list"
    FINANCIAL_DOCUMENT = "financial_document"
    OTHER = "other"


class DUAProcessType(str, Enum):
    """Enumeration for DUA process type."""

    IMPORT = "import"
    EXPORT = "export"
