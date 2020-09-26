
class prediction:
    def __init__(self,model,data):
        self.model=model
        self.data=data

    def prediction(self):
        return self.model.prediction(self.data)
