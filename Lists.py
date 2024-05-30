class Lists():
    def __init__(self,in_list):
        if not isinstance(in_list,list):
            raise TypeError(in_list)
        else:
            self.list = in_list
            self.keys = list(in_list[0].keys())
            print(self.keys)
    def print_contents(self):
        print(self.list)
    def add(self,*args):
        i = 0
        tempdict = {}
        for arg in args:
            tempdict[self.keys[i]]= arg
            i +=1
        self.list.append(tempdict)
    def edit(self, index : int,keys : list,inputs : list):
        i=0
        while i<len(keys):
            self.list[index][keys[i]] = inputs[i]
            i += 1
    def delete(self,index :int):
        self.list.pop(index)
        
        


products = Lists([{'product_name': 'Pepsi', 'price': '80'}])
products.add("Pepsi","80")
products.print_contents()
products.edit(0,["product_name","price"],["Coke","100"])
products.print_contents()
products.delete(1)
products.print_contents()