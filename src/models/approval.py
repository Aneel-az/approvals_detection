from typing import List

from pydantic import BaseModel


class Approval(BaseModel):
    token_name: str
    amount: int


class Approvals(BaseModel):
    approvals: List[Approval]
