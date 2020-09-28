import random
from twilio.rest import Client
def read():
    f = open("cet6.txt","r",encoding = "utf-8")
    src = f.readlines()
    lst = []
    for i in src:
        lst.append ( i.split())
    dic = dict(lst)
    f.close()
    return dic

def start():
    dic = read()
    a = search(dic)
    for i in a:  
        dic[i]=eval(str(dic[i]))+1
    f = open('cet6.txt','w+',encoding = "utf-8")
    for i in dic.keys():
        f.write(i+' ')
        f.write(str(dic[i])+'\n')
    f.close()
    return str(a)

def init():
    dic = read()
    for i in dic.keys():
        dic[i] = 0
    f = open('cet6.txt','w+',encoding = "utf-8")
    for i in dic.keys():
        f.write(i+' ')
        f.write(str(dic[i])+'\n')
    f.close()   
    
def message(text):
    sid = "AC18b9ab2ec519b43eb84490e39af3f246"
    token = "2351d15417a26800726e5551392ce703"
    client = Client(sid,token)
    message = client.messages.create(
    to = "+8617860397150",
    from_ = "+12817127136",
    body = text)
    print(message.sid)

def search(dic):
    s = []
    lst=[]
    lst2= []
    lst3 =[]
    min_=min(map(eval,dic.values()))
    while(1):
        for i in dic.keys():
            if eval(dic[i]) == min_:
                lst.append(i)
            elif eval(dic[i]) == min_+1:
                lst2.append(i)
            else:
                lst3.append(i)
        if len(lst3)>2:
            lst3=random.sample(lst3,1)
        if len(lst2)>10:
            lst2=random.sample(lst2,9)
        lens=50 - len(lst2+lst3+s)
        if len(lst)>=lens:
            lst=random.sample(lst,lens)
            s=s+lst+lst2+lst3
            return s
        else:
            min_=min_+1
            s=lst
            lst=[]
            lst2=[]
            lst3=[]
    










            
            
    
    


            
            



