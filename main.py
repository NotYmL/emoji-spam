import requests, time

token=""
id=input("channel id: ")

try:
    while(True):
        res = requests.post(f"https://canary.discord.com/api/v9/channels/{id}/voice-channel-effects", headers={"authorization": token, "content-type": "application/json"}, json={"emoji_id":"809058615783718962","emoji_name":"arch","animation_type":0,"animation_id":12})
        if(res.status_code == 429):
            time.sleep(int((res.json())['retry_after'])+.2)
        time.sleep(0.5)
except KeyboardInterrupt:
    pass
