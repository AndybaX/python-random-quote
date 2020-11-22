import random
def primary():
  #  print("Keep it logically awesome Dude.")
  #  print('Hello')
  print('did')
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 1
  rnd = random.randint(0, last)
  # print(quotes)
  #print(quotes[-1])
  print(quotes[rnd])
  # adding a comment

if __name__== "__main__":
  primary()
