class Image():
    def __init__(self, format='P3', rows=0, columns=0, max_value=255, pixels=[[]]):
        self.format = format
        self.rows = rows
        self.columns = columns
        self.max_value = max_value
        self.pixels = pixels
    def __str__(self):
        # use this for debugging
        image = ""
        image += f"{self.format}{self.rows} {self.columns}\n{self.max_value}\n"
        for i in range(self.rows):
            for j in range(3 * self.columns):
                image += f"{self.pixels[i][j]} "
            image += "\n"
        return image
    def sepia(self):
        # apply sepia filter to the image
        pass
    def read(self, filename):
        # read from file and assign the correct parameters (see README and input examples)
        f = open(filename, 'r')
        lines = f.readlines()
        self.format = lines[0]
        args = lines[1].split(" ")
        self.rows = args[0]
        self.columns = args[1]
        self.max_value = lines[2]

        

        pass
    def write(self, filename):
        # write to file in the correct format (see README and input examples)
        pass
