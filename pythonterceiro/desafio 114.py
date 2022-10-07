import urllib.request
import urllib.error

link = 'https://www.google.com.br'
try:
    urllib.request.urlopen(link)
    print('site acessível')

except urllib.error.URLError:
    print('site inascessível')
