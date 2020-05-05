'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 

Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 

So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

'''
import time
import os

start = time.time()

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'p22_names.txt')
    with open(my_file) as f:
        contents = f.read().lower()
        name_list = sorted(contents.replace('\"', '').split(','))

    total = 0

    # print(name_list)
    for i in range(len(name_list)):
        score = 0
        letters = [str(c) for c in name_list[i]]
        for j in letters:
            score += ord(j)%32

        total += (score * (i+1))
        pass

    print("Total: " + str(total))

if __name__ == '__main__':
    main()

print("Time elapsed: " + str(time.time() - start) + " seconds")

'''
> python3 problem22.py    
Total: 871198282
Time elapsed: 0.012995004653930664 seconds

'''
