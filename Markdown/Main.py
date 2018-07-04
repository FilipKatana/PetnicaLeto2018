import HtmlGen as hg


class MarkdownGenerator:
    def __init__(self, prompt):
        self.code = input(prompt)


    def __read_code(self, c):
        if c[0:2] == "**" and c[::-1][0:2] == "**":
            try:
                c = c[2:-2]
                return "<b>" + c + "</b>"
            except:
                return ""
        if c[0] == "*" and c[-1] == "*":
            try:
                c = c[1:-1]
                return "<em>" + c + "</em>"
            except:
                return ""

        if c[0:2] == "~~" and c[::-1][0:2] == "~~":
            try:
                c = c[2:-2]
                return "<del>" + c + "</del>"
            except:
                return ""

        if c[0:2] == "__" and c[::-1][0:2] == "__":
            try:
                c = c[2:-2]
                return "<b>" + c + "</b>"
            except:
                return ""

        return c


            

    def __construct(self, enter):
        complete_code = enter.split()
        result = "<p> "
        for word in complete_code:
            result += self.__read_code(word)
            result += " "
        return result + " </p>"

    def write_to_file(self, file_name):
        data = self.__construct(self.code)
        f = open(file_name, "w")
        f.write(data)
        f.close()



m = MarkdownGenerator("Enter something: ")
m.write_to_file("OIEDJI.html")
            
        
