# import instaloader

# ig = instaloader.Instaloader()

# user = "mariaalashtar"

# ig.download_profile(user, profile_pic_only=False)







# import instaloader

# # Create an instance of Instaloader
# loader = instaloader.Instaloader()

# # List of usernames
# usernames = ['mariaalashtar', 'atalaraleyna', 'njema.sh', 'python.hub']

# # Loop through each username
# for username in usernames:
#     try:
#         # Download the profile picture
#         loader.download_profile(username, profile_pic_only=True)
#         print(f"Profile picture downloaded for {username}")
#     except Exception as e:
#         print(f"Error downloading profile picture for {username}: {e}")



import instaloader
import os

# Create an instance of Instaloader
loader = instaloader.Instaloader()

# List of usernames
usernames = ['mariaalashtar', 'atalaraleyna', 'njema.sh', 'python.hub']

# Directory to save profile pictures
save_dir = 'profile_pictures'
os.makedirs(save_dir, exist_ok=True)  # Create directory if it doesn't exist

# Change the current working directory to the save directory
os.chdir(save_dir)

# Loop through each username
for username in usernames:
    try:
        # Download the profile picture
        loader.download_profile(username, profile_pic_only=True)
        print(f"Profile picture downloaded for {username}")
    except Exception as e:
        print(f"Error downloading profile picture for {username}: {e}")

# Change back to the original working directory
os.chdir('..')

print(f"All profile pictures saved to '{save_dir}' directory.")

