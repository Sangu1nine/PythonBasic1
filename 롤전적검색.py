# 롤 전적검색
import requests
import json
import pandas as pd
API_KEY = "RGAPI-73dee9ea-2e0b-48ea-88b4-b8b6ebf3ad4e"
BASE_URL = "https://asia.api.riotgames.com"

def get_summoner_info(summoner_name):
    split_name = summoner_name.split("#")  # 소환사명#태그를 분리
    
    # Riot API URL 설정
    url = f"{BASE_URL}/riot/account/v1/accounts/by-riot-id/{split_name[0]}/{split_name[1]}"
    
    headers = {"X-Riot-Token": API_KEY}
    
    # API 요청
    response = requests.get(url, headers=headers)
    
    # 응답 상태 코드가 200이면 정상적으로 소환사 정보를 반환
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}, {response.text}"

# 소환사명#태그를 입력받기

def get_recent20_match_info(summoner_name):
    split_name = summoner_name.split("#")  # 소환사명#태그를 분리
    puuid = get_summoner_info(summoner_name)['puuid']
    # Riot API URL 설정
    url = f"{BASE_URL}/lol/match/v5/matches/by-puuid/{puuid}/ids"
    
    headers = {"X-Riot-Token": API_KEY}
    
    # API 요청
    response = requests.get(url, headers=headers)
    
    # 응답 상태 코드가 200이면 정상적으로 소환사 정보를 반환
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}, {response.text}"

def match_detail_20(summoner_name) :
    split_name = summoner_name.split("#")  # 소환사명#태그를 분리
    puuid = get_summoner_info(summoner_name)['puuid']
    for matchId in get_recent20_match_info(summoner_name) :
        url = f"{BASE_URL}/lol/match/v5/matches/{matchId}"
    
        headers = {"X-Riot-Token": API_KEY}
    
    # API 요청
        response = requests.get(url, headers=headers)
    
    # 응답 상태 코드가 200이면 정상적으로 소환사 정보를 반환
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}, {response.text}"




def match_detail(summoner_name) :
    split_name = summoner_name.split("#")  # 소환사명#태그를 분리
    puuid = get_summoner_info(summoner_name)['puuid']

    for matchId in get_recent20_match_info(summoner_name) :

        url = f"{BASE_URL}/lol/match/v5/matches/{matchId}"
        headers = {"X-Riot-Token": API_KEY}

    # API 요청
        response = requests.get(url, headers=headers)
    
    # 응답 상태 코드가 200이면 정상적으로 소환사 정보를 반환

        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}, {response.text}"        

        # Extract relevant game information
        game_info = data["info"]
        participants = game_info["participants"]

        # Create a structured DataFrame
        player_stats = []
        for participant in participants:
            player_stats.append({
                "Player": participant["riotIdGameName"] if "riotIdGameName" in participant else "Unknown",
                "Champion": participant["championName"],
                "Kills": participant["kills"],
                "Deaths": participant["deaths"],
                "Assists": participant["assists"],
                "Damage Dealt": participant["totalDamageDealtToChampions"],
                "Gold Earned": participant["goldEarned"],
                "Win": participant["win"],
                "Team ID": participant["teamId"],
            })

        df = pd.DataFrame(player_stats)

        # Display the DataFrame
        import ace_tools as tools
        tools.display_dataframe_to_user(name="Match Player Stats", dataframe=df)


summoner_name = input("소환사명#태그를 입력해주세요 :")
# print(get_summoner_info(summoner_name))
# print(get_recent20_match_info(summoner_name))

print(match_detail(summoner_name))



'''
import json
import pandas as pd

# Load the match data
file_path = "/mnt/data/matchdata.txt"
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Extract relevant game information
game_info = data["info"]
participants = game_info["participants"]

# Create a structured DataFrame
player_stats = []
for participant in participants:
    player_stats.append({
        "Player": participant["riotIdGameName"] if "riotIdGameName" in participant else "Unknown",
        "Champion": participant["championName"],
        "Kills": participant["kills"],
        "Deaths": participant["deaths"],
        "Assists": participant["assists"],
        "Damage Dealt": participant["totalDamageDealtToChampions"],
        "Gold Earned": participant["goldEarned"],
        "Win": participant["win"],
        "Team ID": participant["teamId"],
    })

df = pd.DataFrame(player_stats)

# Display the DataFrame
import ace_tools as tools
tools.display_dataframe_to_user(name="Match Player Stats", dataframe=df)
'''