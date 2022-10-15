from R6TRACKER.r6tracker import R6tracker

user_name = input("Enter username (example : BroooGimmeEla) \n")
user_platform = input("Please enter a platform (options : [psn | xbox | pc]) \n")

r6 = R6tracker(user_name,user_platform)
general = r6.general_info()                                                                                 
# overall data
player_tag = general["gamertag"]
best_mmr = general["best_mmr"]
level = general["level"]
season_mmr = general["seasonal_mmr"]
matches = general["total_matches"]
wins = general["total_wins"]
win_ratio = general["win_ratio"]
kills = general["total_kills"]
kd = general["player_kd"]
best_rank = general["rank_title"]

# top operators
top_op = r6.top_3_ops()
top_operators = top_op["op_names"]

# ranked stats
ranked_stat = r6.ranked_stats()
ranked_wins = ranked_stat["wins"]
ranked_loses = ranked_stat["losses"]
ranked_matches = ranked_stat["matches"]
ranked_deaths = ranked_stat["deaths"]
ranked_kills = ranked_stat["kills"]
ranked_win_ratio = ranked_stat["win_ratio"]
ranked_kd = ranked_stat["kd"]
kpm = ranked_stat["kpm"]

print("|-------------------------Overall Stats--------------------------|")
print("\n")
print(f"{player_tag.strip()} | Level: {level.strip()}")
print(f"Best MMR: {best_mmr.strip()} | Season AVG: {season_mmr.strip()}")
print(f"{matches.strip()} | Total Kills: {kills.strip()}")
print(f"W: {wins.strip()} | W ratio: {win_ratio.strip()}")
print(f"K/D: {kd.strip()} | Best Rank: {best_rank.strip()}")
print("\n")
print("|-------------------------Top Operators-------------------------|")
print("\n")
print(f"Top 3 operators: {top_operators}")
print("\n")
print("|-------------------------Ranked Stats-------------------------|")
print("\n")
print(f"Ranked wins: {ranked_wins.strip()} | Ranked loses: {ranked_loses.strip()}")
print(f"Matches: {ranked_matches.strip()} | Win ratio {ranked_win_ratio.strip()}")
print(f"Kills: {ranked_kills.strip()} | Deaths: {ranked_deaths.strip()}")
print(f"KD: {ranked_kd.strip()} | Kill/match: {kpm.strip()}")
print("\n")
print("|--------------------------------------------------------|")



