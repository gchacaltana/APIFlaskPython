# -*- coding: utf-8 -*-
# author: Gonzalo Chacaltana @gchacaltanab


#Clase ErrorMessage
class ErrorMessage(object):

    def __init__(self):
        pass

    @staticmethod
    def printError(error_code, error_message):
        return {'error_code': error_code, 'message': error_message}

