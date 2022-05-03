# Page306
from aip import AipOcr
import os

# 百度智能云识别车牌
filename = '../file/key.txt'
if os.path.exists(filename):
    with open(filename, 'r') as file:
        dictkey = eval(file.readlines()[0])
        App_ID = dictkey['App_ID']
        API_Key = dictkey['API_Key']
        Secret_Key = dictkey['Secret_Key']
else:
    print('Key.txt不存在')
client = AipOcr(App_ID, API_Key, Secret_Key)


def get_file_content(filepath):
    with open(filepath, 'rb') as fp:
        return fp.read()


def get_car_number():
    image = get_file_content('../file/test.png')
    # 调用车牌识别并从返回信息中只获取number字段
    result = client.licensePlate(image)['words_result']['number']
    print(result)
    return result
