import logging

class Logger(object):
    _instance = None
    _logger = None
    _level = logging.INFO

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)

            cls._logger = logging.getLogger("main")
            cls._logger.setLevel(cls._level)
            ch = logging.StreamHandler()
            ch.setLevel(cls._level)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            ch.setFormatter(formatter)
            cls._logger.addHandler(ch)  

        return cls._instance

    @classmethod
    def setDebug(cls):
        cls._level = logging.DEBUG
        cls._logger.setLevel(cls._level)

    def debug(self, _msg):
        self._logger.debug(_msg)

    def info(self, _msg):
        self._logger.info(_msg)

    def warn(self, _msg):
        self._logger.warn(_msg)

    def error(self, _msg):
        self._logger.error(_msg)