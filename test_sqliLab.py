import requests

class SQLjection(object):
    def __init__(self):
        print()

    def jection(self,url,argument):
        res = requests.get(url,argument)
        print(res.url)
        # print(res.content.decode())

if __name__ == "__main__":
    sj = SQLjection()
    sj.jection("http://www.demosqlilab.io/Less-1/","id=1")
