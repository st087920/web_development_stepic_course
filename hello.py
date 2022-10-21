def wsgi_aplication(environ, start_response):
  status = '200 OK'
  body = byte("\n".join([i for i in environ['QUERY_STRING'].split('&')]), 'ascii')  
  # body = "\n".join([i for i in environ['QUERY_STRING'].split('&')])
  headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(body)))
    ]
  start_response(status, headers)
  return body
