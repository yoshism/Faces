def main():
    #ask user for input
    input_text = input("Your text here -")


    #define a function
    def convert(x):

        # #add emoji
        smiley_face = "🙂"
        sad_face = "🙁"
        # capital letter
        #x = x.capitalize()
        # replace with emoji
        replace_input = x.replace(":)", smiley_face)
        sad_replace = replace_input.replace(":(", sad_face)

        final_output = sad_replace

        return final_output

    final = convert(input_text)


    #final_output = final_output.capitalize()

    print(final)

main()
