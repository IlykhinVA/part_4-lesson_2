def test_function():
    #global inner_function

    def inner_function():
        print('я в области видимости функции test_function')

    inner_function()


test_function()

inner_function()
# При выполнении строки 12 произойдет ошибка:
# программа запросит определить inner_function.
# При определении inner_function глобальной в строке 2 программа отработает корректно.
