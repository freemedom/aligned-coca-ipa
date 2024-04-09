# aligned-coca-ipa
aligned-coca-ipa

查找 字母 和 音标/发音 的对应关系，并分类排序输出

下载下来g2p_coca_ipa_withoutstress.txt和print_find.py  
运行print_find.py即可：python .\print_find.py

withoutstress意思是去掉了重音标记



## 输入输出
```
请输入模式，输入0为输入字母查找音标（支持1个或多个字母、支持正则），输入1为输入音标查找字母（支持多个音标）
x0
输入所需查找的字母（正则必须以//包裹，如/^per/、/.+cu/）：/^per/
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
已启用正则 ^per
pɚ 26 0.52
pɝ 16 0.32
p_ɝ 3 0.06
pɪɹ 2 0.04
pɛɹ 2 0.04
piɹ 1 0.02
p_ɹ 0 0.0
pɨɹ 0 0.0
---------------------------
pɚ 26 0.52
+++++++++++++++++++++++++++
perhaps p}p e|r}ɚ
performance p}p e|r}ɚ
perform p}p e|r}ɚ
perspective p}p e|r}ɚ
percentage p}p e|r}ɚ
perception p}p e|r}ɚ
perceive p}p e|r}ɚ
permission p}p e|r}ɚ
persuade p}p e|r}ɚ
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
