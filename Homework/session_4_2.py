def maximum_candy(money, price, wrapper):
    if wrapper <= 1:
        return "Infinity"
    else:
        bought_candy = money // price
        if bought_candy < wrapper:
            return bought_candy
        else:    
            bought_candy += maximum_candy_plus(wrapper,bought_candy)
            return bought_candy
def maximum_candy_plus(wrapper,remaining_wrapper):
    if remaining_wrapper < wrapper:
        return 0
    else:
        new_candy = remaining_wrapper // wrapper
        remaining_wrapper = new_candy + remaining_wrapper % wrapper
        return new_candy + maximum_candy_plus(wrapper,remaining_wrapper)

def minimum_square(N, M):
    if N <= 1 or M <= 1:
        return (N*M)
    else:
        length, width = max(M,N), min(M,N)
        max_square_length = 1
        i = 0
        loop = True
        while loop:
            i += 1
            if pow(2,i) <= width:
                max_square_length = pow(2,i)
            else:
                loop = False 
        return 1 + minimum_square(width - max_square_length, max_square_length) + minimum_square(width,length - max_square_length)

print(maximum_candy(16,2,2))