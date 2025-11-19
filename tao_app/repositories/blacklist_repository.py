from pymongo import ASCENDING

class BlacklistRepository:
    COLLECTION_NAME="blacklist"
    def __init__(self, client, db_name):
        self.col = client[db_name][self.COLLECTION_NAME]
    def ensure_indexes(self):
        self.col.create_index([("user_id",ASCENDING)])
    def replace_blacklist(self, docs):
        self.col.delete_many({})
        if docs:
            self.col.insert_many([d.model_dump() for d in docs])
