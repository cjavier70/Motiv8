__author__ = 'cameronjavier'
import sys
sys.stdout=open('/var/www/motiv8/log/output.log', 'a+w', 0)

def printAndReturn(str):
    print(str)
    return str