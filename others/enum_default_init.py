from enum import Enum

class ResponseDefinition(Enum):
    SUCCESS = (0, 'query success')
    INPUT_PARAMS_NOT_VALID = (201, 'input parameters not valid')
    INTERNAL_ERROR = (502, 'system error')

    def __init__(self, code, message):
        self.code = code
        self.message = message



if __name__ == '__main__':
  print('success code: {}, message: {}'.format(ResponseDefinition.SUCCESS.code, ResponseDefinition.SUCCESS.message))
