class Counter:
    #생성자
    def __init__(self):
        self.count=0
    def reset(self):
        self.count=0
    def increment(self):
        self.count+=1
    def get(self):
        return self.count


