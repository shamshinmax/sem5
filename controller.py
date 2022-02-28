import functions
import view
import data
def button():
    value1 = view.get()
    value2 = view.get()
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
