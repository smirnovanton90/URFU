

st = "Я помню чудное мгновенье:\n\
Передо мной явилась ты,\n\
Как мимолётное виденье,\n\
Как гений чистой красоты.\n\
\n\
В томленьях грусти безнадежной,\n\
В тревогах шумной суеты,\n\
Звучал мне долго голос нежный\n\
И снились милые черты.\n\
\n\
Шли годы. Бурь порыв мятежный\n\
Рассеял прежние мечты,\n\
И я забыл твой голос нежный,\n\
Твои небесные черты.\n\
\n\
В глуши, во мраке заточенья\n\
Тянулись тихо дни мои\n\
Без божества, без вдохновенья,\n\
Без слёз, без жизни, без любви.\n\
\n\
Душе настало пробужденье:\n\
И вот опять явилась ты,\n\
Как мимолётное виденье,\n\
Как гений чистой красоты.\n\
\n\
И сердце бьётся в упоенье,\n\
И для него воскресли вновь\n\
И божество, и вдохновенье,\n\
И жизнь, и слёзы, и любовь."

#print(st)

def grooming(a):
    literals = ['\n', ':', '.', ',', '-', '(', ')', '    ', '   ', '  ']
    for i in literals:
        a = a.replace(i, ' ')
    return a
                     

def splitter(a, b):
    return a.split(b), len(a.split(b))


def vocabulary(a):
   voc1 = splitter(grooming(a), ' ')[0]
   vocLowerCase = []
   for i in voc1:
      vocLowerCase.append(str(i).lower())
    
   vocLowerCase.remove('')

   vocUnique = sorted(set(vocLowerCase))
    
   finalVoc = {}
   for i in vocUnique:
      finalVoc[i] = vocLowerCase.count(i)
   return finalVoc
                     
print(vocabulary(st))