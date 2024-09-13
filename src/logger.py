import logging 
import os 
from datetime import datetime 

LOG_FILE=f'{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log'
logs_dirs=os.path.join(os.getcwd(),"logs",LOG_FILE)

os.makedirs(logs_dirs,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_dirs,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(lineno)d - %(message)s',
    level=logging.info,
    
)