#! /usr/bin/python3

import time, timeit

n_tests = 10000

DIGITS = {
	'ZERO'  : '0',
	'ONE'   : '1',
	'TWO'   : '2',
    'THREE' : '3',
    'FOUR'  : '4',
    'FIVE'  : '5',
    'SIX'   : '6',
    'SEVEN' : '7',
    'EIGHT' : '8',
    'NINE'  : '9',
}

DIGITS_ = {
	'ZERO'  : 0,
	'ONE'   : 1,
	'TWO'   : 2,
    'THREE' : 3,
    'FOUR'  : 4,
    'FIVE'  : 5,
    'SIX'   : 6,
    'SEVEN' : 7,
    'EIGHT' : 8,
    'NINE'  : 9,
}

DIGITS_STRINGS = tuple(DIGITS.keys())
DIGITS_VALUES = tuple(DIGITS.values())

digits_strings_ = []
digits_values_ = []

for DIGIT in DIGITS_STRINGS:
	digits_strings_.append(' ' + DIGIT)

for DIGIT in DIGITS_VALUES:
	digits_values_.append(int(DIGIT))

DIGITS_STRINGS_ = tuple(digits_strings_)
DIGITS_VALUES_ = tuple(digits_values_)

def test_fn_1():
	sentence = 'PRESS UPPER NINE'
	substr = sentence.replace('PRESS ','')
	if substr.endswith('TWO'):
		substr = substr.replace(DIGITS_STRINGS_[2],'')
		n = DIGITS_VALUES_[2]
	elif substr.endswith('THREE'):
		substr = substr.replace(DIGITS_STRINGS_[3],'')
		n = DIGITS_VALUES_[3]
	elif substr.endswith('FOUR'):
		substr = substr.replace(DIGITS_STRINGS_[4],'')
		n = DIGITS_VALUES_[4]
	elif substr.endswith('FIVE'):
		substr = substr.replace(DIGITS_STRINGS_[5],'')
		n = DIGITS_VALUES_[5]
	elif substr.endswith('SIX'):
		substr = substr.replace(DIGITS_STRINGS_[6],'')
		n = DIGITS_VALUES_[6]
	elif substr.endswith('SEVEN'):
		substr = substr.replace(DIGITS_STRINGS_[7],'')
		n = DIGITS_VALUES_[7]
	elif substr.endswith('EIGHT'):
		substr = substr.replace(DIGITS_STRINGS_[8],'')
		n = DIGITS_VALUES_[8]
	elif substr.endswith('NINE'):
		substr = substr.replace(DIGITS_STRINGS_[9],'')
		n = DIGITS_VALUES_[9]
	
def test_fn_2():

	sentence = 'PRESS UPPER NINE'
	substr = sentence.replace('PRESS ','')
    
	match (substr[12:15]):
		case 'TWO':
			substr = substr.replace(DIGITS_STRINGS_[2],'')
			n = DIGITS_VALUES_[2]
		case 'THREE':
			substr = substr.replace(DIGITS_STRINGS_[3],'')
			n = DIGITS_VALUES_[3]
		case 'FOUR':
			substr = substr.replace(DIGITS_STRINGS_[4],'')
			n = DIGITS_VALUES_[4]
		case 'FIVE':
			substr = substr.replace(DIGITS_STRINGS_[5],'')
			n = DIGITS_VALUES_[5]
		case 'SIX':
			substr = substr.replace(DIGITS_STRINGS_[6],'')
			n = DIGITS_VALUES_[6]
		case 'SEVEN':
			substr = substr.replace(DIGITS_STRINGS_[7],'')
			n = DIGITS_VALUES_[7]
		case 'EIGHT':
			substr = substr.replace(DIGITS_STRINGS_[8],'')
			n = DIGITS_VALUES_[8]
		case 'NINE':
			substr = substr.replace(DIGITS_STRINGS_[9],'')
			n = DIGITS_VALUES_[9]



result1 = timeit.timeit(lambda: test_fn_1(), number=n_tests)
result2 = timeit.timeit(lambda: test_fn_2(), number=n_tests)
print("Timeit Result 1:", result1)
print("Timeit Result 2:", result2)

start_time_1 = time.perf_counter()
    
for i in range(n_tests):
    test_fn_1()
    
end_time_1 = time.perf_counter()
execution_time_1 = end_time_1 - start_time_1
print(f"Mean Excution Time 1: {execution_time_1/n_tests}")


start_time_2 = time.perf_counter()

for i in range(n_tests):
    test_fn_2()
    
end_time_2 = time.perf_counter()
execution_time_2 = end_time_2 - start_time_2
print(f"Mean Excution Time 2: {execution_time_2/n_tests}")