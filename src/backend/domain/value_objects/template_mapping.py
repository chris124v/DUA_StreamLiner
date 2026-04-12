"""Value object for template field mapping."""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class TemplateFieldMapping:
    """Represents mapping of extracted data to DUA template fields."""

    dua_section: str
    dua_field_name: str
    extracted_value: str
    confidence_score: float
    warning_level: str  # "green", "yellow", "red"
    alternative_matches: list[dict] = None  # Top 2 alternative candidates


@dataclass(frozen=True)
class DUATemplateBlock:
    """Represents a block in the DUA template."""

    block_id: str
    section_name: str
    field_type: str  # "text", "table", "code", "conditional"
    expected_field_type: Optional[str] = None
    validation_rules: Optional[dict] = None
    rendering_type: Optional[str] = None
