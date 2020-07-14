for i in range(1, 101):
    if i % 5 == 0 and i % 7 == 0:
        print(f'ChickenMonkey')
    elif i % 5 == 0:
        print(f'Chicken')
    elif i % 7 == 0:
        print(f'Monkey')
    else:
        print(i)
