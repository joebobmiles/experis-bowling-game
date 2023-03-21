class Frame(object):
    def __init__(self, number):

        self.number = number
        self.points = [ None, None ]
        self.score = None 

        self.prev = None
        self.next = None

        self.__points_callbacks = [
            [],
            []
        ]

    def set_points(self, index, value):
        self.points[index] = value

        for callback in self.__points_callbacks[index]:
            callback(value)

    def subscribe_to_points(self, index, callback):
        self.__points_callbacks[index].append(callback)