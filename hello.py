import sys

def greet(name):
    print(f"Halo, {name}! Selamat datang di DevOps 13 Alber.")
    print("update code")

if __name__ == "__main__":
    nama = sys.argv[1] if len(sys.argv) > 1 else "Dunia"
    greet(nama)
