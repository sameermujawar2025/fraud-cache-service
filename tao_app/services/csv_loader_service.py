import pandas as pd
from dateutil.parser import isoparse
import logging
from tao_app.models.transaction_record import TransactionRecord
from tao_app.models.blacklist_record import BlacklistRecord
from tao_app.utils.normalizers import normalize_card_number

logger=logging.getLogger(__name__)

class CsvLoaderService:
    def load_transactions(self, path):
        df=pd.read_csv(path)
        out=[]
        for _,r in df.iterrows():
            try:
                out.append(TransactionRecord(
                    transaction_id=r["transaction_id"],
                    user_id=r["user_id"],
                    card_number = normalize_card_number(r["card_number"]),
                    amount=r["amount"],
                    txn_status=r["txn_status"],
                    timestamp=isoparse(str(r["timestamp"])),
                    ip_address=r["ip_address"],
                    current_latitude=r["current_latitude"],
                    current_longitude=r["current_longitude"],
                    current_country=r["current_country"]
                ))
            except Exception as e:
                logger.warning("Bad row: %s", e)
        return out

    def load_blacklist(self, path):
        df=pd.read_csv(path)
        return [BlacklistRecord(**r.to_dict()) for _,r in df.iterrows()]
