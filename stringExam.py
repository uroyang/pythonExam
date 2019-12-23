a = "Life is too short, You need Python"
print(a[:])
print(a[8:11])
b = "20191222rainy"
year = b[:4]
month = b[4:6]
day = b[6:8]
weather = b[8:]
today_weather = f"오늘은 {year}년 {month}월 {day}일 입니다. 날씨는 {weather}입니다."
print(today_weather)
print(b.count("2"))
print(b.find("r"))
