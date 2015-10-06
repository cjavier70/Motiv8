__author__ = 'cameronjavier'
import logging

class AppFilter(logging.Filter):

    def __init__(self, whoFrom):
        self.whoFrom = whoFrom

    def filter(self, record):
        record.userId = self.whoFrom
        return True


def getLogger(whoFrom, stream):

    logger = logging.getLogger(__name__)
    logger.addFilter(AppFilter(whoFrom))
    syslog = logging.StreamHandler(stream)
    formatter = logging.Formatter('%(asctime)s %(userId)s : %(message)s')
    syslog.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(syslog)
    # logging.basicConfig(filename="/var/www/motiv8/log/output.log",
    #                     level=logging.DEBUG,
    #                     datefmt='%a, %d %b %Y %H:%M:%S')
    return logger






