def top_n (items,n):
    """Return the top n items in array, in desc order.

    Args: 
    items (array): list or array-like object
    n (int): num of items to return 

    Return:
    array: top n items, desc order

    Egs:
    >>>top_n([8,3,2,7,4], 3)
    [8,7,4]
    """
    for i n range(n): #keep sorting until we have the top
    for j in range(len(items)-1-i):

        if items [j] > items[j+1]:  #if this item is big
            items[j], items[j+1] = items[j=+1], items[j]

            # get last two items
            top_n = items[-n:]

            # return in descending order
            return top_n[::-1]