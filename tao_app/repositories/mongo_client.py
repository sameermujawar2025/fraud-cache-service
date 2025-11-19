from pymongo import MongoClient
from tao_app.config.settings import settings

class MongoClientFactory:
    @staticmethod
    def create_client():
        return MongoClient(settings.mongo_uri)
