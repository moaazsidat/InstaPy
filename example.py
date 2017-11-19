"""Example Case of the Script"""
from instapy import InstaPy
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

USERNAME = os.environ.get("IG_USERNAME")
PASSWORD = os.environ.get("IG_PASSWORD")

# if you don't provide arguments, the script will look for INSTA_USER and INSTA_PW in the environment
session = InstaPy(
    username=USERNAME,
    password=PASSWORD)

"""Logging in"""
# logs you in with the specified username and password
session.login()

accs = [
    'therock',
    'natgeo',
    'jimmyfallon'
]
session.unfollow_by_list(accs)


"""Ending the script"""
# clears all the cookies, deleting you password and all information from this session
session.end()
