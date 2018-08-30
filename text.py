import random

class Sashimi:

  def __init__(self, number):
    self.number = number

    self.normal = []
    self.special = []
    self.rea = []
    self.super_special = []
    self.pre_text = []


  def open_text(self):
    with open("./texts/normal.txt", "r") as f:
            self.normal = [line.replace("\n", "") for line in f.readlines()]
    with open("./texts/special.txt", "r") as f:
            self.special = [line.replace("\n", "") for line in f.readlines()]
    with open("./texts/rea.txt", "r") as f:
            self.rea = [line.replace("\n", "") for line in f.readlines()]
    with open("./texts/super_special.txt", "r") as f:
            self.super_special = [line.replace("\n", "") for line in f.readlines()]
    with open("./texts/pre_text.txt", "r") as f:
            self.pre_text = [line.replace("\n", "") for line in f.readlines()]

  def result(self):
    
    N = random.randrange(1000)

    if N == 343:
      text = random.choice(self.super_special)
      self.super_special.remove(text)
    elif N < 30:
      text = random.choice(self.rea)
      self.rea.remove(text)
    elif N < 60:
      text = random.choice(self.special)
      self.special.remove(text)
    else:
      p_text = random.choice(self.pre_text)
      n_text = random.choice(self.normal)
      self.pre_text.remove(p_text)
      self.normal.remove(n_text)
      text = p_text + n_text
    
    return text

  
  def make_tweet(self):

    self.open_text()

    tweet_text = "\n"

    if self.number > 1:
      tweet_text += "【おさしみ10連】"

      for i in range(1, self.number + 1):
        tweet_text += "\n" + str(i) + ". "
        tweet_text += self.result()

    else:
      tweet_text += self.result()

    return tweet_text
