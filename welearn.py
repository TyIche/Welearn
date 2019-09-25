import requests
from bs4 import BeautifulSoup
def getinfo(url):
    vk = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36'}
    try:
        r = requests.get(url,headers=vk,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '0'
def work(u,x,y,z,html):
    soup = BeautifulSoup(html)
    flag = 0
    #find 1
    for i in soup.find_all('et-choice'):
        if(i.parent.name=='et-mobile-only'):
            continue
        if(flag == 0):
            print()
            flag = 1
            print("Unit=%s x=%s y=%s z=%s"%(u,x,y,z))
        print(i.get('key'))
    #find 2
    for i in soup.find_all('et-blank'):
        if(i.parent.name=='et-mobile-only'):
            continue
        if(i.string and flag == 0):
            print()
            flag = 1
            print("Unit=%s x=%s y=%s z=%s" %(u,x,y,z))
        if(i.string):
            print(i.string)
    #find 3
    for i in soup.find_all('et-reference'):
        if(i.parent.name=='et-mobile-only'):
            continue
        #print(i.attrs['title'])
        if(i.get('title') != 'Reference'):
            continue
        
        for j in i.children:
            #print(j.name)
            if(j.name != 'ol'):
                continue
            for k in j.children:
                if(flag == 0):
                    print()
                    flag = 1
                    print("Unit=%s x=%s y=%s z=%s\n" %(u,x,y,z))
                print(k.string)   
def main():
    url1 = 'https://centercourseware.sflep.com/inspire%203/data/'\
    
    #3
    for u in range(13,18):
        for x in range(1,7):
            #print(url1+str(u)+'/'+str(x)+'.html')
            html = getinfo(url1+str(u)+'/'+str(x)+'.html')
            #print(html)
            if(html!='0'):
                work(u,x,0,0,html)
            for y in range(1,5):
                #print(url1+str(u)+'/'+str(x)+'-'+str(y)+'.html')
                html = getinfo(url1+str(u)+'/'+str(x)+'-'+str(y)+'.html')
                #print(html)
                if(html!='0'):
                    work(u,x,y,0,html)
                for z in range(1,6):
                    #print(url1+str(u)+'/'+str(x)+'-'+str(y)+'-'+str(z)+'.html')
                    html = getinfo(url1+str(u)+'/'+str(x)+'-'+str(y)+'-'+str(z)+'.html')
                    #print(html)
                    if html !='0':
                        work(u,x,y,z,html)
                #url = last
    #f = open("嘤语答案.txt"，"w")
    #f.write(ans)
    #f.close()
main()
#你去问好滴哦亲我很激动i