import time, logging
from apscheduler.schedulers.background import BackgroundScheduler
logger=logging.getLogger(__name__)

class SchedulerRunner:
    def __init__(self,pipeline_service):
        self.pipeline=pipeline_service
        self.sch=BackgroundScheduler()
    def start(self):
        self.pipeline.run_pipeline()
        self.sch.add_job(self.pipeline.run_pipeline,'interval',minutes=10)
        self.sch.start()
        try:
            while True:
                time.sleep(2)
        except:
            self.sch.shutdown()
