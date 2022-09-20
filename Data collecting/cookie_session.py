from requests import Session, request, get
from bs4 import BeautifulSoup

session = Session()

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
resp = get('https://nid.naver.com/nidlogin.login')
dom = BeautifulSoup(resp.text, 'html.parser')
form = dom.select_one('form')
inputList = form.select('input[name]')

c = ('''
SB_MODE plusdeal	www.naver.com	/	세션	15						Medium	
NID_JKL	q/dtgTttHDuM7WRMnbvITnV5Pg/WjZPF7/f7VNUj1Qk=	.naver.com	/	세션	51		✓				Medium	
NID_SES	AAABmna16m3vbX7mKa+6GebwtHMBtKyFbs6DTPkAV7fRoRQEzG48eiTNCRqDnn1Uc+47/XI9vMvPvhFssrVaylGGwJuU3lI63yO90vqKjoaaxOVRjpNwDVUuS3uVidv3i7Y5dd0hUL/BoEdJ56vew2ZKCk36OSjTYuNwOzgJiWOY9lOY1loG590Hf2uIe8uPeTNXRgYVOA3rrXPArPHaim3BZqovbKVn5RRccvW0cMO//mWMqlcWgKahCFOEHFknHVNY4wMmZri4r0zc/mp2cz9Rl+uiQR6BxLgyVXfFmLaxzhH3vIswuyeyK8oj/Dh687g4NK7rvfyQFSy+dVkFta0HTzJY4HWXexqFALyqNgm16u7aAo/CvoYfuQNkPFt95R4HyebGPbrLpIpiYzmZcgNQEYqb0sC5j/sPEIbXJeBxeOdw6HcqQCc41I/q9o7GmM4wLumnoD+8e36N8NeZGVViziYxnE3vIQz3nxA2sW4it52GoxLIFC4uilcFBQF9Nz5VKzy79nBCifTAz+puly3dQ1S40m3K3eRxqMHBhMT9oFau	.naver.com	/	세션	567						Medium	
NID_AUT	JJ/fLLTzDZKJITdStrBPEgo7GaFCQAS8rkuyqq8w3NDI0oFXPUDjMgFMHJbPfgFL	.naver.com	/	세션	71	✓					Medium	
nid_inf	1549667697	.naver.com	/	세션	17						Medium	
NNB	ZB4I5EXDFUUWG	.naver.com	/	2023-10-25T03:06:09.095Z	16		✓	None			Medium	
PM_CK_loc	99770fda1fc68c0bdfc0549212eba9e4fc87147f612fe73e94e10fa875e35850	www.naver.com	/	2022-09-21T03:04:58.817Z	73	✓					Medium	
''').split('\n')
for _ in c:
    if len(_) > 0:
        tokens = _.split('\t')
        # print(tokens)

    cookies = {_.split('\t')[0]: _.split('\t')[1] for _ in c if len(_) > 0}

resp = get('https://mail.naver.com', headers=headers, cookies=cookies)

for k, v in cookies.items():
    session.cookies.set(k,v)

print(session.get('https://mail.naver.com', headers=headers).text)
# [.name _ccr(1st.from)]  [.subject ]
