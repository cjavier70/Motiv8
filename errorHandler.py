__author__ = 'cameronjavier'
import sys
# from motiv8Logger import getLogger
from flask import request
logDescriptor = open('/var/www/motiv8/log/output.log', 'a+w', 0)

#TODO
def printAndExit(str):
    # logger = getLogger(request.headers.get('From'), logDescriptor)
    # logger.Error(str)
    exit()