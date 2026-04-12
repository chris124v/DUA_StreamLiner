from dua_business.application.ports.ocr_port import OCRPort

class DocumentAIAdapter(OCRPort):
    def extract(self, file_uri: str) -> dict:
        _ = file_uri
        raise NotImplementedError("Contract only")

