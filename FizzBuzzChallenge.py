def main():

for i in range(100):
    string = ""
    if i % 3 == 0:
        string = string + "Fizz"
    if i % 5 == 0:
        string = string + "Buzz"
    if i % 5 != 0 and i % 3 != 0:
        string = string + str(i)
    print(string)