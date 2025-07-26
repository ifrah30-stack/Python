from instaloader import Instaloader

loader = Instaloader()
profile = input("Enter username: ")
loader.download_profile(profile, profile_pic_only=True)
