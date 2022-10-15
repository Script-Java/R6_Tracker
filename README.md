# R6_Tracker 
### For Personal and Educational Use Only

![r6 logo](https://www.pngkit.com/png/full/308-3083447_logo-kaeo-r6-pro-league-logo.png)

### About

- I am Learning web scraping with python and decided to practice with my favorite game that I have decided to turn into a python library.

- Creating this project using:
    - Streamlit
    - BeautifulSoup
    - Requests
    - Python

- I am going to be working on this project and will post and update daily...in this repository there will be streamlit GUI and terminal version of this project feel free to use

- to see what is upcoming check out the todo_list.txt

### installation
```git clone https://github.com/Script-Java/R6_Tracker.git```
- You can look at **main.py** to see how r6tracker.py works

### Usage
```from R6TRACKER.r6tracker import R6tracker
    r6 = R6tracker(user_name,user_platform)

    # Each of those variables below return a dictionary with data in them
    general = r6.general_info()
    top_op = r6.top_3_ops()
    ranked_stat = r6.ranked_stats()

```
```
# data Looks like this:
stats_stored = {
    "gamertag": player_tag,
    "best_mmr": best_mmr,
    "level": player_level,
    "seasonal_mmr": avg_seasonal_mmr,
    "total_matches": total_matches,
    "total_wins": total_wins,
    "win_ratio": player_win_ratio,
    "total_kills": player_total_kills,
    "player_kd": player_kd,
    "pfp_src": user_pfp_link,
    "rank_title": rank_name,
    "best_rank_src": rank_src
        }

top3_stored = {
            "op_names": top3_list,
            "op_img_src": top3_src
        }

ranked_stored = {
            "wins": ranked_wins,
            "losses": ranked_loss,
            "matches": ranked_matches,
            "deaths": ranked_deaths,
            "kills": ranked_kills,
            "win_ratio": ranked_win_ratio,
            "kd": ranked_kd,
            "kpm": ranked_kill_per_match
        }
```
### Example Usage

```
# example usage
# stores values of the dictionary in each variable
ranked_wins = ranked_stat["wins"]
ranked_loses = ranked_stat["losses"]
ranked_matches = ranked_stat["matches"]
ranked_deaths = ranked_stat["deaths"]
ranked_kills = ranked_stat["kills"]
ranked_win_ratio = ranked_stat["win_ratio"]
ranked_kd = ranked_stat["kd"]
kpm = ranked_stat["kpm"]

#creates a visual inside console
print("|-------------------------Ranked Stats-------------------------|")
print("\n")
print(f"Ranked wins: {ranked_wins.strip()} | Ranked loses: {ranked_loses.strip()}")
print(f"Matches: {ranked_matches.strip()} | Win ratio {ranked_win_ratio.strip()}")
print(f"Kills: {ranked_kills.strip()} | Deaths: {ranked_deaths.strip()}")
print(f"KD: {ranked_kd.strip()} | Kill/match: {kpm.strip()}")
print("\n")
print("|--------------------------------------------------------|")


# example output:

Ranked wins: 164 | Ranked loses: 165
Matches: 331 | Win ratio 49.5%
Kills: 1,632 | Deaths: 1,305
KD: 1.25 | Kill/match: 4.93

```