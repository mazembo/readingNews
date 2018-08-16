import pickle
import io
import pprint
import sys

def printing(filename):
    pkl_file = open(filename, "rb")
    links = pickle.load(pkl_file)
    for link in links:
        print link
    print len(links)

def main():
    printing(sys.argv[1])

if __name__ == "__main__":
    main()
