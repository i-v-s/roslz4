from logging import getLogger
from .rostime import Time


logger = getLogger()


def logwarn(msg):
    logger.warning(msg)
