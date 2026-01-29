from pydantic import BaseModel
from typing import List

class Transaction(BaseModel):
    customer_id: str
    total_amount: float
    country: str
    transaction_date: str

class TransactionsRequest(BaseModel):
    records: List[Transaction]
