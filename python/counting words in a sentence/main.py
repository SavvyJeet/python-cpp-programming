def count_words(sent):
  count = 0
  words = sent.split()
  for word in words:
    if word in words:
      count+=1
      
