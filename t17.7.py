class ArgsError(Exception):
    def __init__(self, message, *args):
        self.d = [a for a in args]
        self.message = message

    def __str__(self):
        return f"{self.d}: {self.message}"


def contain_kwargs(f):
    def _contain_kwargs(*args, **kwargs):
        if args:
            raise ArgsError("Функція містить позиційні параметри", *args)
        return f(*args, **kwargs)
    return _contain_kwargs


@contain_kwargs
def function(*args, **kwargs):
    p = [{k: v} for k, v in kwargs.items()]
    return p


if __name__ == "__main__":
    print(function(y1=2, y2=1, y3=5))
    try:
        print(function(1, 2, 3, y1=2, y2=1, y3=1))
    except Exception as e:
        print(e)
