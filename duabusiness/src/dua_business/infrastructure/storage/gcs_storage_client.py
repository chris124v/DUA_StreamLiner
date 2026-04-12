from dua_business.application.ports.storage_port import StoragePort

class GCSStorageAdapter(StoragePort):
    def upload_file(self, path: str, content: bytes) -> str:
        _ = path
        _ = content
        raise NotImplementedError("Contract only")

