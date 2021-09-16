import math
while True:
    choice = int(input('''Welcome to the triangle area calculation tool.
    
    Menu: 
    1. Calculate triangle area by base and height
    2. Calculate triangle area by 2 sides and angle between them
    3. Exit
    Enter menu item number: '''))
    if choice == 1 or choice == 2 or choice == 3:
        if choice == 1:
            measures = input('Enter base and height: ')
            parts = measures.split(" ")
            base = int(parts[0])
            height = int(parts[1])
            area = base * height / 2
            print(f'Area is: {base * height / 2:.0f}')
        elif choice == 2:
            measures = input('Enter 2 sides and angle(degrees) between them: ')
            parts = measures.split(" ")
            side1 = int(parts[0])
            side2 = int(parts[1])
            angle = int(parts[2])
            print(f'Area is: {side1 * side2 * math.sin(math.radians(angle)) / 2:.2f}')
        elif choice == 3:
            print('Goodbye!')
    else:
        print('Number you entered is incorrect. You should enter 1 or 2 or 3')

