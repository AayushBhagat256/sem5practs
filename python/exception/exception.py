import math

try:
    # mod = "import "+input("Enter your module name : ")
    # exec(mod)
    # a = 2
    # b = 0
    # c = a/b
    # name = ['a','b']
    # name = name/2
    # num = 5
    # if num>3
        # print("hgello")
    k = input("Lets see keyborad ")
except ImportError:
    print("Import error")
except ZeroDivisionError:
    print("Cant divide by zero")
except TypeError:
    print("Check the type")
except SyntaxError:
    print("SyntaxError: expected ':'")
except KeyboardInterrupt:
    print("ehy....")