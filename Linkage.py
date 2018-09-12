from scipy import spatial
import timeit
import ujson
import re
import numpy as np
from collections import defaultdict

def read2json():
    s = []
    #read the file
    with open ('toyota.jl', 'r') as f:
        for line in f:
            s.append(line.strip())

    #jsonFile is the transformation of the string
    jsonFile =  ujson.loads("[{}]".format(','.join(s)))
    return jsonFile


#sort the post
def make_post():
    jsonFile = read2json()
    data = defaultdict(lambda : defaultdict(list))
    #transform the data into the pattern
    pattern = re.compile(r'userinfo\.php\?id=(\d+)')


    for row in jsonFile:
        #find the author => author
        author = row['author']
        #find the post id => post_id
        post_id = row['post_id']
        #find the user id =>usr_id
        usr_id = pattern.search(row['usr_id']).group(1)
        
        #if author==1 save use_id into the 'main' column
        if author == 1:
            data[post_id]['main'].append(usr_id)
        #if author==01 save usr_id into the 'comments' column
        elif author == 0:
            data[post_id]['comments'].append(usr_id)

    print('data read.')
    return data

#write the data into Link.txt
def make_link():
    #get the main and comments user id in every post
    data = make_post()
    #To make a set without any elements
    pair_set = set()
    
    #key=post_id value=
    for key, value in data.items():
        #only one value
        main_id = value['main'][0]
        #comments_id is a vector
        comments_id = value['comments']
        #update the pair_set with main_id and comment
        for comment in comments_id:
            pair_set.update([(main_id, comment)])

    #write the result into Link.txt
    with open('Link.txt', 'w') as o:
        o.write(str(pair_set))

#write the date into date.txt
def make_date():
    jsonFile=read2json()
    data={}
    hourIndex = {'00': 1, '01': 1, '02': 2, '03': 2, '04': 3, '05': 3, '06': 4, '07': 4, 
           '08': 5, '09': 5, '10': 6, '11': 6, '12': 7, '13': 7, '14': 8, '15': 8, 
           '16': 9, '17': 9, '18': 10, '19': 10, '20': 11, '21': 11, '22': 12, '23': 12}
    for row in jsonFile:
        #find the author
        author = row['author']
        #find the usr_id
        #the result of findall is 'list' type, so use the [0] to get the string
        usr_id = re.findall(r'\d+', row['usr_id'])[0]
        
        #find all post time (only hour)
        #the result of findall is the 'list' type, so use the [0] to get the string
        date = re.findall(r'(\d+):', row['postdate'])[0]
        #get the hour index
        hour = hourIndex.get(date)
        #if usr_id exists plus 1 with the index
        #else create a 1x12 zeor vector and plus 1 with index
        if usr_id in data:
            data[usr_id][hour-1]+=1
        else:
            data[usr_id]=np.zeros(12)
            data[usr_id][hour-1]+=1
    with open('Date.txt','w') as w:
        for row in data.items():
            w.write(str((row[0],str(row[1]))))
    w.close()
    print('date done.')
    return data


if __name__ == '__main__':
    #set the timer 
    t0 = timeit.default_timer()
    d=make_date()
    M=1-spatial.distance.cosine(d['3025887'], d['3025887'])
    #stop the timer
    t1 = timeit.default_timer()
    
    #print the running time
    print(t1-t0)

