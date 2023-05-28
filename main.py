# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]
    
    def phone_book_manager(N, queries):
    phone_book = {}

    for query in queries:
      query_parts = query.split()
    
      if query_parts[0] == 'add':
         phone_number = query_parts[1]
         name = query_parts[2]
         phone_book[phone_number] = name
   elif query_parts[0] == 'del':
         phone_number = query_parts[1]
          if phone_number in phone_book:
          del phone_book[phone_number]
        
   elif query_parts[0] == 'find':
     phone_number = query_parts[1]
       if phone_number in phone_book:
          print(phone_book[phone_number])
       else:
          print('not found')

N = int(input())
queries = [input() for _ in range(N)]
phone_book_manager(N, queries)

