def compress(data):
    # Initialize the dictionary with all single-character strings
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    output = []
    current = ""

    # Process the input data one character at a time
    for char in data:
        if current + char in dictionary: 
            current += char  # Extend the string if it exists in the dictionary
        else:
            output.append(dictionary[current])  # Store the code of the current string
            dictionary[current + char] = next_code  # Add new sequence to dictionary
            next_code += 1
            current = char  # Reset current to the new character

    # Output the code for the final string
    if current:
        output.append(dictionary[current])

    return ou
def decompress(codes):
    # Initialize the dictionary with all single-character strings
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256
    output = ""

    # Get the first code and initialize the output
    previous = codes.pop(0)
    output += dictionary[previous]
    previous_char = output  # Store last used string

    # Process the codes one at a time
    for code in codes:
        if code in dictionary:
            current = dictionary[code]
        else:
            # Handle special case when the code is missing from dictionary
            current = previous_char + previous_char[0]

        output += current

        # Add new entry to dictionary
        dictionary[next_code] = previous_char + current[0]
        next_code += 1

        previous_char = current  # Update previous string for next iteration

    return output


# Example usage
data = "ABABABAABABA"
compressed_data = compress(data)
print("Compressed:", compressed_data)

decompressed_data = decompress(compressed_data)
print("Decompressed:", decompressed_data)
