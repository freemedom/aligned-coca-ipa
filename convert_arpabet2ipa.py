import sys
sys.path.append('./phonecodes_master/src')
import phonecodes#有-master不行
import json
# 读取数据
with open('g2p.json', 'r') as f:
    data = json.load(f)

with open('./a.txt', 'r') as a:
    item = a.read().split('\n')

with open('./g2p_coca_ipa.txt','a+',encoding='utf-8') as b:
    for i in item:
        print(i)
        b.write(i)
        try:
            ll1=data[i]['graphemes']
            ll2=data[i]['phonemes']
            res = phonecodes.arpabet2ipa(" ".join(ll2),'eng')
            # for l1, l2 in zip(ll1, ll2):
            for l1, l2 in zip(ll1, res.split()):
                b.write(" "+l1+"}"+l2)
        except KeyError:
            print(KeyError)
        b.write("\n")


print(1)