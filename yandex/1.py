
import random

# # vpf1 = 0
# # vpf2 = 0
# # vpf3 = 0
# # vpf4 = 0
# # vpf5 = 0
# # vpf6 = 0
# # total_number = 100
# # keyword = "цветы-30\nрозы-30\nмагазин-40"
# # pf1 = round(total_number/100*vpf1)
# # pf2 = round(total_number/100*vpf2)
# # pf3 = round(total_number/100*vpf3)
# # pf4 = round(total_number/100*vpf4)
# # pf5 = round(total_number/100*vpf5)
# # pf6 = round(total_number/100*vpf6)


# # final_list = []
# # b = keyword.split("\n")
# # list_theme = ''
# # for i in b:
# #     c = i.split("-")
# #     list_theme+=(c[0]+'|')*round(int(c[1])*(total_number / 100))
# # list_theme = list_theme.split("|")
# # list_theme.remove("")

# # for theme in list_theme:
# #     pf1 = total_number/100*vpf1
# #     final_list.append([theme])


# def append_pf(pf, list):
#     random.shuffle(list)
#     pf = pf
#     for i in list:
#         if pf <= 0:
#             i.append(0)
#         else:
#             i.append(1)
#             pf-=1

keyword = "1.цветы-3\n2.розы-3\n3.магазин-4"
total_number = 100
b = keyword.split("\n")
list_theme = ''
for i in b:
    i = i[i.find(".") + 1:]
    c = i.split("-")
    list_theme+=(c[0]+'|')*(int(c[1]))
list_theme = list_theme.split("|")
list_theme.remove("")
# random.shuffle(list_theme)

final_list = []
for theme in list_theme:
    final_list.append([theme])
print(final_list)

# pf1 = 30
# pf2 = 30
# pf3 = 30
# pf4 = 30
# pf5 = 30
# pf6 = 30
# pf7 = 30
# pf8 = 30
# pf9 = 5
# pf10 = 5
# pf11 = 5



# append_pf(pf1, final_list)
# append_pf(pf2, final_list)
# append_pf(pf3, final_list)
# append_pf(pf4, final_list)
# append_pf(pf5, final_list)
# append_pf(pf6, final_list)
# append_pf(pf7, final_list)
# append_pf(pf8, final_list)
# # random.shuffle(final_list)
# for i in final_list:
#     if pf9>0:
#         i.append(1)
#         pf9-=1
#     else:
#         i.append(0)
# # random.shuffle(final_list)
# for i in final_list:
#     if pf10>0 and i[9]==0:
#         i.append(1)
#         pf10-=1
#     else:
#         i.append(0)
# # random.shuffle(final_list)
# for i in final_list:
#     if pf11>0 and i[10]==0 and i[9]==0:
#         i.append(1)
#         pf11-=1
#     else:
#         i.append(0)
# # random.shuffle(final_list)

# print(final_list)




