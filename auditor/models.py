from dataclasses import dataclass
from enum import Enum


class Severity(Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


@dataclass
class Finding:
    file: str
    line: int
    severity: Severity
    category: str
    message: str
    snippet: str
    owasp_id: str | None = None
