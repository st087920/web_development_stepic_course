def wsgi_aplication(environ, start_response):
  status = '200 OK'
  headers = [('text/plain')]
  # body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
  body = "\n".join([i for i in environ['QUERY_STRING'].split('&'))
  start_response(status, headers)
  return body