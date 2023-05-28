# python3

class Query:
    def __init__(self, query):
        self.type = query[0]  #Piešķir pirmo elementu
        self.number = int(query[1])  #Pārvērš otro elementu no vaicājuma par veselu skaitli un piešķir number"
        if self.type == 'add':
            self.name = query[2]  #Piešķir trešo elementu no vaicājuma atribūtam "name", ja ir "add"

def phone_book_manager(N, queries):
    phone_book = {}  # Izveido tukšu vārdnīcu, kas būs kā telefona grāmata

    for query in queries:  #ciklē cauri katram vaicājumam
        query_parts = query.split()  #Sadala vaicājumu atsevišķos elementos pēc atstarpēm

        if query_parts[0] == 'add':  #Ja vaicājuma pirmā daļa ir "add"
            phone_number = query_parts[1]  #Piešķir otru daļu atribūtam "phone_number"
            name = query_parts[2]  #Piešķir trešo daļu atribūtam "name"
            phone_book[phone_number] = name  #Pievieno telefona numuru un vārdu telefona grāmatas vārdnīcai

        elif query_parts[0] == 'del':  #Vaicājuma pirmā daļa ir del
            phone_number = query_parts[1]  #Piešķir otru daļu 'phone_number'
            if phone_number in phone_book:  #Pārbauda vai telefona numurs ir telefona grāmatā
                del phone_book[phone_number]  #Izdzēš telefona numuru un saistīto vārdu no telefona grāmatas

        elif query_parts[0] == 'find':  #ja vaicājuma pirmā daļa ir "find"
            phone_number = query_parts[1]  #Piešķir otru daļu "phone_number"
            if phone_number in phone_book:  #Pārbauda vai telefona numurs ir telefona grāmatā
                print(phone_book[phone_number])  #Izdrukā vārdu, kas saistīts ar telefona numuru
            else:
                print('not found')  #Drukā "not found", ja telefona numurs nav telefona grāmatā

N = int(input())  #Lasīt N vērtību no ievades
queries = [input() for _ in range(N)]  #Lasīt vaicājumus no ievades

phone_book_manager(N, queries)  #Saukt phone_book_manager funkciju ar ievades vērtībām

