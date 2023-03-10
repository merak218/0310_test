seq = '人易科技:上 機 測 驗 - 演算法'
r_word = ':'
half = chr(ord(r_word))
full = str(chr(ord(half)+65248))
seq1 = seq.replace(half, full)
print(seq1)

# 去掉但保留-兩側的空白
seq2 = seq1.replace(' ', '')
seq2 = seq2.replace('-', ' - ')
print(seq2)

# 列印：~-之間的字元
str1 = '：'
str2 = '-'
seq3 = seq2[seq2.index(str1)+1:seq2.index(str2)]
print(seq3)