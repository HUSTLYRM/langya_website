import json
import requests
import os
import time

# 假设这是从文件或API获取的JSON数据，从url
# https://rm-static.djicdn.com/live_json/schedule.json
# json_data = requests.get("https://schedule.scutbot.cn/api/schedule").json()
json_data = json.loads(open('schedule.json').read())
# matches_ = json_data["data"]["last_event"]["zones"]["nodes"]

video_data = requests.get("https://rm-static.djicdn.com/live_json/simple_cms.json").json()

target_college = "华中科技大学"

# print(len(matches_))

saved_matches = []

# for match in matches_:
#     print(match["name"])
#     # print(match["id"])
#     # print(match["groupMatches"]["nodes"])
#     for game in match["knockoutMatches"]["nodes"]:
#         saved_match = {}
#         if game["blueSide"]["player"]["team"]["collegeName"] == target_college or game["redSide"]["player"]["team"]["collegeName"] == target_college:
#         #    print(game)
#             saved_match["blueSide"] = game["blueSide"]
#             saved_match["redSide"] = game["redSide"]
#             saved_match["redSideWinGameCount"] = game["redSideWinGameCount"]
#             saved_match["blueSideWinGameCount"] = game["blueSideWinGameCount"]
#             saved_match["planStartedAt"] = game["planStartedAt"]
#             saved_match["match_id"] = game["id"]
#             # print(saved_match)
#             # break
#             saved_match["name"] = f"{match['name']}淘汰赛"
#             if game["slug"]:
#                 saved_match["name"] = f"{match['name']}{game['slug']}"

#             for video in video_data["simple_cms"]:
#                 if video["content"].get("match_id") is None:
#                     continue

#                 # print(video["content"]["match_id"], saved_match["match_id"])
#                 if video["content"]["match_id"] == saved_match["match_id"]:
#                     saved_match["video"] = video["content"]["main_source_url"]
#                     break

#             saved_matches.append(saved_match) 
#     for game in match["groupMatches"]["nodes"]:
#         saved_match = {}
#         if game["blueSide"]["player"]["team"]["collegeName"] == target_college or game["redSide"]["player"]["team"]["collegeName"] == target_college:
#         #    print(game)
#             saved_match["blueSide"] = game["blueSide"]
#             saved_match["redSide"] = game["redSide"]
#             saved_match["redSideWinGameCount"] = game["redSideWinGameCount"]
#             saved_match["blueSideWinGameCount"] = game["blueSideWinGameCount"]
#             saved_match["planStartedAt"] = game["planStartedAt"]
#             saved_match["match_id"] = game["id"]
#             # print(saved_match)
#             # break
#             saved_match["name"] = f"{match['name']}小组赛"
#             if game["slug"]:
#                 saved_match["name"] = f"{match['name']} {game['slug']}"

#             for video in video_data["simple_cms"]:
#                 if video["content"].get("match_id") is None:
#                     continue
#                 if video["content"]["match_id"] == saved_match["match_id"]:
#                     saved_match["video"] = video["content"]["main_source_url"]
#                     break

#             saved_matches.append(saved_match)

#     # break
#     # if saved_match:
        

