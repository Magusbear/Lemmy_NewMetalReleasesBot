from dotenv import dotenv_values, set_key

# Load .env variables
env_vars = dotenv_values(".env")
wantedGenre = env_vars["wantedGenre"]
lemmy_instance = env_vars["lemmy_instance"]
community_id = int(env_vars["community_id"])
last_post_id = env_vars["last_post_id"]
release_day = env_vars["release_day"]
username_or_email = env_vars["username_or_email"]
password = env_vars["password"]
last_post_date = env_vars["last_post_date"]
title = env_vars['post_title']
set_for_production = env_vars['set_for_production']
does_post_exist = env_vars['does_post_exist']
loop_bot = True