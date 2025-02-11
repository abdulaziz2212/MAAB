#Task 1: Get Value
def get_value(dct, key, default=None):
    return dct.get(key, default)

# Task 2: Check Key
def check_key(dct, key):
    return key in dct

# Task 3: Count Keys
def count_keys(dct):
    return len(dct)

# Task 4: Get All Keys
def get_all_keys(dct):
    return list(dct.keys())

# Task 5: Get All Values
def get_all_values(dct):
    return list(dct.values())

# Task 6: Merge Dictionaries
def merge_dictionaries(dct1, dct2):
    result = dct1.copy()
    result.update(dct2)
    return result

# Task 7: Remove Key
def remove_key(dct, key):
    dct.pop(key, None)
    return dct

# Task 8: Clear Dictionary
def clear_dictionary(dct):
    dct.clear()
    return dct

# Task 9: Check if Dictionary is Empty
def is_empty_dictionary(dct):
    return len(dct) == 0

# Task 10: Get Key-Value Pair
def get_key_value_pair(dct, key):
    return (key, dct[key]) if key in dct else None

# Task 11: Update Value
def update_value(dct, key, value):
    dct[key] = value
    return dct

# Task 12: Count Value Occurrences
def count_value_occurrences(dct, value):
    return list(dct.values()).count(value)

# Task 13: Invert Dictionary
def invert_dictionary(dct):
    return {v: k for k, v in dct.items()}

# Task 14: Find Keys with Value
def find_keys_with_value(dct, value):
    return [k for k, v in dct.items() if v == value]

# Task 15: Create a Dictionary from Lists
def create_dict_from_lists(keys, values):
    return dict(zip(keys, values))

# Task 16: Check for Nested Dictionaries
def has_nested_dictionaries(dct):
    return any(isinstance(v, dict) for v in dct.values())

# Task 17: Get Nested Value
def get_nested_value(dct, key1, key2):
    return dct.get(key1, {}).get(key2)

# Task 18: Create Default Dictionary
def create_default_dictionary(default_value):
    from collections import defaultdict
    return defaultdict(lambda: default_value)

# Task 19: Count Unique Values
def count_unique_values(dct):
    return len(set(dct.values()))

# Task 20: Sort Dictionary by Key
def sort_dict_by_key(dct):
    return dict(sorted(dct.items()))

# Task 21: Sort Dictionary by Value
def sort_dict_by_value(dct):
    return dict(sorted(dct.items(), key=lambda item: item[1]))

# Task 22: Filter by Value
def filter_dict_by_value(dct, condition):
    return {k: v for k, v in dct.items() if condition(v)}

# Task 23: Check for Common Keys
def check_common_keys(dct1, dct2):
    return set(dct1.keys()).intersection(dct2.keys())

# Task 24: Create Dictionary from Tuple
def create_dict_from_tuple(tpl):
    return dict(tpl)

# Task 25: Get the First Key-Value Pair
def get_first_key_value_pair(dct):
    return next(iter(dct.items()), None)