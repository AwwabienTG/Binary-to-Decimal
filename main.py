import math as m

def BinaryToDecimal(x, choice):
    
    try:
        x = list(str(x))
        sum = 0
        sums = []
        final = ""

        try:
            if choice == "0":
                for j in range(m.floor(len(x)/2)):
                    x[j], x[len(x)-j-1] = x[len(x)-j-1], x[j]
        except:
            print("Invalid choice")

        i = 0
        for bit in x:
            if bit != " " and bit != ".":
                if int(bit) == 1:
                    sum+=2**i
                i+=1
            else:
                sums.append(sum)
                i = 0
                sum = 0
        else:
            sums.append(sum)


        for z, sum in enumerate(sums):
            if z < len(sums) - 1:
                final = final + str(sum) + "."
            else:
                final = final + str(sum)


        return final

    except:
        print("Invalid Input(s)")

input_binary = input("Input a binary number(s) with '.' or ' ' in between: ")
choice = input("Is the binary number(s) read from right to left (0) or from left to right (1): ")

print(BinaryToDecimal(input_binary, choice))

            