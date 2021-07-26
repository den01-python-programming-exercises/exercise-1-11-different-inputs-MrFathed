def main():
    #write your code below this line
    string_input = input("Give a string:")
    int_input = int(input("Give an integer:"))
    float_input = float(input("Give a float:"))
    bool_input = bool(input("Give a boolean:"))

    print("You gave the string " + string_input)
    print("You gave the integer " + str(int_input))
    print("You gave the float " + str(float_input))
    print("You gave the boolean " + str(bool_input))

if __name__ == '__main__':
    main()
