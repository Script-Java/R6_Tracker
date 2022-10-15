import string
from bs4 import BeautifulSoup
import requests
import streamlit as st
import urllib.request
from io import BytesIO
from PIL import Image

class R6tracker:
    # grabs name and plat form
    #creates a connection with the website
    def __init__(self,name,platform):
        self.name = name
        self.platform = platform
        self.r6_website = f"https://r6.tracker.network/profile/{platform}/{name}"
        self.response = requests.get(self.r6_website)
        self.soup = BeautifulSoup(self.response.text, "html.parser")
        
    def general_info(self):
        # user name
        # gamer Tag
        player_tag = self.soup.find("div", {"class":"trn-profile-header__name"})
        stat_value_div = self.soup.findAll("div", {"class":"trn-defstat__value-stylized"})
        stat_value = []
        for stat_value_data in stat_value_div:
            if stat_value_data["class"] == "trn-defstat__value-stylized" or "trn-defstat__value":
                stat_value.append(stat_value_data.string)
        best_mmr = stat_value[0]
        player_level = stat_value[1]
        avg_seasonal_mmr = stat_value[2]
        total_wins = self.soup.find("div", {"data-stat":"PVPMatchesWon"})
        player_win_ratio = self.soup.find("div", {"data-stat":"PVPWLRatio"})
        player_total_kills = self.soup.find("div", {"data-stat":"PVPKills"})
        player_kd = self.soup.find("div", {"data-stat":"PVPKDRatio"})
        
        # retiving user PFP
        # Grab the image container 
        # Then find the img element inside it and with that access the src
        user_profile_img_container = self.soup.find("div", {"class": "trn-profile-header__avatar trn-roundavatar trn-roundavatar--white"})
        user_profile = user_profile_img_container.find("img", recursive=False)
        user_pfp_link = user_profile["src"]
        
        # user PFP optional
        # grabs link and converts into readable data
        response = requests.get(user_pfp_link)
        
        # pfp Ready.......
        pfp = Image.open(BytesIO(response.content))
        
        # Find Rank Banner
        #gets best rank
        best_rank_container = self.soup.find("div", {"class": "trn-card__content trn-card--light trn-defstats-flex pt8 pb8"})
        rank_el = best_rank_container.find("img", recursive=False)
        rank_name = rank_el["title"]
        rank_src = user_profile["src"]
        response2 = requests.get(user_pfp_link)
        
        # The rank Img rady.......
        best_rank = Image.open(BytesIO(response2.content))
        
R6tracker("BroooGimmeEla", "pc").general_info()
        
        