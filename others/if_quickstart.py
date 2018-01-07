from decimal import Decimal
from fractions import Fraction


def test_if_behavior(test_obj):
    is_true = '{} is ture'
    is_false = '{} is false'
    if test_obj:
        print(is_true.format(test_obj))
    else:
        print(is_false.format(test_obj))


def show_type(test_obj):
    print('type of {} is {}'.format(test_obj, type(test_obj)))


constants = None, False
for c in constants:
    show_type(c)
    test_if_behavior(c)

numeric_type = 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
for n in numeric_type:
    show_type(n)
    test_if_behavior(n)

empty_sequences_and_collections = '', (), [], {}, set(), range(0)
for esc in empty_sequences_and_collections:
    print('len of {} is {}'.format(esc, len(esc)))
    show_type(esc)
    test_if_behavior(esc)
