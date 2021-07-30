import tweepy
import discord


client = discord.Client()

ConsumerKey = "" #Add Twitter API Key
ConsumerKeySecret = "" #Add Twitter API Secret Key

AccessKey = "" # Add Twitter Access Token
AccessSecret = "" #Add Twitter Token Secret

auth = tweepy.OAuthHandler(ConsumerKey, ConsumerKeySecret)
auth.set_access_token(AccessKey, AccessSecret)

api = tweepy.API(auth)

@client.event
async def on_ready():
    print("Logged in as Twitter to Discord Bot") #When launched, "Logged in as Twitter To Discord Bot" will be printed to your console

@client.event
async def on_message(message):
    if message.author == client.user: #Bot will only respond to members, not other bots meaning it won't repeat itself.
        return 

    if message.content.startswith("!tweet"):
        await api.update_status(message.content.strip("!tweet")) #When the Discord message starts with !tweet, it will post everything said after it to your Twitter bot.

client.run("") #Add your Discord Bot token