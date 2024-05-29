class Lists():
    def __init__(self,list):
        if not isinstance(list,Lists):
            raise TypeError(list)
        else:
            self.list = list
        
