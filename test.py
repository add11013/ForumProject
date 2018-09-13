import timeit
import ujson
import re


def read2json():
    s = []
    #read the file
    with open ('toyota.jl', 'r') as f:
        for line in f:
            s.append(line.strip())

    #jsonFile is the transformation of the string
    jsonFile =  ujson.loads("[{}]".format(','.join(s)))
    return jsonFile

def get_Usr_id():
    #find the user_id
    # jsonFile=read2json()
    # usr_id_list=[]
    # for row in jsonFile:
    #     usr_id = re.findall(r'\d+', row['usr_id'])[0]
    #     if usr_id not in usr_id_list:
    #         usr_id_list.append(usr_id)
    
    #get the user_id_list
    with open('Usr_id.txt','r') as file:
        usr_id_list=re.findall(r'(\d+)', file.read())
    return usr_id_list
#1
def get_Article_num():
    jsonFile=read2json()
    usr_id_list=get_Usr_id()
    post={}
    comment={}
    Article_num={}
    for row in jsonFile:
        author=row['author']
        usr_id=re.findall(r'\d+', row['usr_id'])[0]
        #find the number of post
        if author==1:
            if usr_id in post:
                post[usr_id]+=1
            else:
                post[usr_id]=1
        #find the number of comment
        else:
            if usr_id in comment:
                comment[usr_id]+=1
            else:
                comment[usr_id]=1
    #initial Article_num
    for usr_id in usr_id_list:
        Article_num[usr_id]=0
    
    #calculatet Article_num
    for usr_id in Article_num:
        if usr_id in post:
            Article_num[usr_id]+=post[usr_id]
        if usr_id in comment:
            Article_num[usr_id]+=comment[usr_id]
    return Article_num
#2
def get_Replied_by_prob():
    jsonFile=read2json()
    usr_id_list=get_Usr_id()
    author_0={}
    author_1={}
    post={}
    Replied={}
    Replied_by_prob={}
    
    #split the author=0 and author=1
    for row in jsonFile:
        author=row['author']
        usr_id=re.findall(r'\d+',row['usr_id'])[0]
        post_id=row['post_id']
        if author==0:
            author_0[post_id]=usr_id
        else:
            author_1[post_id]=usr_id
        
        #find the number of post
        if author==1:
            if usr_id in post:
                post[usr_id]+=1
            else:
                post[usr_id]=1

    #initial Replied_by_prob
    for usr_id in usr_id_list:
        Replied[usr_id]=0

    for post_id in author_1:
        if post_id in author_0:
            Replied[author_1[post_id]]+=1
    
    for usr_id in usr_id_list:
        if usr_id not in Replied:
            Replied[usr_id]=0
        elif usr_id not in post:
            #when the post is 0, the formula error, so use very small number
            post[usr_id]=0.000000000000000000000000000001
        Replied_by_prob[usr_id]=Replied[usr_id]/post[usr_id]

    return Replied_by_prob 
#3
def get_Reply_prob():
    Article_num=get_Article_num()
    jsonFile=read2json()
    usr_id_list=get_Usr_id()
    comment={}
    Reply_prob={}
    for row in jsonFile:
        author=row['author']
        usr_id=re.findall(r'\d+', row['usr_id'])[0]
        if author==0:
            if usr_id in comment:
                comment[usr_id]+=1
            else:
                comment[usr_id]=1
    
    for usr_id in usr_id_list:
        if usr_id not in comment:
            comment[usr_id]=0
        Reply_prob[usr_id]=comment[usr_id]/Article_num[usr_id]
    return Reply_prob
#4
def get_Deg_centrality(G):
    jsonFile=read2json()    
    Deg_centrality={}
    for row in jsonFile:
        usr_id = re.findall(r'\d+', row['usr_id'])[0]
        if usr_id not in Deg_centrality:
            Deg_centrality[usr_id]=len(G.adj[usr_id].keys())
    return Deg_centrality

def get_Kmeans_vector():
    usr_id_list=get_Usr_id()
    Kmeans_vector={}
    Article_num=get_Article_num()
    Replied_by_prob=get_Replied_by_prob()
    Reply_prob=get_Reply_prob()
    #Deg_centrality=get_Deg_centrality(G)
    for usr_id in usr_id_list:
        Kmeans_vector[usr_id]=[0,0,0,0,0]
    for usr_id in usr_id_list:
        Kmeans_vector[usr_id][0]=Article_num[usr_id]
        Kmeans_vector[usr_id][1]=Replied_by_prob[usr_id]
        Kmeans_vector[usr_id][2]=Reply_prob[usr_id]
        #Kmeans_vector[usr_id][3]=Deg_centrality[usr_id]
    return Kmeans_vector
if __name__ == '__main__':
    #set the timer 
    t0 = timeit.default_timer()
    
    Kmeans_vector=get_Kmeans_vector()
    print(Kmeans_vector)
    #stop the timer
    t1 = timeit.default_timer()
    
    #print the running time
    print(t1-t0)