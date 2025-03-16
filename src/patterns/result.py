class Result:
    def __init__(self, value, error):
        self.value = value
        self.error = error

    def is_ok(self):
        return self.error is None

    def is_err(self):
        return self.error is not None

    def unwrap(self):
        return (self.value, self.error)

    def unwrap_err(self):
        if self.is_err():
            return self.error
        else:
            raise Exception("Called unwrap_err on an ok")

    def map(self, f):
        if self.is_ok():
            return Result(f(self.value), None)
        else:
            return Result(None, self.error)

    def map_err(self, f):
        if self.is_err():
            return Result(None, f(self.error))
        else:
            return Result(self.value, None)

    def and_then(self, f):
        if self.is_ok():
            return f(self.value)
        else:
            return Result(None, self.error)

    def or_else(self, f):
        if self.is_err():
            return f(self.error)
        else:
            return Result(self.value, None)

    def __str__(self):
        if self.is_ok():
            return f"Ok({self.value})"
        else:
            return f"Err({self.error})"

    def __eq__(self, other):
        if self.is_ok() and other.is_ok():
            return self.value == other.value
        elif self.is_err() and other.is_err():
            return self.error == other.error
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def ok(value):
        return Result(value, None)

    @staticmethod
    def err(error):
        return Result(None, error)