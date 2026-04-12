from dua_business.application.ports.ai_port import AIPort

class VertexAIAdapter(AIPort):
    def classify(self, text: str) -> dict:
        _ = text
        raise NotImplementedError("Contract only")

