# User-defined exceptions
class CustomImportError(Exception):
    pass

class CustomIndexError(Exception):
    pass

class CustomKeyError(Exception):
    pass

class CustomKeyboardInterruptError(Exception):
    pass

class CustomRuntimeError(Exception):
    pass

class CustomStopIterationError(Exception):
    pass

class CustomSyntaxError(Exception):
    pass

class CustomTypeError(Exception):
    pass

class CustomValueError(Exception):
    pass

class CustomNameError(Exception):
    pass

class CustomAttributeError(Exception):
    pass

class CustomZeroDivisionError(Exception):
    pass

# Example usage of user-defined exceptions
try:
    # Uncomment and modify the following lines to test different exceptions
    import non_existing_module  # ImportError
    # sequence = [1, 2, 3]
    # print(sequence[5])  # IndexError
    # my_dict = {'key': 'value'}
    # print(my_dict['nonexistent_key'])  # KeyError
    # raise KeyboardInterrupt  # KeyboardInterrupt
    # raise RuntimeError("Custom runtime error message")  # RuntimeError
    # iterator = iter([])  # StopIteration
    # next(iterator)
    # eval("print('Hello world')  # SyntaxError
    # x = "text" + 5  # TypeError
    # int("invalid_value")  # ValueError
    # print(undefined_variable)  # NameError
    # object_without_attribute.some_attribute = 42  # AttributeError
    # result = 10 / 0  # ZeroDivisionError

except ImportError:
    raise CustomImportError("Custom ImportError message")

except IndexError:
    raise CustomIndexError("Custom IndexError message")

except KeyError:
    raise CustomKeyError("Custom KeyError message")

except KeyboardInterrupt:
    raise CustomKeyboardInterruptError("Custom KeyboardInterrupt message")

except RuntimeError:
    raise CustomRuntimeError("Custom RuntimeError message")

except StopIteration:
    raise CustomStopIterationError("Custom StopIteration message")

except SyntaxError:
    raise CustomSyntaxError("Custom SyntaxError message")

except TypeError:
    raise CustomTypeError("Custom TypeError message")

except ValueError:
    raise CustomValueError("Custom ValueError message")

except NameError:
    raise CustomNameError("Custom NameError message")

except AttributeError:
    raise CustomAttributeError("Custom AttributeError message")

except ZeroDivisionError:
    raise CustomZeroDivisionError("Custom ZeroDivisionError message")
