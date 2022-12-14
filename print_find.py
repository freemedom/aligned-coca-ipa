mode = input("请输入模式，输入0为输入1个字母查找音标，输入1为输入1个音标查找字母，输入2为输入2个字母查找音标：")
if mode == '0':
    g_p = input("输入所需查找的1个字母：")
elif mode == '1':
    g_p = input("输入所需查找的1个音标：")
else:
    g_p = input("输入所需查找的2个字母：")

with open('g2p_coca_ipa_withoutstress.txt', 'r', encoding='utf-8') as f:  # gbk编码会读成别的字符
    lines = f.read().split('\n')

#
#
# g_p = "i"
dict_print = {}
for line in lines:
    ll = line.split()
    #
    # for i in ll[1:]:
    for i in range(1, len(ll)):
        #
        #
        if mode == '0' or mode == '1':
            grapheme_phoneme = ll[i].split("}")
            # 0 1统一
            if g_p in grapheme_phoneme[int(mode)]:
                key = grapheme_phoneme[1 - int(mode)]
                if key not in dict_print:
                    dict_print[key] = []
                dict_print[key].append(ll[0] + " " + ll[i])
                # print(ll[0] + " " + i)
        if mode == '2':
            grapheme_phoneme = ll[i].split("}")
            if i != len(ll) - 1:
                grapheme_phoneme_2 = ll[i + 1].split("}")
            else:
                grapheme_phoneme_2 = ['@','@']
                # grapheme_phoneme_2 = ''
            app = ''
            if g_p[0] in grapheme_phoneme[0][-1] and g_p[1] in grapheme_phoneme_2[0][0]:
                key = grapheme_phoneme[1]+grapheme_phoneme_2[1]
                if key not in dict_print:
                    dict_print[key] = []
                dict_print[key].append(ll[0] + " " + ll[i] + " " + ll[i + 1])
                # print(ll[0] + " " + ll[i] + " " + ll[i + 1])
            if g_p in grapheme_phoneme[0].replace('|',''):
                key = grapheme_phoneme[1]
                if key not in dict_print:
                    dict_print[key] = []
                dict_print[key].append(ll[0] + " " + ll[i])



#
dict_print_list = sorted(dict_print.items(), key=lambda kv: len(kv[1]), reverse=True)
for tuple in dict_print_list:
    print("---------------------------")
    print(tuple[0])
    print(len(tuple[1]))
    print("---------------------------")
    for i in tuple[1]:
        print(i)
