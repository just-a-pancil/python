q = input()

#0  9   0   2   3   4
left_side = int(q[0])+int(q[1])+int(q[2])
right_side = int(q[3])+int(q[4])+int(q[5])
if right_side == left_side:
    print('nice')
else:
    print('nonice')
