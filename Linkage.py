
import timeit
import ujson
import re
from collections import defaultdict

def read2json():
    s = []

    with open ('toyota.jl', 'r') as f:
        for line in f:
            s.append(line.strip())

    jsonFile =  ujson.loads("[{}]".format(','.join(s)))

    return jsonFile



def make_post():
    jsonFile = read2json()
    data = defaultdict(lambda : defaultdict(list))
    pattern = re.compile(r'userinfo\.php\?id=(\d+)')


    for row in jsonFile:
        author = row['author']
        post_id = row['post_id']
        usr_id = pattern.search(row['usr_id']).group(1)

        if author == 1:
            data[post_id]['main'].append(usr_id)
        elif author == 0:
            data[post_id]['comments'].append(usr_id)

    print('data read.')
    return data


def make_link():
    data = make_post()

    pair_set = set()

    for key, value in data.items():
        main_id = value['main'][0]
        comments_id = value['comments']

        pair_set.update([(main_id, comment) for comment in comments_id])

    #output
    with open('Link.txt', 'w') as o:
        o.write(str(pair_set))








if __name__ == '__main__':
    t0 = timeit.default_timer()
    make_link()
    t1 = timeit.default_timer()

    print(t1-t0)

