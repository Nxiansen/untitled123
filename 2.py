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