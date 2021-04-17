import requests
from bs4 import BeautifulSoup
from plyer import notification

def football_team(team_name):
    name=team_name.split()
    name.append("footabll + live + score")
    name="+".join(name)

    url=f"https://www.google.com/search?q={name}"

    header={"user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"

    }
    page=requests.get(url,headers=header)

    soup=BeautifulSoup(page.content,'lxml')
    score=soup.find("div",class_="imso_mh__ma-sc-cont")
    score1=score.find("div",class_="imso_mh__l-tm-sc imso_mh__scr-it imso-light-font").text
    score2=score.find("div",class_="imso_mh__r-tm-sc imso_mh__scr-it imso-light-font").text
    
    teams=soup.find_all("div",class_="ellipsisize liveresults-sports-immersive__team-name-width kno-fb-ctx")
    competition=soup.find("span",class_="imso-hide-overflow").text
    print(competition)
    team_lists=[]
    for i in teams:
        team_lists.append(i.text)
    print(team_lists)    
    minutes=soup.find("span",class_="liveresults-sports-immersive__game-minute").text
    print(minutes)
    summary_of_game=soup.find("div",class_="imso_mh_s__lg-st-srs").text
    print(summary_of_game)
    
    data={
        "competition": competition,
        "names":team_lists,
       "score_1":score1,
       "score_2":score2,
        "minutes":minutes,
        "summary":summary_of_game
    }
    return data

data=football_team("Goa")

notification.notify(
    title=f" {data['competition']} \n {data['names'][0]} vs {data['names'][1]}",
    message=f"{data['names'][0]} {data['score_1']} -  {data['score_2']} {data['names'][1]}  {data['minutes']} \n {data['summary']} ",
    timeout=10
)