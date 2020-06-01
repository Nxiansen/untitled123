from urllib.parse import urlparse
import argparse
url = 'http://www.abc.cn/jfjbmap/content/2016-01/03/node_2.htm'

urldic = urlparse(url)

print(urldic.path)

pathdict = urldic.path.split('/')

print(pathdict)
if __name__ == '__main__':
    a = 1
    b= 2
    v = 3
    c = 1
    for i in range(10):
        c += a ** 2
        print(c)