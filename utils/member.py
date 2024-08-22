class MyId:

    def __init__(self, id=2):
        self.my_id = id

    def remember(self, id):
        self.my_id = id

    def rid(self):
        return self.my_id


id = MyId()
