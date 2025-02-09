# CIRCULAR CONVOLUTION
def conv(x, h):
    max_len = max(len(x), len(h))

    # adding padding in the array
    x = x + [0] * (max_len - len(x))
    h = h + [0] * (max_len - len(h))

    y = [0] * max_len  # convolution array

    for n in range(max_len):
        for k in range(max_len):
            y[n] = y[n] + x[k] * h[(n - k) % max_len]

    return y


x = [1, -1, -2, 3, -1]
h = [1, 2, 3]

result = conv(x, h)
print(result)
