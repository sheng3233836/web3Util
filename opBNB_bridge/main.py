from sys import stderr
from bridge_main import deposit,transfer
from loguru import logger

logger.remove()
logger.add(stderr, format="<white>{time:HH:mm:ss}</white> | <level>{level: <3}</level> | <level>{message}</level>")

if __name__ == '__main__':
    # deposit()
    transfer()