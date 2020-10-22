import Logic as L

mat = L.start_game()
print(mat)
print('###########')
print('After Adding random 2')
print('###########')

L.add_new_2(mat)
print(mat)

print('###########')
print('After Adding another random 2')
print('###########')


L.add_new_2(mat)
print(mat)

print('###########')
print('After moving up')
print('###########')


mat = L.move_up(mat)
print(mat)

print('###########')
print('After moving right')
print('###########')


mat = L.move_right(mat)
print(mat)