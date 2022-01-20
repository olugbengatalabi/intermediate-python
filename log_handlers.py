##handler objects are responsible for dispatching the appropiate log messages to the handler's specific destination

import logging

logger = logging.getLogger(__name__)

#to create your handler
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler("file.log")

#set the level and format
stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)
## the file_handler will only log messages of level Error.

formatter = logging.Formatter("%(name)s -%(levelname)s - %(message)s")
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

#to add the handlers you just created to the logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

#setting error and warning messages will work because 
logger.warning("this is a warning")
logger.error("this is an error")


##? go back to the video on file config when you have internet. 2:32