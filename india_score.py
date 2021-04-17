import requests
import time
from bs4 import BeautifulSoup
from plyer import notification

def get_score(team_name):
    
    search_team = team_name.split()
    search_team.append("Cricket+Score")
    search_team="+".join(search_team)
    url=f"https://www.google.com/search?q={search_team}"

    header={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"}
     
    page=requests.get(url, headers=header)

    soup=BeautifulSoup(page.content,'lxml')
    soup.find("div", class_="imso_mh__scr-sep")

    score_team1=soup.find("div", class_="imspo_mh_cricket__first-score imspo_mh_cricket__one-innings-column-with-overs").text
    score_team2=soup.find("div", class_="imspo_mh_cricket__second-score imspo_mh_cricket__one-innings-column-with-overs").text
    #print(score_team1,score_team2)
    teams=soup.find_all("div",class_="ellipsisize liveresults-sports-immersive__team-name-width kno-fb-ctx")
    team_list=[]
    for t in teams:
        team_list.append(t.text)
    #print(team_list)    
    summary= soup.find("div",class_="imso_mh__score-txt imso-ani imspo_mh_cricket__summary-sentence").text
    #print(summary)

    data={
        "teams":team_list,
        "score_1":score_team1,
        "score_2":score_team2,
        "summary":summary
    }
    return data


data= get_score("SRH")


notification.notify(
    title=f"{data['teams'][0]}vs{data['teams'][1]}",
    message=f"{data['teams'][0]} {data['score_1']} -  {data['score_2']} {data['teams'][1]} \n {data['summary']}",
    timeout=10
)