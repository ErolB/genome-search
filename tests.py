from modules import utils

def pattern_test():
    test_pattern = '[AC]-x-V-x(4)-{ED}'
    final = utils.pattern_converter(test_pattern)
    print(final)

pattern_test()
