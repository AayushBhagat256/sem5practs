class BaseError(Exception):
    pass
class LowError(BaseError):
    pass
class HighError(BaseError):
    pass

N = 29
while(1):
    try:
        # n = int(input("Enter the number : "))
        # if n>N:
        #     raise HighError
        # elif n<N:
        #     raise LowError
        x = "text" + 5  # TypeError
        break
    except LowError:
        print("low")
    except HighError:
        print("high")
    except KeyboardInterrupt:
        print("cancel kyu kiya")
        break
    except TypeError:
        print("X aur 5 ko str ya int karo")