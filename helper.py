import logging
logger = logging.getLogger(__name__)
#(the __name__ will create a logger with the name of the module i.e helper)

logger.info("hello from helper")

#by default the logger propagates to the base logger, forming an heirrachy of oggers, you can set propagation to false and prevent this. if you then run the code in logging__py.py, it wont print out anything even if you had imported logger

#