#Calculates the Standard Deviation of a vector
def standard_deviation(x):
    n = len(x)
    mean = sum(x) / n
    ssq = sum((x_i-mean)**2 for x_i in x)
    stdev = (ssq/n)**0.5
    return(stdev)

#Calculates the Standard Error of a vector
standard_error = lambda x: standard_deviation(x)/len(x)**0.5
