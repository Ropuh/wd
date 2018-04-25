#while/if ćwiczenie
liczba = [2,5,2,1,7,3,77,33,21,56,89,22,34,56,67,78,89,99,2,44,2,66,56,4,1,10,11,4,7,9,6,34,21,67,23,56,66,78,23,45,67,3,8,9,23,11,12,45,88,23,45,77,31,0,8,9,56,4,3,5,6]
#ile liczb
print (len(liczba))
#ile liczba 
maxLiczba = len(liczba)-2
zmienna = 1
i = 1
while zmienna < maxLiczba:
#    print (zmienna, ' ', liczba[zmienna],' ', liczba[zmienna+1], ' ' , liczba[zmienna+2])
    if liczba[zmienna] < liczba[zmienna+1]  and   liczba[zmienna+1] < liczba[zmienna+2]:
        print (i, '- pozycja ', zmienna, ' - ', liczba[zmienna],' ', liczba[zmienna+1], ' ' , liczba[zmienna+2])
        i+=1
        
    zmienna +=1
    
