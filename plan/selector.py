# HI

class Register(): 
    def __init__ (self, plans):
        self.plans = plans
    
    def DisplayPlanList():
        # display active plan
        pass
    
    def SelectPlanList(plan):
        # display active plan
        pass
       
    
class Plan():
    def __init__ (self, source, has_normalization_actions):
        self.source = source
        self.has_normalization_actions = has_normalization_actions

# given        
plans_list = [Plan("SomeLibrary", True), Plan("blabhblah", True)]
myregister = Register(plans_list)
# when
myregister.DisplayPlanList()
# then

