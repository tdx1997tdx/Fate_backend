import json
import requests

def name_search_test1():
    url = "https://dararara.xyz/name_search"
    values = {'name':'亚瑟'}
    print('请求：',values)
    values_json = json.dumps(values)
    # requests库提交数据进行post请求
    req = requests.post(url, data=values_json)
    # 打印Unicode编码格式的json数据
    # 使用json.dumps()时需要对象相应的类型是json可序列化的
    change = req.json()
    # json.dumps序列化时对中文默认使用ASCII编码,如果无任何配置则打印的均为ascii字符,输出中文需要指定ensure_ascii=False
    new_req = json.dumps(change, ensure_ascii=False)
    # 打印接口返回的数据,且以中文编码
    print('响应：',new_req)

def name_search_test2():
    url = "https://dararara.xyz/servent_infomation"
    values = {'servent_id':'160'}
    print('请求：',values)
    values_json = json.dumps(values)
    # requests库提交数据进行post请求
    req = requests.post(url, data=values_json)
    # 打印Unicode编码格式的json数据
    # 使用json.dumps()时需要对象相应的类型是json可序列化的
    change = req.json()
    # json.dumps序列化时对中文默认使用ASCII编码,如果无任何配置则打印的均为ascii字符,输出中文需要指定ensure_ascii=False
    new_req = json.dumps(change, ensure_ascii=False)
    # 打印接口返回的数据,且以中文编码
    print('响应：',new_req)

name_search_test2()