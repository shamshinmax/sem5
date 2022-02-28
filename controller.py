import functions
import view
import data
def button():
    answer = 1
    chos = int(input("Complex or not(0, 1)"))
    if chos == 0:
        value1 = view.get_int()
    elif chos == 1:
        value1 = view.get_complex()
    while answer == 1:
        chos = int(input("Complex or not(0, 1): "))
        if chos == 0:
           value2 = view.get_int()
        elif chos == 1:
           value2 = view.get_complex()
        data.user_data(value1, value2)
        fun = input("Choose operation(+-/*): " )
        if fun == "+":
            result = functions.sum(value1, value2)
            value1 = result
        elif fun == "*":
            result = functions.mult(value1, value2)
            value1 = result
        elif fun == "/":
            while value2 == 0:
                print("Введите число отличное от нуля")
                if chos == 1:
                    value2 = view.get_complex()
                elif chos == 0:
                    value2 = view.get_int()
            else:
                result = functions.div(value1, value2)
                value1 = result
        elif fun == "-":
            result = functions.dif(value1, value2)
            value1 = result
        else:
            print("Выберите операцию еще раз")
        answer = int(input("Еще операцию?(0,1): "))
    view.viewer(result)
