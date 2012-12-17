# Petr Kolacek, xkolac11@stud.fit.vutbr.cz

import logging

"""
@param Path to save logging.
@return Inicialized logging
"""
def initLog(path):
	LOG_FILENAME = path
	logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG,)
	return logging