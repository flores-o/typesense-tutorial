import typesense

client = typesense.Client({
  'nodes': [{
    'host': 'xxx.a1.typesense.net', # For Typesense Cloud use xxx.a1.typesense.net
    'port': '443',      # For Typesense Cloud use 443
    'protocol': 'https'   # For Typesense Cloud use https
  }],
  'api_key': 'T8Vab724UkIOVVxIrfQAovOFkwv34LDr',
  'connection_timeout_seconds': 2
})
