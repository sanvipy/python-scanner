import logging
from time import strftime,gmtime

class LogHelper:

    @staticmethod
    def createlogger():
        filen = "scan-%s.log" % (strftime("%Y%m%d%H%S"))
        formatter = logging.Formatter('%(levelname)s %(message)s')
        handler = logging.FileHandler('reports/%s' %filen)
        handler.setFormatter(formatter)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)

        #Log into console
        #logger.addHandler(logging.StreamHandler())

        print 'Logging into reports/'+filen
        return logger        
