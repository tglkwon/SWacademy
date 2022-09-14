from urllib import robotparser
parser = robotparser.RobotFileParser()
parser.set_url('https://news.naver.com/robots.txt')
parser.read()
# print(parser.can_fetch('*',  '/main/imagemontage')) # => False
# print(parser.can_fetch('Yeti',  '/main/imagemontage')) # => True


from urllib.request import Request, urlopen
response = urlopen('https://www.google.com')
# print(type(response))
content = response.read()

from html import escape, unescape
# HexaDecimal -> Ampersand Encoding
# 16진 코드    -> Escape(html entities)
#             <- unescape
# 문자열 <-> 바이트(encoding/decoding)과 비슷하다.
url = unescape(content.decode('utf8'))
print(url)

url = 'https://www.google.com/search?q=%ED%95%9C%EA%B0%80%EC%9D%B8&rlz=1C1CHBF_enKR819KR819&oq=%ED%95%9C%EA%B0%80%EC%9D%B8&aqs=chrome..69i57j69i61l2.1079j0j15&sourceid=chrome&ie=UTF-8'
url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%95%9C%EA%B0%80%EC%9D%B8'
url = 'https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%ED%95%9C%EA%B0%80%EC%9D%B8'
response = urlopen(url)
# print(type(response), response.status, response.reason, response.getheaders())
print(response.read().decode('utf8'))