# p1 = 6
# p2 = 16
# s1 = 0
# s2 = 6
# MAX_PRECISION = 38
# MINIMUM_ADJUSTED_SCALE = 6


# p1 = 28
# s1 = 6

# p2 = 28
# s2 = 9


# def get_devide_p_s(p1, s1, p2, s2):
#     p = p1 - s1 + s2 + max(6, s1 + p2 + 1)
#     s = max(6, s1 + p2 + 1)

#     minScaleValue = min(s, MINIMUM_ADJUSTED_SCALE)
#     adjustedScale = max(MAX_PRECISION - p, minScaleValue)
#     print(MAX_PRECISION - p, minScaleValue, adjustedScale)
#     return p, s


# def get_multi_p_s(p1, s1, p2, s2):
#     p = p1 + p2 + 1
#     s = s1 + s2

#     minScaleValue = min(s, MINIMUM_ADJUSTED_SCALE)
#     adjustedScale = max(MAX_PRECISION - p, minScaleValue)
#     print(MAX_PRECISION - p, minScaleValue, adjustedScale)

#     return p, s


# print(get_multi_p_s(p1, s1, p2, s2))


import inspect


def funca(a, b=None):
    return


c = inspect.getfullargspec(funca).args
print(c)

print(inspect.signature(funca), type(inspect.signature(funca)))
