"""Value object for OCR results."""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class OCRResult:
    """Represents extracted OCR data from an image or PDF."""

    extracted_text: str
    detected_tables: list[dict]
    layout_structure: dict
    bounding_boxes: list[dict]
    confidence_scores: dict
    processing_status: str  # "success", "partial", "failed"
