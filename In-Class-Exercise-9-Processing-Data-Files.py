from collections import namedtuple
from pprint import pprint

def main():


    infile = open("yob2014.txt")
    count = 0
    lines = infile.readlines()
    for line in lines:
        if ',F,' in line:
            count +=1
            words = line.split(',')
            for word in words:
                print(repr(word.strip()))
    print('coun=', count)
    print('lines=', len(lines))
    infile.close()

if __name__ == "__main__":
    main()
