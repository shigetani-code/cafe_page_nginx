#import bluepy
import urllib.request, urllib.parse

#scanner = bluepy.btle.Scanner(0)
#devices = scanner.scan(3)

#count = 0
#for i in devices:
#    addr = device.addr
#    hash_str = str(df_t) + addr
#    hash_str = hashlib.sha256(hash_str.encode()).hexdigest()
#    count += 1

addr = "1a:2b:3c:46:2b:3c 1a:2b:3c:46:2b:3c 1a:2b:3c:4e:5f:6g"
count = 60

def post_message(addr, count):
    print("post")
    data = {}
    data["addr"] = addr
    data["count"] = count
    url = "http://127.0.0.1:4231"
    try:
        data = urllib.parse.urlencode(data).encode("utf-8")
        req = urllib.request.Request(url, data=data, method="POST")
        with urllib.request.urlopen(req) as res:
            res = res.read().decode("utf-8")
            print(res)
    except:
        print('Error')

if __name__=='__main__':
    post_message(addr,count)