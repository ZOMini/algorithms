str_len = int(input())
list_all = list(map(str, input().split()))

def find_str():
    tgt_word = list_all[0]
    for idx in range(1, len(list_all)):
        if len(list_all[idx]) <= len(tgt_word): continue
        tgt_word = list_all[idx]
    return tgt_word
res = find_str()
print (res)
print (len(res))
