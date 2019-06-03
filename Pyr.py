while True:
    try:
        height = int(input("Высота пирамиды:"))
        if (0 < height < 24):
            for i in range(1, height):
                indentation = height - i - 1
                print(' ' * indentation, "#" * (i + 1))
            print("#" * (height + 1))
        else:
            print("Высота пирамида выходит за диапазон значений")
    except:
        print("Введите высоту пирамиды повторно. З")