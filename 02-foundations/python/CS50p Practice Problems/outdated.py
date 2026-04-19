def main():
    #get input
    anno_domini = input("Date: ")
    anno_domini = anno_domini.strip()

    #split between two formats
    if "/" in anno_domini:
        #mm/dd/yyyy format
        split = anno_domini.split("/")
        if any(sect.isalpha() for sect in split):
             main()

        #check for valid parameters
        if int(split[0]) > 12:
             main()
        if int(split[1]) > 31:
             main()

        #add a 0 infront of certain values
        if len(split[0]) == 1:
            split[0] = "0" + split[0]
        if len(split[1]) == 1:
            split[1] = "0" + split[1]

        final_form = list_reorderer(split)
        print(final_form)
    elif "," in anno_domini:
        #MMMM DD, YYYY format
        months = {
            "January" : "01",
            "February" : "02",
            "March" : "03",
            "April" : "04",
            "May" : "05",
            "June" : "06",
            "July" : "07",
            "August" : "08",
            "September" : "09",
            "October" : "10",
            "November" : "11",
            "December" : "12",
                }
        #remove "," and split
        split = anno_domini.replace(',', '')
        split = split.split()

        #make sure the parameters in the format are valid
        if split[0] not in months:
            main()
        if int(split[1]) > 31:
            main()
        if len(split[1]) == 1:
            split[1] = "0" + split[1]

        #output atp is "['March', '08', '1999']"
        #need to change 'March' to a number
        split[0] = months[split[0]]\

        #output is now "['03', '08', '1999']"
        #need to change to "['1999', '03', '08']
        final_form = list_reorderer(split)

        print(final_form)
    else:
        main()


def list_reorderer(unordered_list):
        #for MMMM DD, YYYY format
        ordered_list = [unordered_list[2], unordered_list[0], unordered_list[1]]

        #now need to return YYYY-MM-DD
        final_form = f"{ordered_list[0]}-{ordered_list[1]}-{ordered_list[2]}"
        return final_form


main()
