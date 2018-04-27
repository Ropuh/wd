#Skrypt tworzacy katalogi na bazie nazw plików i przesuwają do nich pliki
#wykorzystanie importu i pętli na lista składjących się z stringów
import os
import shutil
import fnmatch
#listaPlikow = os.listdir('.' )
#print(listaPlikow)
#print(os.path.basename(__file__))
areYouSure = ''
areYouSure = input('Ropocząć przesuwanie? (Tak/Nie)')
#print(areYouSure)
#print(len(fnmatch.filter(os.listdir('.'), '*.jpg')))
#liczbaPlikow = os.listdir('.')
liczbaPlikow = fnmatch.filter(os.listdir('.'), '*.jpg')
if areYouSure == 'Tak' or areYouSure == 'tak':
    print ('Rozpoczynam: ')
    liczba=1
    for plik in liczbaPlikow:   
        #print (liczba,len(liczbaPlikow))
        #print (liczba)
        #if plik != os.path.basename(__file__) and ( os.path.isfile(plik) and plik.endswith('.jpg') ):
        #if plik != 'mk.py' and os.path.isfile(plik):
            #print ( plik , ' ', plik[:-4], ' ', plik[:-2])
            #tworzenie katalogu usera / brak reakcji jesli istnieje
            os.makedirs (plik[:-14], exist_ok = True)
            #move pliku
            try:
                #przesuniecie
                #print('OK')
                shutil.move( plik , plik[:-14])
                print(round(liczba/len(liczbaPlikow)*100,1),'% - Plik: ', plik, 'do: ', plik[:-14], end='\r')
                #print(liczba)
                
            except:
                #jesli przesuniecie zwraca błąd lub przerwano (CTRL+C)
                print ('UWAGA przerywam: ', plik, ' istnieje!')
                break
            liczba+=1
else:
    print('Nic nie robie!')
print('\nZakończono działanie...', end='\n')
