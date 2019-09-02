import os
import requests
import smtplib
from email.message import EmailMessage
from twilio.rest import Client
from textblob import TextBlob

from data import emails

#getting email and password and API keys from environment variables 
EMAIL_ADDRESS = os.environ.get("GMAIL_USER")
EMAIL_PASSWORD = os.environ.get("GMAIL_PASS")
API_KEY = os.environ.get("NEWS_API")
Twilio_SID = os.environ.get("Twilio_SID")
Twilio_Token = os.environ.get("Twilio_Token")

#setting up Twilio
account_sid = Twilio_SID
auth_token = Twilio_Token
client = Client(account_sid, auth_token)

#creating an instance 
msg = EmailMessage()
msg['subject'] = "Latest News"
msg['From'] = EMAIL_ADDRESS
msg['To'] = emails

#url from NewsAPI
url = f"https://newsapi.org/v2/top-headlines?country=us&{API_KEY}"
response = requests.get(url)
articles = response.json()['articles']

news_email = ""
news_sms = ""

#looping through each all the articles and adding it to the string
for i, article in enumerate(articles, 1):
	news_email += (f"{i}. {article['title']}\n")

msg.set_content(news_email)

#looping through top 15 news for the SMS
for i, article in enumerate(articles, 1):
	if i<11:
		news_sms += (f"{i}. {article['title']}\n")


#email using SMTP
def send_email():
	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
		smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
		smtp.send_message(msg)


#print(news_sms)

#SMS using twilio
def send_sms():
	message = client.messages.create(
	                              body=news_sms,
	                              from_='+14704287946',
	                              to='+14045478193',
	                          )



#send_email()
#send_sms()

