import requests
import random
import time

headers = {'Host': 'ecast.jackboxgames.com', 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'}



alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabetlen = len(alphabet)
codelen = 4
codeIndexArray = [0] * codelen
codes = []
for i in range(pow(alphabetlen, codelen) - 1):
    CIAIndex = codelen-1
    codeIndexArray[CIAIndex] += 1
    while codeIndexArray[CIAIndex] >= alphabetlen:
        codeIndexArray[CIAIndex] = 0
        CIAIndex -= 1
        codeIndexArray[CIAIndex] += 1
    code = [0] * codelen
    for j in range(codelen):
        code[j] = alphabet[codeIndexArray[j]]
    codes.append(''.join(code))
    
random.shuffle(codes)


for i in range(len(codes)):
    r = requests.get("https://ecast.jackboxgames.com/api/v2/rooms/" + str(codes[i]), headers = headers)
    if r.status_code != 404:
        print(str(codes[i]) + "  Game Started: " + str(r.json()['body']['locked']))
    time.sleep(3)
