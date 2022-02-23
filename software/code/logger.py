import logging

class Logger(object):
    _instance = None
    _logger = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Logger, cls).__new__(cls)
            
            cls._logger = logging.getLogger("main")
            cls._logger.setLevel(logging.INFO)
            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            ch.setFormatter(formatter)
            cls._logger.addHandler(ch)  

        return cls._instance

    def debug(self, _msg):
        self._logger.debug(_msg)

    def info(self, _msg):
        self._logger.info(_msg)

    def warn(self, _msg):
        self._logger.warn(_msg)

    def error(self, _msg):
        self._logger.error(_msg)