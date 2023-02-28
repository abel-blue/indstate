def sumRange(start, end, num):
    sum=0;
    for i in range(start, end, 1):
        num_str = repr(i)
        last_digit_str = num_str[-1]
        last_digit = int(last_digit_str)
        if(last_digit==num):
            sum+=i
    print(sum)

sumRange(3123, 26837, 4)