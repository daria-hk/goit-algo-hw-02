from collections import deque
def palindrom(word):
  stripWord = ''.join(list(map(lambda x: x.strip(), word.split())))
  if len(stripWord) > 1:
    word = deque(stripWord)
    if word.popleft() != word.pop():# for a quick check
      return f'{stripWord} is not a palindrome'
    else: #check if input word as the same as reversed input word
      reverse_the_word = deque(word)
      reverse_the_word.reverse()
      if word == reverse_the_word:
          return f'{stripWord} is a palindrome'
      else:
          return f'{stripWord} is not a palindrome'
  else:
      return f'input should be greater than 1'



#palindrom(' tneneet ')
#palindrom(' ktenet ')
#palindrom(' tenet ')
#palindrom(' anksna ')
palindrom(' anna ')
#palindrom(' a ')