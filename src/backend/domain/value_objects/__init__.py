"""Value objects for the DUA domain."""

from dua_business.domain.value_objects.confidence import Confidence
from dua_business.domain.value_objects.generation_status import GenerationStatus
from dua_business.domain.value_objects.permission import Permission
from dua_business.domain.value_objects.role import Role
from dua_business.domain.value_objects.document_type import (
    DocumentType,
    DocumentCategory,
    DUAProcessType,
)
from dua_business.domain.value_objects.document_block import (
    DocumentBlock,
    ExtractedField,
)
from dua_business.domain.value_objects.template_mapping import (
    TemplateFieldMapping,
    DUATemplateBlock,
)
from dua_business.domain.value_objects.ocr_result import OCRResult
from dua_business.domain.value_objects.customs_fields import (
    ImporterExporterData,
    SupplierInfo,
    GoodsDescription,
    TransportInfo,
    InvoiceDetails,
    CustomsRegimeInfo,
)

__all__ = [
    "Confidence",
    "GenerationStatus",
    "Permission",
    "Role",
    "DocumentType",
    "DocumentCategory",
    "DUAProcessType",
    "DocumentBlock",
    "ExtractedField",
    "TemplateFieldMapping",
    "DUATemplateBlock",
    "OCRResult",
    "ImporterExporterData",
    "SupplierInfo",
    "GoodsDescription",
    "TransportInfo",
    "InvoiceDetails",
    "CustomsRegimeInfo",
]
