from datetime import datetime
from pydantic import BaseModel

class UserBehaviorRecord(BaseModel):
    user_id: str
    card_number: str
    last_transaction_timestamp: datetime
    last_amount: float
    last_country: str
    last_latitude: float
    last_longitude: float
    total_txn_60d: int
    total_decline_60d: int
    avg_amount_60d: float
    max_amount_60d: float
    min_amount_60d: float
