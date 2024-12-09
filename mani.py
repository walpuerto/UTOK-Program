from bs4 import BeautifulSoup
from selenium import webdriver
import json

# Run Chess.com API
dr = webdriver.Chrome()
dr.get("https://api.chess.com/pub/puzzle/random")
bs = BeautifulSoup(dr.page_source,"lxml")

# Get Image
imageUrl = json.loads(bs.text)["image"]
dr.get(imageUrl)
dr.save_screenshot("Puzzles\Chess\chess.png")
dr.close()