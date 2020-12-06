# function that creates a list containing the english ASCII codes (keys) and english characters (values)
def en_create():
    en_dict = {ord(chr(i)): chr(i) for i in range(65, 91)}
    en_dict.update({ord(chr(i)): chr(i) for i in range(97, 123)})
    # Adding manually some special cases . eg (P+S in Greek-lish is translated as Ψ in English)
    en_dict.update(({32: ' ', 163: 'P' + 'S', 227: 'p' + 's', 158: 'K' + 'S', 222: 'k' + 's', 56: '8', 147: 's' + ' '}))
    en_dict[190] = 'K' + 's'
    en_dict[195] = 'P' + 's'
    return en_dict


# function that creates a list containing the greek ASCII codes (keys) and greek characters (values)
def gr_create():
    gr_dict = {ord(chr(i)): chr(i) for i in range(913, 938)}
    # Below we are adding manually some special cases . eg (P+S in Greek-lish is translated as Ψ in English)
    gr_dict.update({ord(chr(i)): chr(i) for i in range(945, 970)})
    gr_dict.update({32: ' ', 936: 'Ψ', 968: 'ψ', 926: 'Ξ', 958: 'ξ', 920: 'Θ', 952: 'θ', 962: 'ς'})
    return gr_dict


# function that connects the english ASCII codes (keys) with the greek ASCII codes (values)
def con_en():
    con_dict = {i: (848 + i) for i in range(65, 91)}  # 848 is the const.diff. between the GR and EN ASCII (913-65=848)
    con_dict.update({i: (848 + i) for i in range(97, 122)})
    con_dict.update({86: 914, 71: 915, 68: 916, 90: 918, 76: 923, 75: 922, 77: 924, 78: 925, 227: 968, 222: 958})
    con_dict.update({79: 927, 80: 928, 82: 929, 89: 933, 70: 934, 88: 935, 87: 937, 32: 32, 163: 936, 158: 926, 195: 936})
    con_dict.update({118: 946, 103: 947, 104: 951, 107: 954, 108: 955, 109: 956, 110: 957, 74: 926, 56: 920, 190: 926})
    con_dict.update({102: 966, 120: 967, 119: 969, 122: 950, 114: 961, 121: 965, 56: 952, 107: 954, 147: 962})
    return con_dict


# function that connects the greek ASCII codes (keys) with the english ASCII codes (values)
def con_gr():
    con_dict = {i: (i - 848) for i in range(913, 939)}
    con_dict.update({i: (i - 848) for i in range(945, 970)})
    con_dict.update({914: 86, 915: 71, 916: 68, 918: 90, 922: 75, 923: 76, 924: 77, 925: 78, 968: 227, 958: 222})
    con_dict.update({927: 79, 928: 80, 929: 82, 933: 89, 934: 70, 935: 88, 937: 87, 32: 32, 936: 163, 926: 158})
    con_dict.update({946: 118, 947: 103, 950: 122, 951: 104, 953: 105, 955: 108, 956: 109, 957: 110, 920: 56, 958: 190})
    con_dict.update({961: 114, 965: 121, 966: 102, 967: 120, 969: 119, 919: 72, 952: 56, 954: 107, 962: 147, 926: 190, 936: 195})
    return con_dict


def main():
    print('!Current version does not support special characters ( ! , * , #). Your string must only contain letters!')
    print(' ')
    english = en_create()
    greek = gr_create()
    connected_gr = con_gr()
    connected_en = con_en()
    string = str(input('Please provide a string in Greek-lish (latin characters) or Greek : '))

    if ord(string[0]) in english:  # Check if the 1st ASCII value is in the English or Greek dictionary. This is EN.

        original_ascii = []
        translated_ascii = []
        trans_str = ''
        length = len(string)
        i = 0

        while i < length:

            # Checking if we are in the special case k+s

            if string[i] == 'K' or string[i] == 'k':
                if string[i + 1] == 'S':
                    special_case = ord(string[i]) + ord(string[i + 1])
                    original_ascii.append(special_case)  # list containing the original ASCII values of the string.
                    i += 2
                elif string[i + 1] == 's':
                    special_case = ord(string[i]) + ord(string[i + 1])
                    original_ascii.append(special_case)
                    i += 2
                else:
                    original_ascii.append(ord(string[i]))
                    i += 1

            # Checking if we are in the special case p+s

            elif string[i] == 'P' or string[i] == 'p':
                if string[i + 1] == 'S':
                    special_case = ord(string[i]) + ord(string[i + 1])
                    original_ascii.append(special_case)
                    i += 2
                elif string[i + 1] == 's':
                    special_case = ord(string[i]) + ord(string[i + 1])
                    original_ascii.append(special_case)
                    i += 2
                else:
                    original_ascii.append(ord(string[i]))
                    i += 1

            # Special case for s in the end of a word where in greek it's ς and not σ

            elif string[i] == 's':
                if i == length - 1:
                    special_case = 147
                    original_ascii.append(special_case)
                    break
                elif string[i+1] == ' ':
                    special_case = 147
                    original_ascii.append(special_case)
                    i += 1
            else:
                original_ascii.append(ord(string[i]))  # Create a list containing the ASCII values of the string.
                i += 1

        for i in original_ascii:    # this is where the list we created above is used to connect the dictionaries
            translated_ascii.append(connected_en[i])  # Create a list with the translated ASCII values.
        for i in translated_ascii:
            trans_str += greek[i]  # Translate using the new ASCII values
        print(trans_str)

    elif ord(string[0]) in greek:  # Check if the 1st ASCII value is in the English or Greek dictionary. This is GR.

        original_ascii = []
        translated_ascii = []
        trans_str = ''
        length = len(string)

        for i in range(length):
            original_ascii.append(ord(string[i]))
        for i in original_ascii:
            translated_ascii.append(connected_gr[i])
        for i in translated_ascii:
            trans_str += english[i]
        print(trans_str)


if __name__ == '__main__':
    main()
