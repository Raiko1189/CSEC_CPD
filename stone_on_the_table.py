n = int(input())
color = input()
color_list = list(color)
no_move = 0;
i = 0
while i< len(color_list)-1:
    if color_list[i+1]==color_list[i]:
        color_list.pop(i+1)
        no_move += 1
    else:
        i+=1

print(no_move)
