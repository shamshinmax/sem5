import functions
import view
import data
def button():
    chos = int(input("Complex or not(0, 1)"))
    if chos == 0:
        value1 = view.get_int()
        value2 = view.get_int()
    elif chos == 1:
        value1 = view.get_complex()
        value2 = view.get_complex()
    data.user_data(value1, value2)
    fun = input("Choose operation(+-/*): " )
    if fun == "+":
        result = functions.sum(value1, value2)
    elif fun == "*":
        result = functions.mult(value1, value2)
    elif fun == "/":
        result = functions.div(value1, value2)
    elif fun == "-":
        result = functions.dif(value1, value2)
    view.viewer(result)
