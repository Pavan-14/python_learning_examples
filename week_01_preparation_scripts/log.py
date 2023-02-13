import logging

# custom logger
logger = logging.getLogger(__name__)

# create handlers
c_handler = logging.StreamHandler()
i_handler = logging.StreamHandler()
f_handler = logging.FileHandler(r"E:\Pavan Learnings\Braineest\week_01_preparation_scripts\filelog.log")
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)
i_handler.setLevel(logging.INFO)


# create formatters and add it to handlers
c_format = logging.Formatter("%(process)d - %(levelname)s - %(message)s")
f_format = logging.Formatter("%(asctime)s - %(process)d - %(levelname)s - %(message)s")
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)
i_handler.setFormatter(c_format)


# add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)
logger.addHandler(i_handler)