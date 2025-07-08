# there should be a abstract class can have and non abstract class also can use

from abc import ABC, abstractmethod # we should import


class featurePlan(ABC):
    @abstractmethod  #we use this called as abstract class this mantory to use in child class
    def feature(self):
        pass

    # def logout(self):   # this was not a abstract class this was not mantory to use in the child class
    #     pass
    #