from tkinter.tix import COLUMN
from bs4 import BeautifulSoup
import requests
import streamlit as st
import urllib.request
from PIL import Image

class R6tracker:
    def __init__(self,name,platform):
        self.name = name
        self.platform = platform
        self.r6_website = f"https://r6.tracker.network/profile/{platform}/{name}"
        self.response = requests.get(self.r6_website)
        self.soup = BeautifulSoup(self.response.text, "html.parser")
        
        # Basic user information in the overview section from r6 tracker
        user_gamer_tag = self.soup.find("span", {"class":"trn-profile-header__name"}).string
        # retiving user PFP
        user_profile_img_container = self.soup.find("div", {"class": "trn-profile-header__avatar trn-roundavatar trn-roundavatar--white"})
        user_profile = user_profile_img_container.find("img", recursive=False)
        user_pfp_link = user_profile["src"]
        urllib.request.urlretrieve(user_pfp_link, "pfp.png")
        img = Image.open("pfp.png")
    
        # overall stats and basic stats
        user_total_matches = self.soup.find("div", {"class":"trn-card__header-subline"}).string
        user_total_wins = self.soup.find("div", {"data-stat":"PVPMatchesWon"}).string
        user_total_win_ratio = self.soup.find("div", {"data-stat":"PVPWLRatio"}).string
        user_total_kills = self.soup.find("div", {"data-stat": "PVPKills"}).string
        user_total_kill_ratio = self.soup.find("div", {"data-stat": "PVPKDRatio"}).string
        
        #streamlit setup here
        st.image(img)
        st.write(f"Total Mathces Played: ```{user_total_matches}```")
        col2,col3,col4,col5 = st.columns(4)
        col2.metric("Total Wins", user_total_wins, "")
        col3.metric("Total win %", user_total_win_ratio)
        col4.metric("Total Kills", user_total_kills)
        col5.metric("KD", user_total_kill_ratio)
        
    def get_seasons():
        pass
    
    def get_recently_played_with():
        pass
    
    def get_mmr_history():
        pass
    
    
        
R6tracker("BroooGimmeEla", "pc")
        
        