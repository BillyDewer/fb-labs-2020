import codecs

alphabet={
'А':0,  'а':0,
'Б':1,  'б':1,
'В':2,  'в':2,
'Г':3,  'г':3,
'Д':4,  'д':4,
'Е':5,  'е':5,
'Ё':5,  'ё':5,
'Ж':6,  'ж':6,
'З':7,  'з':7,
'И':8,  'и':8,
'Й':9,  'й':9,
'К':10,  'к':10,
'Л':11,  'л':11,
'М':12,  'м':12,
'Н':13,  'н':13,
'О':14,  'о':14,
'П':15,  'п':15,
'Р':16,  'р':16,
'С':17,  'с':17,
'Т':18,  'т':18,
'У':19,  'у':19,
'Ф':20,  'ф':20,
'Х':21,  'х':21,
'Ц':22,  'ц':22,
'Ч':23,  'ч':23,
'Ш':24,  'ш':24,
'Щ':25,  'щ':25,
'Ъ':26,  'ъ':26,
'Ы':27,  'ы':27,
'Ь':28,  'ь':28,
'Э':29,  'э':29,
'Ю':30,  'ю':30,
'Я':31,  'я':31
}
alphabet_len=32

numbers={
0:'А',  
1:'Б',  
2:'В',  
3:'Г',  
4:'Д',  
5:'Е', 
6:'Ж',  
7:'З',  
8:'И',  
9:'Й',  
10:'К', 
11:'Л',  
12:'М',  
13:'Н',  
14:'О', 
15:'П', 
16:'Р',  
17:'С', 
18:'Т',  
19:'У',
20:'Ф', 
21:'Х', 
22:'Ц', 
23:'Ч', 
24:'Ш', 
25:'Щ', 
26:'Ъ', 
27:'Ы', 
28:'Ь', 
29:'Э', 
30:'Ю',
31:'Я'
}

def get_numbers_of_characters(string):
       global alphabet
       result=[]
       for char in string:
              if char in alphabet.keys():
                     result.append(alphabet[char])
       return result
def get_characters_of_numbers(arr):
       global numbers
       result=''
       for n in arr:
              if n in numbers.keys():
                     result+=numbers[n]
       return result
def num(char):
       if char in alphabet.keys():
              return alphabet[char]
       else:
              return -1
def char(num):
       if num in numbers.keys():
              return numbers[num]
       else:
              return -1


char_counts={
'А':0,
'Б':0,
'В':0,
'Г':0, 
'Д':0, 
'Е':0,
'Ж':0, 
'З':0, 
'И':0,
'Й':0, 
'К':0, 
'Л':0,
'М':0,
'Н':0, 
'О':0, 
'П':0,
'Р':0,
'С':0,
'Т':0,
'У':0,
'Ф':0,
'Х':0,
'Ц':0,
'Ч':0, 
'Ш':0,
'Щ':0,
'Ъ':0,
'Ы':0,
'Ь':0,
'Э':0,
'Ю':0,
'Я':0
}
frequencies={
'О':0.10983,
'Е':0.08496,
'А':0.07998,
'И':0.07367,
'Н':0.067,
'Т':0.06318,
'С':0.05473,
'Р':0.04746,
'В':0.04533,
'Л':0.04343,
'К':0.03486,
'М':0.03203,
'Д':0.02977,
'П':0.02804,
'У':0.02615,
'Я':0.02001,
'Ы':0.01898,
'Ь':0.01735,
'Г':0.01687,
'З':0.01641,
'Б':0.01592,
'Ч':0.0145,
'Й':0.01208,
'Х':0.00966,
'Ж':0.0094,
'Ш':0.00718,
'Ю':0.00639,
'Ц':0.00486,
'Щ':0.00361,
'Э':0.00331,
'Ф':0.00267,
'Ъ':0.00037
}
freq_rating=[
'О',
'Е',
'А',
'И',
'Н',
'Т',
'С',
'Р',
'В',
'Л',
'К',
'М',
'Д',
'П',
'У',
'Я',
'Ы',
'Ь',
'Г',
'З',
'Б',
'Ч',
'Й',
'Х',
'Ж',
'Ш',
'Ю',
'Ц',
'Щ',
'Э',
'Ф',
'Ъ'
]

def get_counts_in_text(text):
       cur_counts = char_counts.copy()
       for char in text:
              cur_counts[char.upper()]+=1
       return cur_counts
def calculate_INDEX(text):
       cur_counts = get_counts_in_text(text)
       summ=0
       for i in cur_counts:
              summ+=cur_counts[i]*(cur_counts[i]-1)
       INDEX=summ*1.0/(len(text)*(len(text)-1))
       return INDEX
       
