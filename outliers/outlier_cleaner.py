#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    cleaned_data = []

    ### your code goes here
    err_list = [ (a[0], n[0], abs(n[0] - p[0])) for a, n, p in zip(ages, net_worths, predictions) ]
    err_list = sorted(err_list, key=lambda x: x[2])
    cleaned_data = err_list[ 0: len(err_list) -  len(err_list)/10]
   
    return cleaned_data

