"""
--> Binary Search Algorithm(Ikili Arama Algoritmasi)

Sirali olarak verilen bir listeden, verilen bir eleman bulunur iken aranacak eleman,bulununcaya kadar
listenin ortasindaki eleman ile karsilastirilir, ona gore aranacak liste duzenenir.
Aranan eleman listenin orta elemanindan buyuk ise liste ortadan ikiye bolunerek buyuk parcasi alinir,
daha kucuk ise listenin kucuk olan kismi alinir.

"""


def binary_search(a_list, item):  # parametre olarak arama yapilacak liste ve aranacak eleman istenir

    first = 0  # aranacak listenin ilk elemaninin indexi
    last = len(a_list)-1  # aranacak listenin son elemaninin indexi
    found = False  # flag

    while first <= last and not found:  # liste sona ermedikce ve aranan eleman bulunmadikca devam
        mid = (first+last) // 2  # aranacak indexlerin ortasi(int)
        if item == a_list[mid]:  # aranacak olan eleman ortadaki liste elemanina esit ise
            found = True  # bulunma durumu >> while biter (sartlari saglanmiyor)
        elif item > a_list[mid]:  # aranan eleman liste ortasindaki elemandan buyuk ise
            first = mid+1  # aranacak listenin ilk elemani ortanin bir fazlasina esitlenir
        else:  # aranan eleman listenin orta elemanindan kucuk ise
            last = mid-1  # aranacak listenin son elemani orta elemanin bir eksigine esitlenir
    return found
