
# DELPHINUS - ADVENTURE APP
# CS 467 - Winter 2017
# Team Members: Sara Hashem:, Shawn Hillyer, Niza Volair
#
# debug.py
# Description: Debug tool setup (logging module)
# Principal Author of this file per Project plan: Shawn Hillyer
#
# CITATIONS
# CITE: http://stackoverflow.com/questions/6579496/using-print-statements-only-to-debug
# CITE: http://docs.python-guide.org/en/latest/writing/logging/
# CITE: http://stackoverflow.com/questions/7083249/conditional-logging-in-python


# Use the following code in a file to use debug logging:
#
# from debug.debug import *
# logger = logging.getLogger(__name__)
#
# [ ... ]
#
# logger.debug("This will print stuff as a debug message")


import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)