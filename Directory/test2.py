class TpsDiff:
    def __init__(self,maxi):
        self.count=0
        self.maximum=maxi
    def self(self):
        self.count+=1
        if self.count==self.maximum:
            return True
            self.count=0
        else:
            return False
            
premier=TpsDiff(5)
while True:
    premier.self()
    
    
    
