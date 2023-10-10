import requests,hashlib,threading,random,time

def translate(ori):# 网上搞来没有防爬的小网站，乐
    url = r"https://translate-api-fykz.xiangtatech.com/translation/webs/index"
    data ={
        'appid': '105',
        'sgid': 'auto',
        'sbid': 'auto',
        'egid': 'auto',
        'ebid': 'auto',
        'content': ori,
        'type': '2'
    }

    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.55"
    }
    res = requests.post(url, data=data,headers=headers).json()
    print(f"{ori}: {res['by']}")

def api_translate(ori):
    time.sleep(random.random()*5)
    app_id = "20231006001838395"
    api_key = "2V2VIzuB8c8g8dI8VqLD"
    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    salt = str(random.randint(1,65536))
    sign = hashlib.md5((app_id+ori+salt+api_key).encode('utf-8')).hexdigest()
    data = {
        'q': ori,
        'from': 'auto',
        'to': 'auto',
        'appid': app_id,
        'salt': salt,
        'sign': sign,
        'Content-Type':'application/x-www-form-urlencoded'
    }
    res = requests.post(data=data,url=url).json()
    try:
        print(f"{ori}: {res['trans_result'][0]['dst']}")
    except Exception:
        print(res)

if __name__ == "__main__":
    ori = ["苹果","梨","香蕉"]
    for word in ori:
        subthread = threading.Thread(target=api_translate,args=(word,))
        subthread.start()
