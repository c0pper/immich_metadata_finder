from pathlib import Path
import re

#  Remove emoji from files so that google-photos-takeout-date-fixer doesn't crash
emoji_pattern = re.compile("["
                        u"\U0001F600-\U0001F64F"  # emoticons
                        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                        u"\U0001F680-\U0001F6FF"  # transport & map symbols
                        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                        u"\U00002702-\U000027B0"
                        u"\U000024C2-\U0001F251"
                        u"🦉"
                        "]+", flags=re.UNICODE)

def remove_emoji(string):
    return emoji_pattern.sub(r'', string)

folder = Path(r"E:\\Google Takeout\\photos-12-23\\takeout-20231224T114747Z-001\\Takeout\\Google Photos")
for f in folder.glob("**/*"):
    # print(f.name)
    if emoji_pattern.search(f.name):
        # print(f.name)
        new_name = remove_emoji(f.name)
        new_name = f"{f.parent}\\{new_name}"
        print(f"renaming {f.name} to {new_name}")
        f.rename(new_name)
