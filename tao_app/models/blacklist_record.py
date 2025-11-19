from pydantic import BaseModel

class BlacklistRecord(BaseModel):
    user_id: str | None = None
    card_number: str | None = None
    ip_address: str | None = None
    reason: str | None = None
    source: str | None = None