matches_ = json_data["data"]["event"]["zones"]["nodes"]
for match in matches_:
    for game in match["groupMatches"]["nodes"]:
        saved_match = {}
        print(game)
        if game['status'] == 'WAITING':
            continue
        if not game["blueSide"]["player"]["team"] or not game["redSide"]["player"]["team"]:
            continue
        if game["blueSide"]["player"]["team"]["collegeName"] == target_college or game["redSide"]["player"]["team"]["collegeName"] == target_college:
        #    print(game)
            saved_match["blueSide"] = game["blueSide"]
            saved_match["redSide"] = game["redSide"]
            saved_match["redSideWinGameCount"] = game["redSideWinGameCount"]
            saved_match["blueSideWinGameCount"] = game["blueSideWinGameCount"]
            saved_match["planStartedAt"] = game["planStartedAt"]
            saved_match["match_id"] = game["id"]
            # print(saved_match)
            # break
            saved_match["name"] = f"2025高校联盟赛-3V3对抗赛{match['name']}小组赛"
            if game["slug"]:
                saved_match["name"] = f"{match['name']}{game['slug']}"

            for video in video_data["simple_cms"]:
                if video["content"].get("match_id") is None:
                    continue

                # print(video["content"]["match_id"], saved_match["match_id"])
                if video["content"]["match_id"] == saved_match["match_id"]:
                    saved_match["video"] = video["content"]["main_source_url"]
                    break

            saved_matches.append(saved_match)  
    for game in match["knockoutMatches"]["nodes"]:
        saved_match = {}
        if not game["blueSide"]["player"] or not game["redSide"]["player"]:
            continue 
        if not game["blueSide"]["player"]["team"] or not game["redSide"]["player"]["team"]:
            continue
        if game["blueSide"]["player"]["team"]["collegeName"] == target_college or game["redSide"]["player"]["team"]["collegeName"] == target_college:
        #    print(game)
            saved_match["blueSide"] = game["blueSide"]
            saved_match["redSide"] = game["redSide"]
            saved_match["redSideWinGameCount"] = game["redSideWinGameCount"]
            saved_match["blueSideWinGameCount"] = game["blueSideWinGameCount"]
            saved_match["planStartedAt"] = game["planStartedAt"]
            saved_match["match_id"] = game["id"]
            # print(saved_match)
            # break
            saved_match["name"] = f"2025高校联盟赛-3V3对抗赛{match['name']}淘汰赛"
            if game["slug"]:
                saved_match["name"] = f"{match['name']}{game['slug']}"
            print(saved_match["name"])
            for video in video_data["simple_cms"]:
                if video["content"].get("match_id") is None:
                    continue

                # print(video["content"]["match_id"], saved_match["match_id"])
                if video["content"]["match_id"] == saved_match["match_id"]:
                    saved_match["video"] = video["content"]["main_source_url"]
                    break

            saved_matches.append(saved_match)  

print(len(saved_matches))

# 保存到文件
# ---
# name: 小组赛
# red: 华中科技大学 狼牙
# blue: 西安交通大学 笃行
# red_score: 2
# red_logo: /images/1525675209294-logo_blue_800x800.png
# blue_score: 0
# blue_logo: /images/1525666415627-logo_red_800x800.png
# date: 2025-3-14 15:40
# link: https://www.robomaster.com/live?djifrom=nav
# ---

for match in saved_matches:
    file_name = f"_events/{match['name']}.md"
    cnt = 0
    while os.path.exists(file_name):
        cnt += 1
        file_name = f"_events/{match['name']}{cnt}.md"
    with open(file_name, "w") as f:
        link = ""
        # 如果现在的时间早于比赛时间，就可以直接看直播
        if match["video"]:
            link = match["video"]
        else:
            link = "https://www.robomaster.com/live?djifrom=nav"
        # 将比赛时间+8小时
        # 2019-05-25T01:30:00Z
        match_time = time.mktime(time.strptime(match["planStartedAt"], "%Y-%m-%dT%H:%M:%SZ"))
        match_time += 8 * 3600
        match_time_str = time.strftime("%Y-%m-%d %H:%M", time.localtime(match_time))
        # match_time = time.localtime(match_time)
        f.write(f"""---
name: {match['name']}
red: {match['redSide']['player']['team']['collegeName']} {match['redSide']['player']['team']['name']}
blue: {match['blueSide']['player']['team']['collegeName']} {match['blueSide']['player']['team']['name']}
red_score: {match['redSideWinGameCount']}
red_logo: {match['redSide']['player']['team']['collegeLogo']}
blue_score: {match['blueSideWinGameCount']}
blue_logo: {match['blueSide']['player']['team']['collegeLogo']}
date: {match_time_str}
link: https://www.robomaster.com/zh-CN/resource/video?type=live-replay&videoUrl={link}&zoneType=548
---
""")
        
