import funcoes, os ,requests

url = input('digite a sua url:')

pastas = []

def main (r,pastas):
    funcoes.criar_headers(r,pastas)

    if r.headers['Content-Type'] == 'text/plain':
        pastas += funcoes.criar_plain(r,pastas)
    
    if r.headers['Content-Type'] == 'text/html':
        pastas += funcoes.criar_html(r,pastas)
    
    if r.headers['Content-Type'] == 'text/css':
        pastas += funcoes.criar_css(r,pastas)
    
    if r.headers['Content-Type'] == 'text/javascript':
        pastas += funcoes.criar_javascript(r,pastas)
    
    if r.headers['Content-Type'] == 'image/jpeg':
        pastas += funcoes.criar_jpg(r,pastas)
    
    if r.headers['Content-Type'] == 'image/png':
        pastas += funcoes.criar_png(r,pastas)
    
    if r.headers['Content-Type'] == 'image/gif':
        pastas += funcoes.criar_gif(r,pastas)
    
    if r.headers['Content-Type'] == 'audio/mpeg':
        pastas += funcoes.criar_mpeg(r,pastas)
    
    if r.headers['Content-Type'] == 'video/mp4':
        pastas += funcoes.criar_mp4(r,pastas)
    
    if r.headers['Content-Type'] == 'application/json':
        pastas += funcoes.criar_json(r,pastas)
    
    if r.headers['Content-Type'] == 'application/xml':
        pastas += funcoes.criar_xml(r,pastas)
    
    if r.headers['Content-Type'] == 'application/pdf':
        pastas += funcoes.criar_pdf(r,pastas)

  
r = requests.get(url)
main(r,pastas)
