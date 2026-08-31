print("-------------------------------------------------------------------\n")

repeat
    io.write("Enter your first digit: ")
    io.flush()
    local dig1 = io.read("*n")

    io.write("Enter your second digit: ")
    io.flush()
    local dig2 = io.read("*n")
    print()

    io.read()

    io.write("What would you like to do? [add/subtract/multiply/divide] ")
    io.flush()
    local operator = io.read()
    
    print()

    if operator == "add" then
        print(dig1 + dig2)

    elseif operator == "subtract" then
        print(dig1 - dig2)
    
    elseif operator == "multiply" then
        print(dig1 * dig2)

    elseif operator == "divide" then
        print(dig1 / dig2)

    elseif operator == "exit" then
        print("Bye!")
    
    else
        print("Unknown input")
    end

    print("\n-------------------------------------------------------------------")
    print()

until operator == "exit"
