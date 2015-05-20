# @param start, a string
# @param end, a string
# @param dict, a set of string
# @return an integer
import string
def ladderLength(start, end, dict):
    if not start or not end or not dict:
        return 0
    queue = []
    visited = set([start])
    queue.append(start)
    level=1
    last=1
    cur=0
    while len(queue) > 0:
        v = queue.pop(0)
        last-=1
        for i in range(len(v)):
            for j in string.ascii_lowercase:
                word=v[:i]+j+v[i+1:]
                if word == end:
                    return level+1
                if word not in visited and word in dict:
                    cur+=1
                    queue.append(word)
                    visited.append(word)
        if last==0:
            last = cur
            cur = 0
            level+=1
    return 0


def ladderLength1(start, end, dict):
    if not start or not end or not dict:
        return 0
    dict.append(end)
    level = 0
    visited = set([start])
    current = [start]
    while current:
        next = []
        for word in current:
            if word == end:
                return level+1
            for i in range(len(word)):
                for j in string.ascii_lowercase:
                    neword = word[:i]+j+word[i+1:]
                    if neword not in visited and neword in dict:
                        next.append(neword)
                        visited.add(neword)
        level+=1
        current = next
    return 0






start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]

print ladderLength1(start, end, dict)
