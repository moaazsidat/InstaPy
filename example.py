"""Example Case of the Script"""
from instapy import InstaPy
import os
from dotenv import load_dotenv, find_dotenv
import random

load_dotenv(find_dotenv(), override=True)

USERNAME = os.environ.get("IG_USERNAME")
PASSWORD = os.environ.get("IG_PASSWORD")

# if you don't provide arguments, the script will look for INSTA_USER and INSTA_PW in the environment
session = InstaPy(
    username=USERNAME,
    password=PASSWORD,
    nogui=True)

"""Logging in"""
# logs you in with the specified username and password
session.login()

accs = [
    'theglobewanderer',
    'awesomelife.style',
    'squarespace',
    'ourplanetdaily',
    'dreaming_travel',
    'discoverglobe',
    'nakedplanet',
    'moodygrams',
    'artofvisuals',
    'thecreatorclass',
    'beautifuldestinations',
    'earthpix',
    'instagood',
    'awesome_earthpix',
    'heatercentral',
    'theimaged',
    'canonusa',
    'visualmobs',
    'airbnb',
    'awesome.phtoographers',
    'reflectiongram',
    'way2ill_',
    'earthvacations',
    'stayandwander',
    'cntraveler'
    'awesomeglobe',
    'earthofficial',
    'australia',
    'shotzdelight',
    'travelandleisure',
    'agameoftones',
    'visualsoflife',
    'canon_photos',
    'illgrammers',
    'curiocitytoronto',
    'sonyalpha',
    '6tour',
    '6ixwalks',
    'wildcalifornia_',
    'createcommune',
    'natureonly',
    'thevisualscollective',
    'time',
    'dailyhivetoronto',
    'gopro',
    'fantastic_earth',
    'natgeotravel',
    'wonderful_places',
    'magnumphotos'
    'awesome.earth',
    'nytimes',
    'streets_vision',
    'thephotosociety',
    'awesomedreamplaces',
    'etsy',
    'forbes',
    'streetdreamsmag',
    'aroundtheworldpix',
    'nationaldestinations',
    'natgeoadventure',
    'bonappetitmag',
    'discoverychannel',
    'national.earth',
    'bbcearth',
    'ig_color',
    'passionpassport',
    'beautifulmatters',
    'designmilk',
    'discover_earthpix',
    'travelchannel',
    'itsabandoned',
    '500px',
    'usaprimeshot',
    'earth.landscape',
    'tripadvisor',
    'luxuryworldtraveler',
    'welivetoexplore',
    'wilderness_culture',
    'google',
    'patagonia',
    'bbc_travel',
    'createxplore',
    'hasselblad_official',
    'streetsoftoronto',
    'natgeocreative',
    'shopify',
    'techcrunch',
    'amazon',
    'travelawesome',
    'create.and.capture',
    'natgeowild',
    'vsco',
    'streetshared',
    'californiacaptures',
    'eclectic_shotz',
    'moodyports',
    'visualambassadors',
    'gramslayers',
    'strangertones',
    'fatal.frames',
    'caligrammers',
    'meistershots',
    'torontonia_ig',
    'nowtoronto',
    'globeandmail',
    'toronto_restaurants',
    'lovetoronto',
    'toronto_insta',
    'to_finest',
    'ottawa_2017',
    'torontolife',
    'lululemon',
    '_settlementco',
    'printfulhq',
    'mailchimp',
    'adele',
    'nytimestravel',
    'expedia',
    'homepolish',
    'humansofny',
    'bora.vs.bora',
    'fantastic.colours',
    'lumi',
    'trappingtones',
    'landscape.photos',
    'sony',
    'lonelyplanet',
    'nasa',
    'natgeo',
]

print(len(accs))
random.shuffle(accs)

session.unfollow_by_list(accs)

session.follow_by_list(accs)


"""Ending the script"""
# clears all the cookies, deleting you password and all information from this session
session.end()
