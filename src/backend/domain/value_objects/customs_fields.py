"""Value object for customs fields and domain-specific entities."""

from dataclasses import dataclass
from typing import Optional
from datetime import date


@dataclass(frozen=True)
class ImporterExporterData:
    """Represents importer or exporter identification data."""

    name: str
    identification_number: str
    country: str
    address: Optional[str] = None
    phone: Optional[str] = None


@dataclass(frozen=True)
class SupplierInfo:
    """Represents supplier information."""

    name: str
    country: str
    contact: Optional[str] = None


@dataclass(frozen=True)
class GoodsDescription:
    """Represents product/goods information."""

    commercial_description: str
    tariff_code: Optional[str] = None
    quantity: Optional[float] = None
    unit_of_measure: Optional[str] = None
    weight: Optional[float] = None
    fob_value: Optional[float] = None
    cif_value: Optional[float] = None
    currency: Optional[str] = None


@dataclass(frozen=True)
class TransportInfo:
    """Represents transport-related information."""

    transport_mode: str  # maritime, air, land
    transport_document_number: Optional[str] = None
    carrier_name: Optional[str] = None
    port_of_loading: Optional[str] = None
    port_of_discharge: Optional[str] = None
    incoterms: Optional[str] = None


@dataclass(frozen=True)
class InvoiceDetails:
    """Represents invoice information."""

    invoice_number: str
    invoice_date: date
    reference_number: Optional[str] = None


@dataclass(frozen=True)
class CustomsRegimeInfo:
    """Represents customs regime and country of origin."""

    country_of_origin: str
    customs_regime: str
    certificate_of_origin: Optional[str] = None
