# ClimbShoeBot

ClimbShoeBot is designed to update the user when a new climbing shoe has been added to the climbing gym or an older shoe has been restocked. In addition, a Machine Learning bot will be implemented to run sentiment analysis (via Reddit comments) on the shoe model as a review for the user.

## Systems Overview
A webscraper will be made to recheck the shop page every day. If a new entry has been added from the previous day’s records, a bot will alert the user via an email/Telegram message. Additionally, the new shoe model will be searched among Reddit comments for sentiment analysis to determine the worth of the shoe for the user.

## Specifications & Features
- Webscraper (requests, BeautifulSoup) for a climbing shoe website
- System to query for specific Reddit comments
- Webscraper for Reddit comments
- Machine Learning sentiment analysis (PyTorch)
- Telegram bot
