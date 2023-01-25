import re

teste = input("> ").replace(" ", "")
match = re.search(r"(\w*)(https://)(www.)(youtube.)(com)(/embed/)(\w+)", teste)
if match:
    print(f"https://youtu.be/{match.group(7)}")