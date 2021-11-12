# my_list = [*range(10, 20, 1)]
# print(my_list)


def ext_force(val):
    return 10*val


class test_fun:
    def __init__(self, ext):
        self.ext = ext

    def run(self):
        for i in range(10):
            print(self.ext(i))



test1 = test_fun(ext_force)

test1.run()