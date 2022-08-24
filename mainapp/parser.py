import requests
import xmltodict
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def placeParsing():
    area = "서울"
    key = '4dyWzA6P86MqeODeWSta%2FGWsVhhhGnt66S3voAAXhcnXgldM3gqVOgur7RO6yDvALtfM%2B0RfkoMt52QPQbmTCw%3D%3D'
    url = 'https://apis.data.go.kr/B552735/workspaceErumService/getAreaCenterList?serviceKey='+key+'&area='+ area

    req = requests.get(url, verify=False).content 

    xmlObject = xmltodict.parse(req)
    allData = xmlObject['items']['item']

    # print(allData)
    return allData

    

