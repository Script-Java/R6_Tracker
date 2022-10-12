from operator import attrgetter
from bs4 import BeautifulSoup
import requests


def scrapeData(name,plat):
    platform_list = ["pc","xbox","psn"]
    tracker_url = f"https://r6.tracker.network/profile/{plat}/{name}"
    scrape_this = requests.get(tracker_url)
    soup = BeautifulSoup(scrape_this.text, "html.parser")
    general_win_ratio = soup.find("div", attrs={"data-stat":"PVPWLRatio"})
    wins_number = soup.find("div", attrs={"data-stat":"PVPMatchesWon"})
    total_matches_played = soup.find("div", attrs={"data-stat":"PVPMatchesPlayed"})
    total_kills = soup.find("div", attrs={"data-stat":"PVPKills"})
    overall_kd_ratio = soup.find("div", attrs={"data-stat":"PVPKDRatio"})
    print(f"{general_win_ratio}, {wins_number}, {total_matches_played}")
    
    
    
scrapeData("BroooGimmeEla","pc")