import logging
#by default only debug levels of arnign and above are printed but to change that.
logging.basicConfig(level = logging.DEBUG, format='%(asctime)s - %(name)s -%(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
#you can log to 5 debug levels which indicate the severity of the event

# logging.debug("This is a debug message")
# logging.info("This is a info message")
# logging.warning("This is a warning message")
# logging.error("This is a error message")
# logging.critical("This is a critical message")

'''
its best practice not to use the root logger but to create your own logger in your module (run the code to see the printed result and see root)'''

'''
best practice is to create your own logger in your modules, for exmple the helper.py file and import it'''
import helper