def positive_values_from_array(array):
    positives = 0
    for x in array:
        if x > 0:
            positives += 1
    return positives
