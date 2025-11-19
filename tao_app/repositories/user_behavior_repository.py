from pymongo import ASCENDING
import logging
logger=logging.getLogger(__name__)

class UserBehaviorRepository:
    COLLECTION_NAME="user_behavior_60_days"
    def __init__(self, client, db_name):
        self.col = client[db_name][self.COLLECTION_NAME]
    def ensure_indexes(self):
        self.col.create_index([("user_id",ASCENDING),("card_number",ASCENDING)], unique=True)
    def replace_behavior(self, docs):
        self.col.delete_many({})
        if docs:
            self.col.insert_many([d.model_dump() for d in docs])
