# Given a set of time intervals in any order, merge all overlapping intervals into one and output the result which should have only mutually exclusive intervals.
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort intervals based on start time
    result = [intervals[0]]  # Initialize result with the first interval
    
    for interval in intervals[1:]:
        # If the start time of the current interval is greater than the end time of the last interval in the result list,
        # then add the current interval to the result list.
        if interval[0] > result[-1][1]:
            result.append(interval)
        else:
            # Otherwise, merge the current interval with the last interval in the result list by updating its end time.
            result[-1][1] = max(result[-1][1], interval[1])
    
    return result
