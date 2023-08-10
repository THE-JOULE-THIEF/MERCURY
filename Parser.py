class Parser:
    def parser(self, parse_string: str) -> dict:
        char_array = list(parse_string)
        
        index = 0
        temp_parse_string = ""
        parse_list = []
        STRFLG = False
        
        while index < len(char_array):
            if (char_array[index] == " ") and (not STRFLG):
                parse_list.append(temp_parse_string)
                temp_parse_string = ""
            elif (char_array[index] == "\""):
                STRFLG = not(STRFLG)
            else:
                temp_parse_string += char_array[index]
            index += 1
            
        parse_list.append(temp_parse_string)
        temp_parse_string = ""
        
        parse_dict = dict()
        parse_dict["module"] = parse_list[0]
        parse_dict["args"] = parse_list[1:]
        
        return parse_dict