from seaborn.calling_function import *
from collections import OrderedDict

def smoke_test():
    # from seaborn.test.assert_answer import assert_answer
    class TestClass(object):
        def __init__(self, c, d=1):
            self.path = path(d)
            self.args = function_info(d)

        @staticmethod
        def static_test(a, index=1):
            return function_info(function_index=index) # BJC was function but I didn't understand that

    def test_func_path(a, index=1):
        return path(index)

    def test_func_info(a, index=1, function_name=None):
        return function_info(function_name=function_name, function_index=index, line_number='skip for testing')

    def test_func_embed(func, **kwargs):
        return func(**kwargs)

    results = OrderedDict([('class_path', TestClass(c='c').path),
                           ('class_info', TestClass(c='c').args),
                           ('function_path', test_func_path("a")),
                           ('test_info', test_func_info(a="a")),
                           ('embed_func_info', test_func_embed(test_func_info, a="a", index=2)),
                           ('embed_func_path', test_func_embed(test_func_path, a="a", index=2)),
                           ('embed_class_path', test_func_embed(TestClass, c="c", d=2).path),
                           ('embed_class_info', test_func_embed(TestClass, c="c", d=2).args),
                           ('static_args', TestClass.static_test("a")),
                           ('embed_static_args', test_func_embed(TestClass.static_test, a="a", index=2))])

