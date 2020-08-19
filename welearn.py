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
    ret  = ""
    L = {'a','b','c','d'}
    #find 1
    for i in soup.find_all('et-choice'):
        #if(i.parent.name=='et-web-only'):
        #    continue
        if(i.get('key') not in L):
            continue
        if(flag == 0):
            #print()
            ret+='\n'
            flag = 1
            print("Unit=%s x=%s y=%s z=%s"%(u,x,y,z))
            ret+=("Unit=%s x=%s y=%s z=%s"%(u,x,y,z))
        ret+='\n'+(i.get('key'))
        #rwz=i.get('ol')
        #for j in rwz.children:
        #    print(j.string)
        #print(i)
    #find 2
    
    for i in soup.find_all('et-blank'):
        if(i.parent.name=='et-mobile-only'):
            continue
        if(flag == 0):
            #print()
            ret+='\n'
            flag = 1
            print("Unit=%s x=%s y=%s z=%s"%(u,x,y,z))
            ret+=("Unit=%s x=%s y=%s z=%s"%(u,x,y,z))
        if(i.string):
            #print(i.string)
            ret+='\n'+i.string
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
                    #print()
                    ret+='\n'
                    flag = 1
                    print("Unit=%s x=%s y=%s z=%s"%(u,x,y,z))
                    ret+=("Unit=%s x=%s y=%s z=%s"%(u,x,y,z))
                #print(k.string)   
                ret+='\n'+k.string
    return ret
    
def main():
    url1 = 'https://centercourseware.sflep.com/inspire%204/data/'\
    
    #3
    ans=""
    for u in range(11,16):
        for x in range(1,7):
            #print(url1+str(u)+'/'+str(x)+'.html')
            html = getinfo(url1+str(u)+'/'+str(x)+'.html')
            #print(html)
            if(html!='0'):
                ans=ans+work(u,x,0,0,html)
            for y in range(1,5):
                #print(url1+str(u)+'/'+str(x)+'-'+str(y)+'.html')
                html = getinfo(url1+str(u)+'/'+str(x)+'-'+str(y)+'.html')
                #print(html)
                if(html!='0'):
                    ans=ans+work(u,x,y,0,html)
                for z in range(1,6):
                    #print(url1+str(u)+'/'+str(x)+'-'+str(y)+'-'+str(z)+'.html')
                    html = getinfo(url1+str(u)+'/'+str(x)+'-'+str(y)+'-'+str(z)+'.html')
                    #print(html)
                    if html !='0':
                        ans=ans+work(u,x,y,z,html)
                #url = last
    f = open("out.html","a",encoding='utf-8')  
    print(ans)
    f.write(ans)
    f.close()
main()
#zhy goto f