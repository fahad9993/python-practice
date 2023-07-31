row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]

treasure_map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? (rc) ")

r = int(position[0])
c = int(position[1])

treasure_map[r - 1][c - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
