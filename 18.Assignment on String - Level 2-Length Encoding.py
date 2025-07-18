#lex_auth_012693816331657216161

def encode(message):
    encoded_message = ""
    count = 1

    # Iterate through the message
    for i in range(len(message)):
        # If the current character is the same as the next one, increment the count
        if i < len(message) - 1 and message[i] == message[i + 1]:
            count += 1
        else:
            # Append the character and its count to the encoded message
            encoded_message += str(count) + message[i]
            count = 1  # Reset count for the next character

    return encoded_message

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)