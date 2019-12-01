import pandas as pd
import requests
import json
import time
import random

def main():
    data = pd.DataFrame(columns=['com_name','born','close','live_time','total_money','cat_name','com_prov','closure_type'])
    for i in range(1,20): #设置爬取N页
        url= 'https://www.itjuzi.com/api/closure?com_prov=&fund_status=&sort=&page='+ str(i)
        headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0"}
        proxies = { "http": "http://27.152.8.26:9999", "https": "http://27.152.8.26:9999", } 
        #html = requests.get(url=url,headers=headers,proxies=proxies)

        #url = 'https://www.baidu.com/'
        html = requests.get(url=url,headers=headers).content
        print(i)
        doc = json.loads(html.decode('utf-8'))['data']['info']
        for j in range(10): #一页10个死亡公司
            data = data.append({'com_name':doc[j]['com_name'],'born':doc[j]['born'],'cat_name':doc[j]['cat_name'],
                    'closure_type':doc[j]['closure_type'],'close':doc[j]['com_change_close_date'],'com_prov':doc[j]['com_prov'],
                    'live_time':doc[j]['live_time'],'total_money':doc[j]['total_money']},ignore_index=True)
            time.sleep(random.random())
    data.to_csv('./res/company.csv')
    return data

if __name__ == "__main__":
    main()