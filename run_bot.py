import metal_archives_scraper.ma_scraper as ma_scraper
import Utils.Bot_Utils as Bot_Utils
import lemmy_api.lemmy_api_tasker as lemmy_api_tasker
from config.config import set_for_production, wantedGenre, lemmy_instance, title, community_id, last_post_id, release_day, username_or_email, password, last_post_date
from dotenv import dotenv_values, set_key
import time


# Load misc variables
release_type_list = ["Full-length","Single","EP"]

# Get current Date
today, currentWeekday, wantedMonth, wantedDay = Bot_Utils.get_date()

# Change .env vars / settings 
if input("Do you want to change settings? 'y/n'") == "y":
    wantedGenre = input("What genre releases do you want to post? ")
    wantedDay = input("Release day testing overwrite ")
    currentWeekday = input("Type '4' for immediate posting ")
    title = input("What should the weekly post title be? (can also be changed in .env) ")
    community_id = input("In which community do you want to post this? (Needs to be community id not name) ")
    env_vars = dotenv_values(".env")
    env_vars['wantedGenre'] = wantedGenre
    env_vars['post_title'] = title
    env_vars['community_id'] = community_id
    for key, value in env_vars.items():
        set_key(".env", key, value)

# Bot
# Post to Lemmy function
def post_to_lemmy():
    if currentWeekday == release_day and does_post_exist == False:
        # Call scraper to get release list
        wanted_list,wantedMonthString = ma_scraper.get_releaseList(wantedGenre,wantedDay,wantedMonth)
        # Create body text
        body = ""
        body += (f'{wantedGenre} releases for {wantedDay} of {wantedMonthString}: \n')
        for type in release_type_list:                                  # cheeky way of sorting the list
            releases_list = Bot_Utils.sortByReleaseType(type, wanted_list,wantedGenre,wantedDay,wantedMonthString)
            for string in releases_list:
                body += string
            

        # Get User Token
        user_token = lemmy_api_tasker.get_user_token(username_or_email, password, lemmy_instance)
        # Post through Lemmy Api
        post_successful, post_id, posted_date = lemmy_api_tasker.create_post(user_token, int(community_id), lemmy_instance, title, body)
        
        # For testing
        # print(title)
        # print(body)
        # post_successful = True 
        # post_id = "1"
        # posted_date = "15.03.2023"

        if post_successful == True:
            env_vars['last_post_id'] = str(post_id)
            env_vars['last_post_date'] = str(posted_date)
            for key, value in env_vars.items():
                set_key(".env", key, value)
        does_post_exist = True
    else:
        print("Waiting 7 days to post again...")
        # time.sleep(10)
        # currentWeekday = "4"      #Test
        # wantedDay = "23"          #Test
        # wantedMonth = "June"    #Test
        time.sleep(43200)
        today, currentWeekday, wantedMonth, wantedDay = Bot_Utils.get_date()    # refresh date

# Scrapes and creates title and body but posts it only into the console, not to Lemmy
def post_locally():
    if currentWeekday == release_day and does_post_exist == False:
        # Call scraper to get release list
        wanted_list,wantedMonthString = ma_scraper.get_releaseList(wantedGenre,wantedDay,wantedMonth)
        # Create body text
        body = ""
        body += (f'{wantedGenre} releases for {wantedDay} of {wantedMonthString}: \n')
        for type in release_type_list:                                  # cheeky way of sorting the list
            releases_list = Bot_Utils.sortByReleaseType(type, wanted_list,wantedGenre,wantedDay,wantedMonthString)
            for string in releases_list:
                body += string

        # For testing
        print(title)
        print(body)
        post_successful = True 
        post_id = "1"
        posted_date = "15.03.2023"

        if post_successful == True:
            env_vars['last_post_id'] = str(post_id)
            env_vars['last_post_date'] = str(posted_date)
            for key, value in env_vars.items():
                set_key(".env", key, value)
        does_post_exist = True
    else:
        print("Waiting 7 days to post again...")
        # time.sleep(10)
        # currentWeekday = "4"      #Test
        # wantedDay = "23"          #Test
        # wantedMonth = "June"    #Test
        time.sleep(43200)
        today, currentWeekday, wantedMonth, wantedDay = Bot_Utils.get_date()    # refresh date        

does_post_exist = False
loop_bot = True
# Bot runs only on friday
while loop_bot == True:
    if set_for_production == True:
        post_to_lemmy()
    else:
        post_locally()                          # Scrapes and creates title and body but posts it only into the console, not to Lemmy