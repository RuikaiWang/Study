import requests
import json
import time
import base64


def do(Authorization, userId):
    def stxx():
        # 试听学习
        headers = {
            'Authorization': Authorization,
            'sUserId': userId,
            'User-Agent': 'san jin xian feng/3.2.6 (iPhone; iOS 13.4.1; Scale/3.00)',
            'Content-Type': 'application/json',
            'Host': '221.204.170.88:8184',
            'Accept-Language': 'zh-Hans-CN;q=1, ko-KR;q=0.9, en-US;q=0.8',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*'
        }
        endtime = int(time.time())
        starttime = endtime - 700
        stData = {"appEndTime": endtime, "appStartTime": starttime, "type": "2", "time": "700", "articleId": "12"}
        stRsponse = requests.post(
            url='http://221.204.170.88:8184/app/personalCenter/articleTime?type=2&time=700&articleId=12&appStartTime=' + str(
                starttime),
            json=stData, headers=headers)
        print("试听学习====================" + stRsponse.text)

    def dati(str):
        url = 'http://221.204.170.88:8184/app/questionLib'
        pageData = {"page": 1, "pageSize": 10, "themeId": str}
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '37',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Authorization': Authorization,
            'Origin': 'http://sxzhdjkhd.sxdygbjy.gov.cn:8081',
            'User-Agent': 'Mozilla/5.0',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Referer': 'http://sxzhdjkhd.sxdygbjy.gov.cn:8081/zhdj-pre/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,en-US;q=0.9',
            'X-Requested-With': 'io.dcloud.H5B1841EE'
        }
        answerList = []
        response = requests.post(url, json=pageData, headers=headers)
        list = json.loads(response.text)
        for data in list['data']['list']:
            answerList.append({"selectAnswer": data['correctAnswer'], "grade": data['grade'], "ifCorrect": 1,
                               "questionCode": data['code'], "questionType": data['type']})
        uuidHeaders = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Authorization': Authorization,
            'Origin': 'http://sxzhdjkhd.sxdygbjy.gov.cn:8081',
            'User-Agent': 'Mozilla/5.0',
            'Accept': '*/*',
            'Referer': 'http://sxzhdjkhd.sxdygbjy.gov.cn:8081/zhdj-pre/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,en-US;q=0.9',
            'X-Requested-With': 'io.dcloud.H5B1841EE'
        }
        uuidResponse = requests.get("http://221.204.170.88:8184/app/uuid", headers=uuidHeaders).text
        uuidData = json.loads(uuidResponse)
        uuid = '"' + uuidData['data'] + '"'
        answer = {"userId": userId, "method": str, "totalGrade": "100", "list": answerList, "summaryCode": uuid}
        answerHeaders = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Authorization': Authorization,
            'Origin': 'http://sxzhdjkhd.sxdygbjy.gov.cn:8081',
            'User-Agent': 'Mozilla/5.0',
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'Referer': 'http://sxzhdjkhd.sxdygbjy.gov.cn:8081/zhdj-pre/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,en-US;q=0.9',
            'X-Requested-With': 'io.dcloud.H5B1841EE'
        }
        dumps = json.dumps(answer)
        print(dumps)
        answerResponse = requests.post("http://221.204.170.88:8184/app/question", data=dumps, headers=answerHeaders)
        print(answerResponse.text)
        print("完成答题" + str + answerResponse.text)

    def scwz():
        Headers = {
            'Authorization': Authorization,
            'User-Agent': 'san jin xian feng/3.2.6 (iPhone; iOS 13.4.1; Scale/3.00)',
            'Accept-Language': 'zh-Hans-CN;q=1, ko-KR;q=0.9, en-US;q=0.8',
            'sUserId': userId,
        }
        # 取消点赞
        articleList = \
            json.loads(requests.get("http://221.204.170.88:8184/app/study/list_article/72?size=10&page=1").text)[
                "data"]
        unlovedata1 = {"type": "1", "userId": userId, "uniqueId": articleList[0]["id"]}
        unlove1Response = requests.post("http://221.204.170.88:8184/app/loveCancelDelete", json=unlovedata1,
                                        headers=Headers)
        print(unlove1Response.text)
        unlovedata2 = {"type": "1", "userId": userId, "uniqueId": articleList[1]["id"]}
        unlove2Response = requests.post("http://221.204.170.88:8184/app/loveCancelDelete", json=unlovedata2,
                                        headers=Headers)
        print(unlove2Response.text)
        # 取消收藏
        uncollect1Response = requests.post("http://221.204.170.88:8184/app/collectCancelDelete", json=unlovedata1,
                                           headers=Headers)
        print(uncollect1Response.text)
        uncollect2Response = requests.post("http://221.204.170.88:8184/app/collectCancelDelete", json=unlovedata2,
                                           headers=Headers)
        print(uncollect2Response.text)
        headers = {
            'Authorization': Authorization,
            'User-Agent': 'okhttp/3.8.0',
            'Content-Type': 'application/json',
            'Host': '221.204.170.88:8184',
            'sUserId': userId,
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip'
        }
        collectresponse1 = requests.post('http://221.204.170.88:8184/app/collect', json=unlovedata1, headers=headers)
        print(collectresponse1.text)
        collectresponse2 = requests.post('http://221.204.170.88:8184/app/collect', json=unlovedata2, headers=headers)
        print(collectresponse2.text)
        dzRsponse = requests.post(url='http://221.204.170.88:8184/app/love', json=unlovedata1, headers=headers)
        print(dzRsponse.text)
        dzRsponse = requests.post(url='http://221.204.170.88:8184/app/love', json=unlovedata2, headers=headers)
        print(dzRsponse.text)

    def yd():
        headers = {
            'Authorization': Authorization,
            'User-Agent': 'san jin xian feng/3.2.6 (iPhone; iOS 13.4.1; Scale/3.00)',
            'Content-Type': 'application/json',
            'Host': '221.204.170.88:8184',
            'sUserId': userId,
            'Accept-Language': 'zh-Hans-CN;q=1, ko-KR;q=0.9, en-US;q=0.8',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*'
        }
        endtime = int(time.time())
        starttime = endtime - 60
        stData = {"appEndTime": endtime, "appStartTime": starttime, "type": "1", "time": "60", "articleId": "4"}
        stRsponse = requests.post(
            url='http://221.204.170.88:8184/app/personalCenter/articleTime?type=2&time=60&articleId=12&appStartTime=' + str(
                starttime), json=stData, headers=headers)
        print(stRsponse.text)

    # 答题
    dati("1")
    dati("1")
    dati("4")
    dati("4")
    # 试听学习
    stxx()
    stxx()
    # 收藏点赞
    scwz()
    # 阅读
    yd()
    yd()


def login(username, password):
    url = 'http://221.204.170.88:8184/app/user/login'
    data = {"password": password, "deviceId": "5D2723AE-D386-48C3-AC49-586260EE7E79", "clientid": "236236",
            "userName": username}
    headers = {
        'Content-Type': 'application/json',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'User-Agent': 'san jin xian feng/3.2.6 (iPhone; iOS 13.4.1; Scale/3.00)',
        'Accept-Language': 'zh-Hans-US;q=1, en-US;q=0.9',
        'Content-Length': '119',
        'Accept-Encoding': 'gzip, deflate',
    }
    response = requests.post(url, json=data, headers=headers)
    userInfo = json.loads(response.text)['data']
    info = json.loads(base64.b64decode(userInfo))
    return [info['jwtToken'], info['id']]


def sjxx(username, password):
    JWT = login(username, password)
    do('Bearer ' + str(JWT[0]), str(JWT[1]))


sjxx("username", "password")
