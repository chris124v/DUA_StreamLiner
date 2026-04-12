from dataclasses import dataclass


@dataclass
class DUAGeneration:
    generation_id: str
    status: str
    current_step: int
    progress_percent: int
