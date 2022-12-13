mode = input("请输入模式，输入0为输入字母查找音标，输入1为输入音标查找字母：")
if mode == '0':
    g_p = input("输入所需查找的字母：")
else:
    g_p = input("输入所需查找的音标：")

with open('g2p_coca_ipa_withoutstress.txt', 'r', encoding='utf-8') as f:  # gbk编码会读成别的字符
    lines = f.read().split('\n')

#
#
# g_p = "i"
dict_print = {}
for line in lines:
    ll = line.split()
    for i in ll[1:]:
        grapheme_phoneme = i.split("}")
        #0 1统一
        if g_p in grapheme_phoneme[int(mode)]:
            if grapheme_phoneme[1-int(mode)] not in dict_print:
                dict_print[grapheme_phoneme[1-int(mode)]] = []
            dict_print[grapheme_phoneme[1-int(mode)]].append(ll[0] + " " + i)
            # print(ll[0] + " " + i)
#
dict_print_list = sorted(dict_print.items(), key=lambda kv: len(kv[1]), reverse=True)
for tuple in dict_print_list:
    print("---------------------------")
    print(tuple[0])
    print(len(tuple[1]))
    print("---------------------------")
    for i in tuple[1]:
        print(i)
