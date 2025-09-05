from pacotes import fatorial, fibonacci

def main():
    n_fat = 5
    n_fib = 7

    print(f"Fatorial de {n_fat}: {fatorial(n_fat)}")
    print(f"{n_fib}º termo da sequência de Fibonacci: {fibonacci(n_fib)}")

if __name__ == "__main__":
    main()