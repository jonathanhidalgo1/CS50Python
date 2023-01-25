import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", help="number of times to meow", type=str)
parser.add_argument("-d", help="number of times to dog")
parser.add_argument("-c", help="number of times to cat")
args = parser.parse_args()

print(args.n)
    
