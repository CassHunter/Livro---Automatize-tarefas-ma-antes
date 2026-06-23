allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    '''Retorna a soma de item do dicionarios guests'''
    numBrought = 0
    for k, v in guests.items():  #percorre as k=keys e v=values do dicionario guests
        numBrought += v.get(item, 0)  # incrementa o valor se houver item, senao define 0
    return numBrought


print('Number of things being brought:')
print('- Apples      '+str(totalBrought(allGuests, 'apples')))
print('- Cups        '+str(totalBrought(allGuests, 'cups')))
print('- Cakes        '+str(totalBrought(allGuests, 'cakes')))
print('- Ham Sandwiches        '+str(totalBrought(allGuests, 'ham sandwiches')))
print('- Apple Pies        '+str(totalBrought(allGuests, 'apple pies')))
print('- Icecream        '+str(totalBrought(allGuests, 'icecream')))