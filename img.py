import requests
from bs4 import BeautifulSoup
import datetime

# specify the URL that shows the chart image
pair = "usd-jpy"
start_date = "2021-01-01" # format yyyy-mm-dd
end_date = datetime.date.today().strftime("%Y-%m-%d") # format yyyy-mm-dd
url = f"https://www.investing.com/currencies/{pair}-historical-data?start_date={start_date}&end_date={end_date}"

# optional - set the request headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

# make the request to the website
response = requests.get(url, headers=headers)

# create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# find the HTML tag or attribute that contains the chart image URL
chart_url = soup.find("img", {"class": "navChartImg"})["data-src"]

# download the chart image and save it to a file
chart_image = requests.get(chart_url)
open(f"{pair}_{start_date}_{end_date}.png", "wb").write(chart_image.content)
