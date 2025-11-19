from datetime import datetime
from pydantic import BaseModel

class TransactionRecord(BaseModel):
    transaction_id: str
    user_id: str
    card_number: str
    amount: float
    txn_status: str
    timestamp: datetime
    ip_address: str
    current_latitude: float
    current_longitude: float
    current_country: str
