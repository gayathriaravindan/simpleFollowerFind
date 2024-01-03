#simple program to find instagram accounts you are following who are not following you back :)
from instabot import Bot
import pprint
import os 
import glob

cookie = glob.glob("config/*cookie.json")
if cookie : os.remove(cookie[0])

bot = Bot()

u = input("Instagram Username: ")
p = input("Instagram Password: ")

bot.login(username = u, password = p, ask_for_code = True)
print("Logged in!")

followers = bot.get_user_followers(u)
following = bot.get_user_following(u)

notFollowingBack = list(set(following) - set(followers))
notFollowingBack = [bot.get_username_from_user_id(user_id) for user_id in notFollowingBack]
pprint.pprint(notFollowingBack)
