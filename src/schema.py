import json
from typing import List, Optional

from pydantic import BaseModel, HttpUrl, field_validator


class Evidence(BaseModel):
    title: str
    url: Optional[HttpUrl] = None


class FraudGuardResult(BaseModel):
    rating: str
    score: float
    reasons: List[str]
    evidence: Optional[List[Evidence]] = []
    disclaimer: str

    @field_validator("disclaimer", mode="before")
    @classmethod
    def unwrap_disclaimer_if_json(cls, v, values):
        if isinstance(v, str):
            try:
                nested = json.loads(v)  # try parsing
                if isinstance(nested, dict):
                    # overwrite outer fields with the parsed JSON
                    values.update(nested)
                    return nested.get("disclaimer", "")
            except json.JSONDecodeError:
                pass
        return v


class QueryIn(BaseModel):
    query: str
