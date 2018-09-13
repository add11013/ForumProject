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
    print(type(usr_id_list))
    return usr_id_list
#1
def get_Article_num():

        # for row in file.readlines():
        #     print(row)
    Article_num=0
    return Article_num
# #2
# def get_Replied_by_prob():
       
#     return Replied_by_prob
# #3
# def get_Reply_prob():
    
#     return Reply_prob

#4
def get_Deg_centrality(G):
    jsonFile=read2json()    
    Deg_centrality={}
    for row in jsonFile:
        usr_id = re.findall(r'\d+', row['usr_id'])[0]
        if usr_id not in Deg_centrality:
            Deg_centrality[usr_id]=len(G.adj[usr_id].keys())
    return Deg_centrality

if __name__ == '__main__':
    #set the timer 
    t0 = timeit.default_timer()
    
    usr_id_list=get_Usr_id()
    #stop the timer
    t1 = timeit.default_timer()
    
    #print the running time
    print(t1-t0)