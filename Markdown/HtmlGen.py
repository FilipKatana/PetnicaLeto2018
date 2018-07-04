

class html_element:
    def __init__(self, text = "Text not defined", color = "blue"):
        self.text = text
        self.color = color

    
    def write_to_file(self):
        raise NotImplementedError



class heading(html_element):
    def __init__(self, text = "Text not defined", color = "black"):
        super(heading, self).__init__(text, color)


    def write_to_file(self, file_name = "Example.html"):
        f = open(file_name, "a")
        f.write('<h1 design = "color: ' + self.color + ';">')
        f.write(self.text)
        f.write("</h1>")
        f.close()



class paragraph(html_element):
    def __init__(self, text = "Par text", color = "blue", brk = 10):
        super(paragraph, self).__init__(text, color)
        self.brk = brk

    def write_to_file(self, file_name = "Example.html"):
        f = open(file_name, "a")
        arr = self.text.split()
        i = 0
        f.write('<p design = "color: ' + self.color + ';">')
        for word in arr:
            f.write(word + " ")
            i += 1
            if i == self.brk - 1:
                f.write("<br>")
                i = 0
        f.write("</p>")
        f.close()








