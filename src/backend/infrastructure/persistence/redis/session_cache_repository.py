from dua_business.application.ports.cache_port import CachePort

class RedisCacheAdapter(CachePort):
    def get(self, key: str) -> str | None:
        _ = key
        raise NotImplementedError("Contract only")

    def set(self, key: str, value: str) -> None:
        _ = key
        _ = value
        raise NotImplementedError("Contract only")

    def delete(self, key: str) -> None:
        _ = key
        raise NotImplementedError("Contract only")

