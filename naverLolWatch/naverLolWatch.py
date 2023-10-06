import pyfiglet
import requests
import json
import webbrowser
from selenium import webdriver

print("*****************************************************************************")
result = pyfiglet.figlet_format("Naver Lol Watch")
print(result)
print("*****************************************************************************")
print("이 프로그램은 본방 사수를 하지 못하고 녹방을 네이버 스포츠에서 다시보기를 할 때")
print("본의가 아니게 결과를 스포당해 경기를 감상하는데 방해가 되는 상황을 없애고자")
print("제작된 단순 링크 탐지용 프로그램 입니다.")
print("*****************************************************************************")
print("")
print("")

def askType():
    while 1:
        ret = input('대회의 타입을 알려주세요. (1: LCK, 2: Worlds, 3: MSI): ')
        if str.isdigit(ret):
            if int(ret) == 1:
                print("LCK를 선택하셨습니다.")
                break
            elif int(ret) == 2:
                print("Worlds를 선택하셨습니다.")
                break
            elif int(ret) == 3:
                print("MSI를 선택하셨습니다.")
                break
            else:
                print("ERROR :: 1번~3번중에서 선택해주세요!!\n\n")
                continue
        else:
            print("ERROR :: 숫자를 입력해주세요!!\n\n")
            continue
    return int(ret);

def askTeam1():
    while 1:
        ret = input('1-1. 시청을 원하시는 팀명을 적으세요.(ex.T1)): ')
        if ret.isalnum():
            break
        else:
            print("ERROR :: 팀명을 잘못 적으셨습니다. 다시 입력해주세요!!\n\n")
    return ret

def askTeam2():
    while 1:
        ret = input('1-2. 나머지 팀명도 적으세요.(ex.GEN)): ')
        if ret.isalnum():
            break
        else:
            print("ERROR :: 팀명을 잘못 적으셨습니다. 다시 입력해주세요!!\n\n")
    return ret

def askSet():
    while 1:
        ret = input('몇 세트의 경기를 보실 것인지 숫자만 적으세요.(ex.1) ')
        if int(ret) < 1 or int(ret) > 5:
            print("ERROR :: 세트를 잘못 입력하셨습니다. 1~5 사이의 숫자를 입력해주세요.\n\n")
            continue
        else:
            break
    return ret + "세트"

def askDate():
    while 1:
        ret = input('경기가 치뤄진 날짜를 적으세요.(ex.202206 or 20220618): ')
        if ret.isdigit():
            break
        else:
            print("ERROR :: 날짜를 잘못 적으셨습니다. 숫자로만 입력해주세요.\n\n")
            continue
    return str(ret)

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

leagueType = askType()
# print("leagueType: ", leagueType);
if leagueType == 1:
    listUrl = "https://game.naver.com/esports/videos/league/lck" # LCK
elif leagueType == 2:
    listUrl = "https://game.naver.com/esports/videos/league/world_championship" # Worlds
else:
    listUrl = "https://game.naver.com/esports/videos/league/msi" # MSI

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

jsonObj = json.loads(jsonText)
popularList = jsonObj['props']['initialState']['video']['perTopLeagueVideo']['content']

matchTeam1 = askTeam1()
matchTeam2 = askTeam2()
matchSet = askSet()
matchDate = askDate()

print("")
print("해당 정보로 검색을 시작합니다.")
print("==============================================")
if leagueType == 1:
    print(matchTeam1 + " VS " + matchTeam2 + " " + matchSet + " (" + matchDate + ")")
else:
    print(matchTeam1 + " VS " + matchTeam2 + " " + " (" + matchDate + ")")
print("==============================================\n\n")
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
