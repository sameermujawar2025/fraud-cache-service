from pymongo import ASCENDING
import logging

logger=logging.getLogger(__name__)

class TransactionRepository:
    COLLECTION_NAME="transactions_last_1_hour"
    def __init__(self, client, db_name):
        self.col = client[db_name][self.COLLECTION_NAME]
    def ensure_indexes(self, ttl_seconds):
        self.col.create_index([("timestamp",ASCENDING)], expireAfterSeconds=ttl_seconds)
    def replace_last_hour_transactions(self, txns):
        self.col.delete_many({})
        if txns:
            self.col.insert_many([t.model_dump() for t in txns])
