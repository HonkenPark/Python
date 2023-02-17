import requests
import json
import webbrowser
from selenium import webdriver

print("*****************************************************************************")
print("이 프로그램은 본방 사수를 하지 못하고 녹방을 네이버 스포츠에서 다시보기를 할 때")
print("본의가 아니게 결과를 스포당해 경기를 감상하는데 방해가 되는 상황을 없애고자")
print("제작된 단순 링크 탐지용 프로그램 입니다.")
print("*****************************************************************************")
print("")
print("")

def askType():
    ret = input('대회의 타입을 알려주세요. (1: LCK, 2: Worlds): ')
    while 1:
        if int(ret) == 1:
            print("LCK를 선택하셨습니다.")
            break
        elif int(ret) == 2:
            print("Worlds를 선택하셨습니다.")
            break
        else:
            print("1번과 2번중에서 선택하세요.")
            ret = input('대회의 타입을 알려주세요. (1: LCK, 2: Worlds): ')
            continue
    return int(ret);

def askTeam1():
    ret = input('1-1. 시청을 원하시는 팀명을 적으세요.(ex.T1)): ')
    while 1:
        if ret.isalnum():
            break
        else:
            print("팀명을 잘못 적으셨습니다. 다시 입력해주세요.")
    return ret

def askTeam2():
    ret = input('1-2. 나머지 팀명도 적으세요.(ex.GEN)): ')
    while 1:
        if ret.isalnum():
            break
        else:
            print("팀명을 잘못 적으셨습니다. 다시 입력해주세요.")
    return ret

def askSet():
    ret = input('몇 세트의 경기를 보실 것인지 숫자만 적으세요.(ex.1) ')
    while 1:
        if int(ret) < 1:
            print("세트를 잘못 입력하셨습니다. 1~5 사이의 숫자를 입력해주세요.")
            continue
        elif int(ret) > 5:
            print("세트를 잘못 입력하셨습니다. 1~5 사이의 숫자를 입력해주세요.")
            ret = input('몇 세트의 경기를 보실 것인지 숫자만 적으세요.(ex.1) ')
            continue
        else:
            break
    return ret + "세트"

def askDate():
    ret = input('경기가 치뤄진 날짜를 적으세요.(ex.202206 or 20220618) ')
    while 1:
        if ret.isdigit():
            break
        else:
            print("날짜를 잘못 적으셨습니다. 숫자로만 입력해주세요.")
            ret = input('경기가 치뤄진 날짜를 적으세요.(ex.202206 or 20220618) ')
            continue
    return str(ret)

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

leagueType = askType()
# print("leagueType: ", leagueType);
if leagueType == 1:
    listUrl = "https://game.naver.com/esports/videos/league/lck" # LCK
else:
    listUrl = "https://game.naver.com/esports/videos/league/world_championship"; # Worlds

preDel = "{\"props\":{"
postDel = "\"appGip\":true}"
jsonPath = "videoList.js"
finalUrl = "https://game.naver.com/esports/League_of_Legends/videos/"
findResult = False

response = requests.get(listUrl).text
preIdx = response.find(preDel)
postIdx = response.rfind(postDel)
jsonText = response[preIdx:postIdx]
jsonText += postDel
# with open(jsonPath, "w", encoding="utf8") as jsonParce: 
# 	jsonParce.write(response)
 
# with open(jsonPath, "r") as json_file:
#     json_data = json.load(json_file)
#     print(json_data['popularVideo'])

jsonObj = json.loads(jsonText)
# print(jsonText)
popularList = jsonObj['props']['initialState']['video']['perTopLeagueVideo']['content']

matchTeam1 = askTeam1()
matchTeam2 = askTeam2()
if leagueType == 1:
    matchSet = askSet() # LCK용 (ex. T1-NS 1세트)
matchDate = askDate()

print("")
print("해당 정보로 검색을 시작합니다.")
print("==============================================")
if leagueType == 1:
    print(matchTeam1 + " VS " + matchTeam2 + " " + matchSet + " (" + matchDate + ")")
else:
    print(matchTeam1 + " VS " + matchTeam2 + " " + " (" + matchDate + ")")
print("==============================================")
for item in popularList:
    if matchTeam1 in item['title']:
        if matchTeam2 in item['title']:
            if matchSet in item['title']:
                if matchDate in item['gameId']:
                    finalUrl += str(item['id'])
                    findResult = True
                    break


if findResult == True:
    # options = webdriver.ChromeOptions()
    # options.add_argument('start-maximized')
    # driver = webdriver.Chrome('chromedriver.exe', options=options)
    # driver.get(finalUrl)
    print(finalUrl)
    webbrowser.open(finalUrl)
else:
    print("!!!!!!!!!!! 검색 결과가 없습니다. !!!!!!!!!!!")

# print(element)
# driver.quit()

# options.add_argument('headless')
# options.add_argument('start-maximized')
# driver = webdriver.Chrome('chromedriver.exe', options=options)
