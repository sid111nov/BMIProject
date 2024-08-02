import logging
import datetime
import os
from logging.handlers import RotatingFileHandler

LOG_FILE=f"Log_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
LOG_PATH='logs'

LOG_FILE_PATH = os.path.join(LOG_PATH)
os.makedirs(LOG_FILE_PATH,exist_ok=True)
LOG_FILE_LOC = os.path.join(LOG_FILE_PATH,LOG_FILE)

handler = RotatingFileHandler(LOG_FILE_LOC,maxBytes=1024*5*1024,backupCount=10)
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


logger.info("Intiating Logs................")

