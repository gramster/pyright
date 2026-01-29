class ClassA:
    def x(self):
        return

maybe = True

a = None if maybe else ClassA()
reveal_type(a)
