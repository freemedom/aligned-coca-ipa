# aligned-coca-ipa
aligned-coca-ipa

查找 字母 和 音标/发音 的对应关系，并分类排序输出

下载下来g2p_coca_ipa_withoutstress.txt和print_find.py  
运行print_find.py即可

withoutstress意思是去掉了重音标记



## 输入输出
```
请输入模式，输入0为输入字母查找音标，输入1为输入音标查找字母：1
输入所需查找的音标ɪ
---------------------------
i
2336
---------------------------
in i}ɪ
time i}aɪ
think i}ɪ
which i}ɪ
like i}aɪ
等
---------------------------
a
919
---------------------------
a a}eɪ
make a}eɪ
take a}eɪ
state a}eɪ
great a}eɪ
same a}eɪ
place a}eɪ
等
```


```
请输入模式，输入0为输入1个字母查找音标，输入1为输入1个音标查找字母，输入2为输入2个字母查找音标：2
输入所需查找的2个字母：ci
---------------------------
ʃ
59
---------------------------
social c|i}ʃ
especially c|i}ʃ
special c|i}ʃ
official c|i}ʃ
financial c|i}ʃ
commercial c|i}ʃ
politician c|i}ʃ
```
