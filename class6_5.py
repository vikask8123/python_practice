#oop

class TVFunction:
    def tv_fun(self,model,operation):
        print("model: ",model)
        print("operation: ",operation)

class FridgeFunction:
    def fridge_fun(self,model,operation):
        print("model: ",model)
        print("operation: ",operation)
        
tv_obj = TVFunction()
frg_obj = FridgeFunction()

tv_obj.tv_fun("BPL","Video")
frg_obj.fridge_fun("Videcon","cooling")

frg_obj.tv_fun("xyz","audio")
tv_obj.fridge_fun("ABC","cooling")
