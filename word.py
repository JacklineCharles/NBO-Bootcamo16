def words(words):
   try:
       words=words.split()
       L={}
       for word in words:
           if word.isdigit():
               if int(word) in L:
                 L[int(word)]=L[int(word)]+1
               else:
                   L[int(word)]=1
           else:
               if word in L:
                   L[word]=L[word]+1
               else:
                   L[word]=1
       return L
   except Exception:
       return 'invalid'

print(words("hello there we hello we are people from planet earth 1 2 2 3"))
