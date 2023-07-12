def file(file="Assignment7.txt"):
    try:
        # Open the file in append mode
        f = open(file, "a")
        
        # Write data to the file
        rollNumber = "61"
        name = "Maroof"
        className = "SYCO"
        f.writelines([rollNumber + "\n", name + "\n", className + "\n"])
                
        # Reopen the file in read mode
        f = open(file, "r")
        
        # Read and print the data from the file
        print(f.readlines())

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except IOError as e:
        print(f"Error: {e}")

# Call the function
file()