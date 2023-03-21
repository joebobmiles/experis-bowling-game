class Frame(object):
    def __init__(self, number, points = (None, None)):
        self.number = number
        self.points = [ points[0], points[1] ]
        self.score = None 

        self.prev = None
        self.next = None

    def set_points(self, index, value):
        self.points[index] = value

    def compute_score(self):
        return self.points[0] + self.points[1]