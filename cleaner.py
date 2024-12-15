def filter_nondigits(data: list) -> list:
    """
    Filter all strings from list that are not integers

    Args:
        data (list[str]): list of strings representing heart rate samples.
            Might contain invalid or missing data.
    Returns:
        list[int]: list of integers, with all non-digit strings removed
    """
    #creating new list with just integers
    new_data = []

    for item in data:
        x = item.strip()

        if x.isdigit():
         new_data.append(int(x))
        else:
         continue
    return new_data

#flitering heart rate data to return wanted values
def filter_outliers(data: list) -> list:
    hrt =[]
    for item in data:
       if item >30 and item <250:
          hrt.append(item)
       else:
          continue
    return hrt
             
        
