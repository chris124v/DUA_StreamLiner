from typing import Protocol

from dua_business.domain.entities.dua_generation import DUAGeneration


class GenerationRepository(Protocol):
    def get_by_id(self, generation_id: str) -> DUAGeneration | None: ...

    def save(self, generation: DUAGeneration) -> None: ...
