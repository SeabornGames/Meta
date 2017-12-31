#Ensure test_file_code
from seaborn.meta.calling_function import *
from collections import OrderedDict
import unittest

class test_calling_function(unittest.TestCase):

    def test_function_arguments(self):
        self.assertEqual(function_arguments(function_arguments),['func'])

    def test_function_defaults(self):
        self.assertEqual(function_defaults(function_doc),[1, None])

    def test_function_doc(self):
        """
        Tests function_doc's return
        :return:
        """
        self.assertEqual(function_doc(),"\n        Tests function_doc's return"
                                        "\n        :return:\n        ")

    def test_function_path(self):
        self.assertEqual(function_path(function_path),
                         '/Users/ben/code/seaborn/meta/seaborn'
                         '/meta/calling_function.py')

    def test_file_code(self):
        self.assertIn('#Ensure test_file_code\n'
                      'from seaborn.meta.calling_function import *\n'
                      'from collections import OrderedDict\n',file_code())

    def test_relevant_kwargs(self):
        pass
        #TODO: discuss true function of relevant_kwargs

    def test_function_args(self):
        self.assertTupleEqual(function_args(function_args),('function',))

    def test_function_kwargs(self):
        def test(a):
            return function_kwargs()
        self.assertDictEqual(test(a=1),{'a':1})

    def test_function_code(self):
        pass
        #raise NotImplemented

#    def test_function_info(self):
#        denial = ['frame','func_frame','function_linenumber','function_args',
#                  'function_history','function_info','__loader__',
#                  'relevant_kwargs','function_path','function_doc',
#                  'trace_error','function_defaults','function_arguments',
#                  'function_name','builtins','function_kwargs','current_folder',
#                  'path','function_code','file_code','__spec__','line_number',
#                  'locals','kwargs','globals']
#        str_only = ['sys','os','inspect','unittest',
#                    '__doc__','test_calling_function','OrderedDict']
#        control={'line_number': 44,
#                 'locals': "{'self': <test_calling_function.test_calling_function testMethod=test_function_info>}",
#                 'kwargs': "{'self': <test_calling_function.test_calling_function testMethod=test_function_info>}",
#                 'path': '/Users/ben/code/seaborn/meta/test',
#                 'globals': "{'__cached__': '/Users/ben/code/seaborn/meta/test/__pycache__/test_calling_function.cpython-35.pyc'",
#                 'sys': "<module 'sys' (built-in)>",
#                 'traceback': "<module 'traceback' from '/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/traceback.py'>",
#                 'os': "<module 'os' from '/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/os.py'>",
#                 '__package__': '',
#                 'inspect': "<module 'inspect' from '/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/inspect.py'>",
#                 'unittest': "<module 'unittest' from '/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/unittest/__init__.py'>",
#                 '__file__': '/Users/ben/code/seaborn/meta/test/test_calling_function.py',
#                 '__doc__': "None",
#                 '__name__': 'test_calling_function',
#                 'test_calling_function': "<class 'test_calling_function.test_calling_function'>",
#                 'OrderedDict': "<class 'collections.OrderedDict'>",
#                 'function_name': 'test_function_info',
#                 'basename': 'test_calling_function',
#                 'class_name': 'test_calling_function',
#                 'arguments': ['self'],
#                 'file': '/Users/ben/code/seaborn/meta/test/test_calling_function.py'
#                 }
#        testing = function_info()
#        for key in denial:
#            control[key] = 'denied'
#        for key in testing.keys():
#            if key in denial:
#                testing[key] = 'denied'
#            elif key in str_only:
#                testing[key]=repr(testing[key])
#        self.assertDictEqual(testing,control)

#    def test_function_history(self):
#        print(repr(function_history()))

#    def test_func_frame(self):
#        print(repr(func_frame(1,'test_func_frame')))

    def test_function_linenumber(self):
        self.assertEqual(function_linenumber(),'97   ')

    def test_function_name(self):
        self.assertTupleEqual(function_name(),('test_calling_function','test_function_name'))

    def test_path(self):
        self.assertEqual(path(),'test_calling_function__test_calling_function__test_path')

    def test_current_folder(self):
        self.assertEqual(current_folder(),'/Users/ben/code/seaborn/meta/test')

    def test_trace_error(self):
        err = trace_error()
        self.assertEqual(err[1],'in test_trace_error\n    err = trace_error()')

if __name__ == '__main__':
    unittest.main()