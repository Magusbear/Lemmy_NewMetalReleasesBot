import requests
from dotenv import dotenv_values, set_key
env_vars = dotenv_values(".env")


# Login
def get_user_token(username_or_email, password, lemmy_instance):
    login_url = f'{lemmy_instance}/api/v3/user/login'
    login_data = {
        "username_or_email": username_or_email,
        "password": password
    }
    try:
        response = requests.post(login_url, json=login_data)
        response.raise_for_status()  # Debug print
        user_token = response.json()["jwt"]
        return user_token
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while getting token {e:}")
        raise

# Create a post
def create_post(user_token, community_id, lemmy_instance, title, body):
    create_post_url = f'{lemmy_instance}/api/v3/post'
    create_post_data = {
        "community_id": community_id,
        "name": title,
        "body": body,
        "auth": user_token
    }
    try: 
        response = requests.post(create_post_url, json=create_post_data)
        response.raise_for_status()  # Debug print
        response_data = response.json()
        post_id = response_data['post_view']['post']['id']
        post_name = response_data['post_view']['post']['name']
        community_name = response_data['post_view']['community']['name']
        link_to_post = response_data['post_view']['post']['ap_id']
        posted_date = response_data['post_view']['post']['published']
        if post_id:
            print(f'Post "{post_name}" created successfully in community "{community_name}". Link: {link_to_post} ')
            post_successful = True
            return post_successful, post_id, posted_date
        else:
            print("Failed to create post.")
            post_successful = False
            return post_successful, None, posted_date
    except requests.exceptions.RequestException as e:
        print(f"Lemmy Response: {e}")  # Debug print
        raise

# response_data={'post_view': {'post': {'id': 41, 'name': 'TestyMcTestPost2', 'body': 'Still very fantastic body!', 'creator_id': 10907, 'community_id': 5, 'removed': False, 'locked': False, 'published': '2023-06-21T15:48:55.752735', 'deleted': False, 'nsfw': False, 'ap_id': 'https://voyager.lemmy.ml/post/41', 'local': True, 'language_id': 37, 'featured_community': False, 'featured_local': False}, 'creator': {'id': 10907, 'name': 'Magusbear', 'banned': False, 'published': '2023-06-21T14:16:06.756921', 'actor_id': 'https://voyager.lemmy.ml/u/Magusbear', 'local': True, 'deleted': False, 'admin': False, 'bot_account': False, 'instance_id': 1}, 'community': {'id': 5, 'name': 'test', 'title': 'test', 'removed': False, 'published': '2023-06-11T22:04:16.113117', 'deleted': False, 'nsfw': False, 'actor_id': 'https://voyager.lemmy.ml/c/test', 'local': True, 'hidden': False, 'posting_restricted_to_mods': False, 'instance_id': 1}, 'creator_banned_from_community': False, 'counts': {'id': 41, 'post_id': 41, 'comments': 0, 'score': 1, 'upvotes': 1, 'downvotes': 0, 'published': '2023-06-21T15:48:55.752735', 'newest_comment_time_necro': '2023-06-21T15:48:55.752735', 'newest_comment_time': '2023-06-21T15:48:55.752735', 'featured_community': False, 'featured_local': False, 'hot_rank': 1728, 'hot_rank_active': 1728}, 'subscribed': 'NotSubscribed', 'saved': False, 'read': True, 'creator_blocked': False, 'my_vote': 1, 'unread_comments': 0}}
