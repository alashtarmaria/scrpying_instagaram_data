import instaloader
import csv

# Create an instance of Instaloader
loader = instaloader.Instaloader()

# Account names to fetch data for
account_names = ['mariaalashtar', 'atalaraleyna']

# Open CSV file to write data
with open('bio_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Username', 'Biography', 'Followers', 'Following', 'Posts'])

    # Iterate over each account name
    for account_name in account_names:
        # Load the profile of the user
        profile = instaloader.Profile.from_username(loader.context, account_name)
        
        # Get the username
        username = profile.username

        # Get the biography
        bio = profile.biography

        # Get the number of followers
        followers = profile.followers

        # Get the number of followings
        following = profile.followees

        # Get the number of posts
        posts = profile.mediacount

        # Write data to CSV
        writer.writerow([username, bio, followers, following, posts])

        # Print information
        print(f"Data for {username} saved.")

print("Biographical data saved to bio_data.csv")
