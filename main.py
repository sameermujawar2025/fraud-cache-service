from tao_app.core.logging_config import configure_logging
from tao_app.services.pipeline_service import PipelineService
from tao_app.services.csv_loader_service import CsvLoaderService
from tao_app.repositories.transaction_repository import TransactionRepository
from tao_app.repositories.user_behavior_repository import UserBehaviorRepository
from tao_app.repositories.blacklist_repository import BlacklistRepository
from tao_app.repositories.mongo_client import MongoClientFactory
from tao_app.scheduler.scheduler_runner import SchedulerRunner
from tao_app.config.settings import settings
import argparse

def build_pipeline_service():
    mongo = MongoClientFactory.create_client()
    txn_repo = TransactionRepository(mongo, settings.mongo_db_name)
    beh_repo = UserBehaviorRepository(mongo, settings.mongo_db_name)
    bl_repo = BlacklistRepository(mongo, settings.mongo_db_name)
    loader = CsvLoaderService()
    return PipelineService(loader, txn_repo, beh_repo, bl_repo, settings)

def main():
    configure_logging()
    parser=argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["once","schedule"], default="once")
    args=parser.parse_args()
    service=build_pipeline_service()
    if args.mode=="once":
        service.run_pipeline()
    else:
        SchedulerRunner(service).start()

if __name__=="__main__":
    main()
