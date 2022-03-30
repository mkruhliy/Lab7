class CustomException(Exception):
    def __init__(self, message) -> None:
        self.message = message

def myexcept_raise_func():
    raise CustomException("my custom err")

def raise_func():
    raise IndexError
    # raise KeyError

def except_func():
    try:
        #raise_exc()
        myexcept_raise_func()
    except KeyError:
        print("key err handling")
    except IndexError:
        print("indx err handling")
    except CustomException as e:
        print("{} handling, {}".format(e.__class__.__name__, e.message))
    else:
        print("no exceptions")


except_func()