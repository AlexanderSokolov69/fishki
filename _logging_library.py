import os
from loguru import logger
# Организация логгирования в программе


logger.add("file_{time}.log", format="{time} | {level} | <{name}> :{message}:", level="DEBUG", rotation="5 MB")

logger.debug("Test log")
print(os.listdir())
