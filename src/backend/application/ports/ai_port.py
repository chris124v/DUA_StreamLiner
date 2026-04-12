"""Port for AI/ML services (Vertex AI, Gemini)."""

from typing import Protocol, list


class AIPort(Protocol):
    """Protocol for AI/ML operations."""

    async def classify_text(self, text: str, categories: list[str]) -> dict:
        """Classify text into categories.

        Args:
            text: Text to classify
            categories: List of possible categories

        Returns:
            Dictionary with category probabilities
        """
        ...

    async def extract_fields(self, text: str, field_schema: dict) -> dict:
        """Extract structured fields from text.

        Args:
            text: Text to extract from
            field_schema: Schema defining fields to extract

        Returns:
            Extracted fields dictionary
        """
        ...

    async def generate_embedding(self, text: str) -> list[float]:
        """Generate embedding vector for text.

        Args:
            text: Text to embed

        Returns:
            Embedding vector as list of floats
        """
        ...

    async def calculate_similarity(
        self, embedding1: list[float], embedding2: list[float]
    ) -> float:
        """Calculate similarity between two embeddings.

        Args:
            embedding1: First embedding vector
            embedding2: Second embedding vector

        Returns:
            Similarity score (0-1)
        """
        ...

    async def perform_semantic_search(
        self, query_embedding: list[float], candidates: list[dict], top_k: int = 2
    ) -> list[dict]:
        """Perform semantic search against candidate embeddings.

        Args:
            query_embedding: Query embedding vector
            candidates: List of candidate objects with embeddings
            top_k: Number of results to return

        Returns:
            Top K matching candidates
        """
        ...
