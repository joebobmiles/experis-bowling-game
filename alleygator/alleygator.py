class ScoreCard(object):
    def __init__(self, frames):
        self.frames = frames

    def __getitem__(self, indices):
        # According to SO, sometimes we get a tuple instead of a single value.
        # https://stackoverflow.com/questions/41686020/python-custom-class-indexing
        # if not isinstance(indices, tuple):
        #     indices = tuple(indices)

        return self.frames[indices]