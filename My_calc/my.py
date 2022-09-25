# with open('RLE.txt', 'w', encoding='utf-8') as data:
#     simbol = 'AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool'
#     for i in simbol:
#         data.writelines(i)

# with open('RLE.txt', 'r', encoding='utf-8') as data:
#     source_text = ''
#     for i in data:
#         source_text += i
    
#     compressed_text = ''
#     # no_alements = ' '
#     alements = ''
#     i=0
#     while i < len(source_text):
        
#         alements = source_text[i]
#         count_alements = 1
#         while i + 1 < len(source_text) and source_text[i] == source_text[i+1]:
#                 count_alements+=1
#                 i+=1
#         compressed_text = compressed_text + (str(count_alements) + alements)
#         i+=1
#     print(compressed_text)
#     new = open('rez_RLE.txt', 'w',encoding='utf-8')
#     new.writelines(compressed_text)
#     new.close()
# with open('rez_RLE.txt', 'r', encoding='utf-8') as data:
#     text = ''
#     for i in data:
#         text+= i
#     print(text)
   
#     decod = ''
#     alements = ''
#     vrem_int = ''
#     for i in text:
#         if i.isdigit():
#             vrem_int+=i
#         else: 
#             alements = i
#             decod += int(vrem_int)*alements
#             vrem_int = ''
#     print('decod -> ', decod)