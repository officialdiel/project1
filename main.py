TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
oddelovac = '-' * 40
Title = 0
Upper = 0
Lower = 0
Numeric = 0
Temp = 0
SumNum = 0

USERS =  {'bob': '123',
        'ann': 'pass123',
        'mike': 'password123',
         'liz': 'pass123',
        }
username = input('username: ')
password = input('password: ')
number_text = list(range(0, len(TEXTS)))

if USERS.get(username) == password:
    print(oddelovac)
if not USERS.get(username) == password:
    print('Username or password is wrong!')
    exit()

print('Welcome to the app,', username)
print(f'We have {len(number_text)} texts to be analyzed')
print(oddelovac)


cisla = input('Enter a number btw. 1 and 3 to select: ')
if cisla in ['1','2','3']:
    pass
else:
    print('Not available')
    exit()
print(oddelovac)

if cisla == '1':
    TEXT = TEXTS[0]
elif cisla == '2':
    TEXT = TEXTS[1]
elif cisla == '3':
    TEXT = TEXTS[2]
else:
    print('wrong')
TEXT = TEXT.translate({ord(c): None for c in ',.?!'})
Count_words = int(len(TEXT.split()))
for Word in TEXT.split():
    if Word.istitle():
        Title = Title + 1
    elif Word.isupper():
        Upper = Upper + 1
    elif Word.islower():
        Lower = Lower + 1
    elif Word.isnumeric():
        Numeric = Numeric + 1
    else:
        pass
for Word in TEXT.split():
    if (Word.isnumeric()):
        Temp += Word
    else:
        SumNum += int(Temp)
        Temp = '0'

print('There are', Count_words, 'words in the selected text.')
print('There are', Title, 'titlecase words.')
print('There are', Upper, 'uppercase words.')
print('There are', Lower, 'lowercase words.')
print('There are', Numeric, 'numeric strings.')
print('The sum of all the numbers', SumNum)
print(oddelovac)

TEXT_graph = []
for x in TEXT.split():
    word_length = len(x)
    TEXT_graph.append(word_length)

i = TEXT_graph
TEXT_graph_dict = {x:i.count(x) for x in i}

TEXT_graph_dict_sort = sorted(TEXT_graph_dict.items())

print('LEN| OCCURENCES        |NR.')
print(oddelovac)
LEN = ''
OCC = ''
NR = ''
