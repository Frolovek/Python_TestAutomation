class KeyValueStorage:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        with open(self.path_to_file, "r+") as first:
            for line in first:
                divided_items = line.split('=')
                if isinstance(divided_items[0], int) or isinstance(divided_items[0], float) :
                    raise ValueError
                else:
                    setattr(self, divided_items[0], divided_items[1].rstrip())

    def __getitem__(self, item):
        return getattr(self, item)
