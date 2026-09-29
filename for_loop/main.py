import sys

sys.stdin = open("for_loop/input.txt", "r")  # noqa
sys.stdout = open("for_loop/output.txt", "w")  # noqa

for i in range(5):
    print(f"The value of i is {i}")
    print()
    for k in range(5):
        print(f"The value of k is {k}")
        print()
        for j in range(5):
            print(f"The value of j is {j}")
