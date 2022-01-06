word = 'roooooobertapalaxxxxios'

# delete just the SEQUENTIAL duplicate letters
result = letter = word[0]

for l in word[1:]:
    if l == letter:
        continue
    result += l
    letter = l

print (result)

#-------------------------------------------------------
#
# result = word[0]  # delete ALL duplicate letters
# letter = list(word[0])
#
# for l in word[1:]:
#     if l in letter:
#         continue
#     result += l
#     letter.append(l)
# print(result)

#--------------------------------------------------------

# result=''   # delete just the SEQUENTIAL duplicate letters
# for i in range(len(word)):
#     if i == len(word)-1:
#          result+=word[i]
#     elif word[i] != word[i+1]:
#         result+=word[i]
#     else: continue
# result