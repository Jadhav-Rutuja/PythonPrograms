def ChkPrime(Arr,Value):
    Sum =0
    for i in range(0,Value,1):
        #if Arr[i] > 1:
        for no in range(2,Arr[i],1):
            if((Arr[i]%no)==0):
                i+=1
        if i==1:
            Sum = Sum + Arr[i]
    return Sum