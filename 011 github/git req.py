from tokenize import Token
import requests 

dado = requests.get("https://github.com/2025-2-gbat-ProgRedes/codes/blob/main/pratica-usando-github.txt")
#print((dado.headers))
#dado = dado.json()
#print(dado.keys())
dado2 = requests.get("https://api.github.com/repos/gbat/pr2025/contents/README.md")
dado3 = requests.get("https://api.github.com/repos/2025-2gbat-ProgRedes/codes/contents/README.md")
#print(dado3.content)
# curl -v https://api.github.com/repos/2025-2-gbat-ProgRedes/codes/contents/README.md

dado4 = requests.get('https://api.github.com/repos/2025-2-gbat-ProgRedes/codes/contents/README.md', headers={ "Authorization": Bearer YourToken })
print(dado4.text)