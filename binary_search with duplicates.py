
def binsearch(keys, query, low, high, res):
    # if the query less than or equal the last elemnt in the left array then the query must be in the left
    if high > low : return res
    mid = (low+high)//2
    if query == keys[mid]:
        res = mid
        return binsearch(keys, query, low, mid-1, res)
            
    if query < keys[mid]:
        return binsearch(keys, query, low, mid-1, res)
    elif query > keys[mid]:
        return binsearch(keys, query, mid+1, high, res)

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys
    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries
    res = -1
    for q in input_queries:
        print(binsearch(input_keys, q, 0, num_keys-1, res), end=' ')
        
