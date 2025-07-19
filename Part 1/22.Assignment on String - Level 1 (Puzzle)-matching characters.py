#lex_auth_012693825794351104168

def find_common_characters(msg1, msg2):
    common_characters = ""
    
    # Remove spaces (as per the problem statement)
    msg1 = msg1.replace(" ", "")
    msg2 = msg2.replace(" ", "")
    
    # Case-sensitive comparison (so we DO NOT convert to lowercase)
    for i in range(len(msg1)):
        for j in range(len(msg2)):
            if msg1[i] == msg2[j] and msg1[i] not in common_characters:
                common_characters += msg1[i]
    
    if common_characters:
        return common_characters
    else:
        return -1


#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)