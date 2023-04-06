def fact(n):
    if(n>1):
        return n*fact(n-1)
    else:
        return 1
    


def main():
    n =0
    while(n!=16):
        result = fact(n)
        print(str(n)+'! = '+str(result)+'\n')
        n=n+2


    

 

if __name__ == '__main__':
    main()


