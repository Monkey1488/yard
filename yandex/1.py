# import random

# vpf1 = 0
# vpf2 = 0
# vpf3 = 0
# vpf4 = 0
# vpf5 = 0
# vpf6 = 0
# total_number = 100
# keyword = "цветы-30\nрозы-30\nмагазин-40"
# pf1 = round(total_number/100*vpf1)
# pf2 = round(total_number/100*vpf2)
# pf3 = round(total_number/100*vpf3)
# pf4 = round(total_number/100*vpf4)
# pf5 = round(total_number/100*vpf5)
# pf6 = round(total_number/100*vpf6)


# final_list = []
# b = keyword.split("\n")
# list_theme = ''
# for i in b:
#     c = i.split("-")
#     list_theme+=(c[0]+'|')*round(int(c[1])*(total_number / 100))
# list_theme = list_theme.split("|")
# list_theme.remove("")

# for theme in list_theme:
#     pf1 = total_number/100*vpf1
#     final_list.append([theme])


# def append_pf(pf, list):
#     random.shuffle(list)
#     pf = pf
#     for i in list:
#         if pf <= 0:
#             i.append(0)
#         else:
#             i.append(1)
#             pf-=1

# append_pf(pf1, final_list)
# append_pf(pf2, final_list)
# append_pf(pf3, final_list)
# append_pf(pf4, final_list)
# append_pf(pf5, final_list)
# append_pf(pf6, final_list)
# random.shuffle(final_list)
# pf7 = 0
# c=0
# for i in final_list:
#     if pf7>0 and i[6]==0:
#         i.append(1)
#         pf7-=1
#         c+=1
#     else:
#         i.append(0)
# a = 0
# for i in final_list:
#     if "1" in i:
#         a+=1
# print(final_list)
# print(c)



import time
a = time.perf_counter()
# time.sleep(3)
b = time.perf_counter()
c = b-a
print(round(a),round(b),c)

