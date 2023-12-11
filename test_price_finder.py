from price_finder import (clean_up, get_info,
                        check_customer, find_price_for_all_products,
                        find_price_for_customer)

# This test is test with 'test.xlsx'

def test_clean_up():
    print('Testing clean_up')
    num_fail = 0
    # Test1
    result = clean_up([10,20,30,40,50])
    expect = [30,40,50]
    if result != expect:
        print(f'...Fail clean_up([10,20,30,40,50]\n expecting: {expect}\n get: {result})')
        num_fail += 1
    # Test2
    result = clean_up(['a', 'b', 'c', 'd'])
    expect = ['b', 'c', 'd']
    if result != expect:
        print(f"...Fail clean_up(['a', 'b', 'c', 'd'])\n expecting: {expect}\n get: {result}")
        num_fail += 1
    # if everything pass
    if result == expect:
        print('...all tests passed for clean_up()')
    return num_fail


def test_get_info():
    print('Testing get_info')
    num_fail = 0
    # Test1
    result = get_info('castle', '52', 'Fresh:Tuna- Big Eye')
    expect = '10/13/2022: sushi castle purchased Fresh:Tuna- Big Eye with 42.21 lbs, each $5.50'
    if result != expect:
        print(f"...Fail get_info('castle', '52', 'Fresh:Tuna- Big Eye')\n expecting: {expect}\n get: {result}")
        num_fail += 1
    # Test2
    result = get_info('34', '66', 'Frozen:Red shumai (ajinomoto)')
    expect = '10/11/2022: sushi palace #34 purchased Frozen:Red shumai (ajinomoto) with 1 cs, each $70.00'
    if result != expect:
        print(f"...Fail get_info('34', '66', 'Frozen:Red shumai (ajinomoto)')\n expecting: {expect}\n get: {result}")
        num_fail += 1
    # if everything pass
    if result == expect:
        print('...all tests passed for get_info()')
    return num_fail


def test_check_customer():
    print('Testing check_customer')
    num_fail = 0
    # Test1
    result = check_customer('34')
    expect = True
    if result != expect:
        print(f"...Fail check_customer('34')\n expecting: {expect}\n get: {result}")
        num_fail += 1
    # Test2
    result = check_customer('not a customer')
    expect = False
    if result != expect:
        print(f"...Fail check_customer('not a customer')\n expecting: {expect}\n get: {result}")
        num_fail += 1
    # if everything pass
    if result == expect:
        print('...all tests passed for check_customer()')
    return num_fail


def test_find_price_for_all_products():
    print('Testing area_triangle')
    num_fail = 0
    # Test1
    result = find_price_for_all_products('yuzu')
    expect = ['10/17/2022: asahi purchased dry:yuzu citrus with 3 cs, each $11.50', '10/14/2022: sushi palace new purchased dry:yuzu citrus with 1 cs, each $11.95']
    if result != expect:
        print(f"...Fail find_price_for_all_products('yuzu')\n expecting: {expect}\n get: {result}")
        num_fail += 1
    # Test2
    result = find_price_for_all_products('not a product')
    expect = []
    if result != expect:
        print(f"...Fail find_price_for_all_products('not a product')\n expecting: {expect}\n get: {result}")
        num_fail += 1
    # if everything pass
    if result == expect:
        print('...all tests passed for find_price_for_all_products()')
    return num_fail


def test_find_price_for_customer():
    print('Testing find_price_for_customer')
    num_fail = 0
    # Test1
    result = find_price_for_customer('cast', '810')
    expect = ['10/13/2022: sushi castle purchased supply:tz 810 with 1 cs, each $50.00']
    if result != expect:
        print(f"...Fail find_price_for_customer('cast', '810')\n expecting: {expect}\n get: {result}")
        num_fail += 1
    # Test2
    result = find_price_for_customer('new', '12oz')
    expect = ['10/14/2022: sushi palace new purchased frozen:12oz eel with 2 cs, each $230.00']
    if result != expect:
        print(f"...Fail find_price_for_customer('new', '12oz')\n expecting: {expect}\n get: {result}")
        num_fail += 1
    # if everything pass
    if result == expect:
        print('...all tests passed for find_price_for_customer()')
    return num_fail


# example main, use as you want. 
def main() -> None: 
    print("Running all tests")
    fail_count = 0
    fail_count += test_clean_up()
    fail_count += test_get_info()
    fail_count += test_check_customer()
    fail_count += test_find_price_for_all_products()
    fail_count += test_find_price_for_customer() 
    if (fail_count > 0):
        print(f"Failed {fail_count} tests.")
    else:
        print('All tests passed')


if __name__ == '__main__':
    main()
