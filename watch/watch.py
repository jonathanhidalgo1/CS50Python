import re
import sys

'''
<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" 
frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
'''

def main():
    print(parse(input("HTML: ").replace(" ", "")))


def parse(s):

    match = re.search(r"(\w*)(https?://)(www.)(youtube.)(com)(/embed/)(\w+)", s)
    if match:
        return f"https://youtu.be/{match.group(7)}"





if __name__ == "__main__":
    main()