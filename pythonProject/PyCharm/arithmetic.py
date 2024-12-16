def add(*plus):
    sum = 0
    for x in plus:
        sum += x
    return sum


def subtract(*minus):
    diff = minus[0]
    for i in range(1, len(minus)):
        diff -= minus[i]
    return diff


def multiply(*times):
    result = 1
    for aster in times:
        result *= aster
    return result


def divide(*over):
    equal = over[0]
    for divis in range(1, len(over)):
        equal /= over[divis]
    return equal
