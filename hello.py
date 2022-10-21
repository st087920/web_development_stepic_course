def wsgi_aplication(environ, start_response):
  status = '200 OK'
  body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
  # body = "\n".join([i for i in environ['QUERY_STRING'].split('&')])
  headers = [
        ('Content-type', 'text/plain'),
    ]
  start_response(status, headers)
  return body
