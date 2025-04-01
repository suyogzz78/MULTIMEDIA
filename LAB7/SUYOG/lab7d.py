def run_length_encoding(input_string):
    if not input_string:
        return ""
    
    count = 1
    prev_char = input_string[0]
    output = ""

    for char in input_string[1:]:
        if char == prev_char:
            count += 1
        else:
            output += str(count) + prev_char
            count = 1
            prev_char = char

    # Append the last counted character sequence
    output += str(count) + prev_char

    return output

input_string = "aaabbbbccddde"
encoded_string = run_length_encoding(input_string)
print(encoded_string)
