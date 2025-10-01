import logging

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(filename="example.log", level=logging.DEBUG, format = FORMAT)
logging.info("Hi this is my first log")
logging.debug("Hi this is my third log")
logging.error("Hi this is my second log")
logging.warning("Hi this is my fourth log")