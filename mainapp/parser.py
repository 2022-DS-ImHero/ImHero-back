import encodings
import requests
import xmltodict
import time
import urllib3 
from urllib import parse
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

key = '4dyWzA6P86MqeODeWSta%2FGWsVhhhGnt66S3voAAXhcnXgldM3gqVOgur7RO6yDvALtfM%2B0RfkoMt52QPQbmTCw%3D%3D'

def placeParsing():
    area = "서울"
    
    url = 'https://apis.data.go.kr/B552735/workspaceErumService/getAreaCenterList?serviceKey='+key+'&area='+ area

    req = requests.get(url, verify=False).content 

    xmlObject = xmltodict.parse(req)
    allData = xmlObject['items']['item']

    # print(allData)
    return allData

def infoParsing():

    url = 'http://openapi.kised.or.kr/openapi/service/rest/ContentsService/getAnnouncementList'
    dkey  = requests.utils.unquote(key)
    numOfRows = '10'
    startPage = '1'
    pageSize = '10'
    pageNo = '1'
    url = 'http://openapi.kised.or.kr/openapi/service/rest/ContentsService/getNoticeList?serviceKey='+key+'&numOfRows='+numOfRows+'&startPage'+startPage+'&pageSize='+pageSize+'&pageNo='+pageNo
 
    
    # url = 'https://apis.data.go.kr/B552735/workspaceErumService/getAreaCenterList?serviceKey='+dkey+'&area='+ area

    req = requests.get(url, verify=False).content 

    xmlObject = xmltodict.parse(req)
    allData = xmlObject['response']

    print(allData)
    # return allData

    # queryParams = '?' + parse.urlencode({
    #     parse.quote_plus('ServiceKey') : key,
    #     parse.quote_plus('numOfRows') : '10',
    #     # parse.quote_plus('startPage') :'1',
    #     #parse.quote_plus('pageSize') : '10',
    #     parse.quote_plus('pageNo') : '1'
    # })
    # print((url + queryParams).find(key))
    #req = requests.get(url + queryParams, verify=False).content
#
    #xmlObject = xmltodict.parse(req)
    #allData = xmlObject['response']
#
    #print(allData)
    #url = 'http://openapi.kised.or.kr/openapi/service/rest/ContentsService/getAnnouncementList'
    #params ={'serviceKey' : key, 'pageNo' : '1', 'numOfRows' : '10', 'startDate' : '20200101', 'endDate' : '20200131' }
#
    #response = requests.get(url, params=params).content
    #xmlObject = xmltodict.parse(response)
    #print(xmlObject)

    #url = 'http://openapi.kised.or.kr/openapi/service/rest/ContentsService/getAnnouncementList'
    #dkey = '4dyWzA6P86MqeODeWSta/GWsVhhhGnt66S3voAAXhcnXgldM3gqVOgur7RO6yDvALtfM+0RfkoMt52QPQbmTCw=='
#
    
    #queryParams = f'?{parse.quote_plus("ServiceKey")}={dkey}&'+ parse.urlencode({
    #    parse.quote_plus('numOfRows') : '10',
    #    # parse.quote_plus('startPage') :'1',
    #    # parse.quote_plus('pageSize') : '10',
    #    parse.quote_plus('pageNo') : '1'
    #})
##
    #req = requests.get(url + queryParams, verify=False)
    #print(req.text)
    #print(req)
    #print((url+queryParams).find(key))
#
    #xmlObject = xmltodict.parse(req)
    #allData = xmlObject['response']
#
    #print(allData)
#
infoParsing()


    #dkey = requests.utils.unquote(key)
    #numOfRows = 10
    #startPage = 1
    #pageSize = 10
    #pageNo = 1
    #url = 'http://openapi.kised.or.kr/openapi/service/rest/ContentsService/getNoticeList?'+dkey+'&numOfRows='+numOfRows+'&startPage'+startPage+'&pageSize='+pageSize+'&pageNo='+pageNo
    #
    #req = requests.get(url, verify=False).content 
#
    #xmlObject = xmltodict.parse(req)
    #allData = xmlObject['items']['item']
#
    ## print(allData)
    #return allData
#
