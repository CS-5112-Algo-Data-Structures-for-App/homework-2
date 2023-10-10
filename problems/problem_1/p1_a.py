# Problem 1a

def maxsum_list(xs) -> int:
   
    # Edge Cases
    if len(xs) == 0:
        return 0
    
    if len(xs) == 1:
        return xs[0]
    
    if len(xs) == 2:
        return max(xs)
    
    memo = [0] * len(xs)
    memo[0] = xs[0]
    memo[1] = max(xs[0], xs[1])
    
    for i in range(2, len(xs)):
        memo[i] = max(memo[i - 1], memo[i - 2] + xs[i])
        
    return memo[-1]




if __name__ == '__main__':
    print(maxsum_list([10,1,1,1,10])) # ans21