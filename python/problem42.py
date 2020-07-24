import time
import os

start = time.time()

def read_words():
  THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
  my_file = os.path.join(THIS_FOLDER, 'p42_words.txt')
  with open(my_file) as f:
    contents = f.read().lower()
    word_list = sorted(contents.replace('\"', '').split(','))
  
  return word_list

def num_of_triangle_words():
  number = 1
  triangle_nums = [1]
  triangle_num_count = 0

  for i in range(2, 30):
    number += i
    triangle_nums.append(number)

  words = read_words()

  for word in words:
    word_value = 0
    for char in word:
      word_value += (ord(char) - 96)
    
    if word_value in triangle_nums:
      triangle_num_count += 1

  return triangle_num_count

def main():
  print(num_of_triangle_words())
  pass

if __name__ == '__main__':
  main()

print("Time elapsed: {} seconds".format(time.time() - start))