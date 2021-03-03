"""Quadro v 0.4 / Author © s-evg"""

INFO = '''   \nДля решения квадратного уравнения
вида: a*x**2 + b*x + c = 0
введите последовательно значения
a, b, c, каждый раз нажимая Enter:\n'''

HELP = '''   \nВведено не верное значение,
введите "y" чтобы решить ещё одно
уравнение, или "n" чтобы выйти: '''

ERROR = ''' \nЭто не квадратное уравнение.
Коэффициент а не может быть равен нулю.
Введите верные значения.\n'''

EXIT = '''  \nСпасибо, что выбрали наше приложение.
До новых встреч! (❁´◡`❁)'''

UPS = '''   \nУпссс... (⊙_⊙;)
  Похоже Вы ошиблисьи и ввели не
числовые значения коэффициентов.
Попробуйте ещё раз, 
и будьте внимательны!\n'''

run = True
while run:
    print(INFO)

    a = (input("Введите значение a: "))
    b = (input("Введите значение b: "))
    c = (input("Введите значение c: "))

    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        print(UPS)
        run = True
    else:
        if a == 0:
            print(ERROR)
            run = True

        else:
            D = b ** 2 - 4 * a * c  # вычисляем дискриминант
            print("\nДискриминант D равен: ", round(D, 2))

            if D > 0:
                X1 = (-b - D ** 0.5) / (2 * a)
                X2 = (-b + D ** 0.5) / (2 * a)
                print("X1 =", round(X1, 2), "X2 =", round(X2, 2))

            elif D == 0:
                X = (-b / 2 * a)
                print("X =", round(X, 2))

            else:
                print('Дискриминант D меньше 0, корней нет.\n¯\\_(ツ)_/¯')

            question = input('\nРешить ещё одно уравнение? y/n: ').lower()
            y_n = True

            while y_n:
                if question == 'y':
                    run = True
                    y_n = False

                elif question == 'n':
                    print(EXIT)
                    run = False
                    y_n = False

                else:
                    question = input(HELP).lower()
                    y_n = True
                    run = False
