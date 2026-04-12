from dataclasses import dataclass


@dataclass
class RequestContext:
    trace_id: str
    user_id: str | None = None
