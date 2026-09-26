import requests

url = "https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json"
response = requests.get(url)
data = response.json()

area_name = data[0]["timeSeries"][0]["areas"][0]["area"]["name"]
today_weather = data[0]["timeSeries"][0]["areas"][0]["weathers"][0]
today_pop = data[0]["timeSeries"][1]["areas"][0]["pops"][0]

temp_areas = data[0]["timeSeries"][2]["areas"]
for a in temp_areas:
    if a["area"]["name"] == "東京":
        temps = a["temps"]
        break

print(f"{area_name}の今日の天気: {today_weather}")
print(f"降水確率: {today_pop}%")
print(f"気温: 最低{temps[0]}℃ / 最高{temps[1]}℃")

if int(today_pop) >= 30:
    print("傘を持っていきましょう")
else: 
    print("傘は大丈夫そうです")

if int(temps[1]) <= 20:
    print("上着があると安心です")
elif int(temps[1]) >= 28:
    print("薄着で大丈夫そうです")
else:
    print("過ごしやすい気温です")