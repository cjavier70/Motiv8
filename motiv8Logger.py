__author__ = 'cameronjavier'
import logging

class CustomAdapter(logging.LoggerAdapter):
    """
    This example adapter expects the passed in dict-like object to have a
    'connid' key, whose value in brackets is prepended to the log message.
    """
    def process(self, msg, kwargs):
        return '[%s] %s' % (self.extra['connid'], msg), kwargs

class init():
    def __init__(self, whoFrom):
        logging.basicConfig(filename="/var/www/motiv8/log/output.log",
                            level=logging.DEBUG,
                            format='%(asctime)s : %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S')
        logger = logging.getLogger(__name__)
        # logger.addFilter(AppFilter(whoFrom))

        # syslog = logging.StreamHandler(stream)
        # formatter = logging.Formatter('%(asctime)s %(userId)s : %(message)s')
        # syslog.setFormatter(formatter)
        # logger.addHandler(syslog)

        # logger.info = lambda msg: logger.info(msg, extra={'userId': whoFrom})
        # logger.debug = lambda msg: logger.debug(msg, extra={'userId': whoFrom})
        # logger.warning = lambda msg: logger.warning(msg, extra={'userId': whoFrom})
        global adapter
        adapter = CustomAdapter(logger, {'connid': whoFrom})
