from enum import Enum, unique


class ResponseTypeAlias(Enum):
    SUCCESS = 0
    LICENSE_NOT_VALID = 100
    LICENSE_EXPIRED = 101
    INPUT_DATA_INVALID = 200
    JSON_DATA_INVALID = 200


# @unique
# class ResponseTypeUniqueName(Enum):
#     SUCCESS = 0
#     LICENSE_NOT_VALID = 100
#     LICENSE_EXPIRED = 101
#     INPUT_DATA_INVALID = 200
#     JSON_DATA_INVALID = 200

print(ResponseTypeAlias.INPUT_DATA_INVALID)
print(ResponseTypeAlias.JSON_DATA_INVALID)

for r in ResponseTypeAlias:
    print(r)

for name, member in ResponseTypeAlias.__members__.items():
    print('name:{}, member:{}'.format(name, member))
