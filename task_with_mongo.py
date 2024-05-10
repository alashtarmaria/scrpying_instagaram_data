import instaloader
from pymongo import MongoClient


loader = instaloader.Instaloader()

account_names = ['mariaalashtar', 'atalaraleyna','njema.sh' ,'python.hub']

# Connect to MongoDB
client = MongoClient('localhost', 27017)  
db = client['instagram']  
collection = db['insta_data'] 

for account_name in account_names:
    profile = instaloader.Profile.from_username(loader.context, account_name)

    username = profile.username

    bio = profile.biography

    followers = profile.followers

    following = profile.followees

    posts = profile.mediacount

    data = {
        'username': username,
        'biography': bio,
        'followers': followers,
        'following': following,
        'posts': posts
    }

    collection.insert_one(data)

    print(f"Data for {username} saved.")

print("Biographical data saved to MongoDB collection 'insta_data'")
