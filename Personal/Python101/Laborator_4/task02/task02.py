import numpy as np

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
        self.format = f.readline().strip('/n')
        args = f.readline().strip('/n').split(" ")
        self.rows = int(args[0])
        self.columns = int(args[1])
        self.max_value = f.readline().split('/n')

        data = f.read().split('/n')
        r = open('da.txt', 'w')
        array = np.array(data)
        r.writelines(array)
        self.pixels = array.reshape(self.rows, self.columns, 3)
    def write(self, filename):
        # write to file in the correct format (see README and input examples)
        pass
