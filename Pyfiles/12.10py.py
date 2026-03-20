def recur_fibo(n):
    if n == 0:  
        return 0
    elif n == 1:  
        return 1
    return recur_fibo(n - 1) + recur_fibo(n - 2)

def main():
    nterms = int(input())
    for i in range(nterms):
        print(recur_fibo(i))

if __name__ == "__main__":
    main()
