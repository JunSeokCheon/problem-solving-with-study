# 10808 알파벳 찾기 알파벳(97,122), <find>
word = input()
alphabet = list(range(97,123))

for i in alphabet:
  print(word.find(chr(i)))