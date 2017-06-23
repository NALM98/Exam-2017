import os
 
for root, dirs, files in os.walk('.\\news\\'):
    for f in files:
        with open (os.path.join(root, f), 'r', encoding = 'cp1251') as text:
            words = text.read()
            print(f, '\t', words.count('<ana lex='))
