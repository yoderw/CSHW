def reverse_of(xs):
    if len(xs)<2:
        return xs
    else:
        return xs[-1:] + reverse_of(xs[:-1])
