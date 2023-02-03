import typesense

client = typesense.Client({
  'nodes': [{
    'host': 'c4qsg2xpi8jv9dmzp-1.a1.typesense.net', # For Typesense Cloud use xxx.a1.typesense.net
    'port': '443',      # For Typesense Cloud use 443
    'protocol': 'https'   # For Typesense Cloud use https
  }],
  'api_key': '',
  'connection_timeout_seconds': 2
})


books_schema = {
  'name': 'books',
  'fields': [
    {'name': 'title', 'type': 'string' },
    {'name': 'authors', 'type': 'string[]', 'facet': True },

    {'name': 'publication_year', 'type': 'int32', 'facet': True },
    {'name': 'ratings_count', 'type': 'int32' },
    {'name': 'average_rating', 'type': 'float' }
  ],
  'default_sorting_field': 'ratings_count'
}

client.collections.create(books_schema)



# with open('/tmp/books.jsonl') as jsonl_file:
#     count = sum(1 for line in jsonl_file)
# print("Number of books in books.jsonl:", count)


with open('/tmp/books.jsonl') as jsonl_file:
    client.collections['books'].documents.import_(jsonl_file.read().encode('utf-8'))

search_parameters = {
'q'         : 'harry potter',
'query_by'  : 'title',
'sort_by'   : 'ratings_count:desc'
}

response = client.collections['books'].documents.search(search_parameters)
print(response)
