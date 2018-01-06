from enum import Enum


class ResponseTypeDuplicateName(Enum):
    SUCCESS = 0
    LICENSE_NOT_VALID = 100
    LICENSE_EXPIRED = 101
    INPUT_DATA_INVALID = 200
    INPUT_DATA_INVALID = 201


print(ResponseTypeDuplicateName.INPUT_DATA_INVALID)
