from abc import ABCMeta.abstractmethod

class DuaDimensi(metaclass=ABCMeta):
    @abstractmethod
    def luas(self):
        pass

    class SegiEmpat(DuaDimensi):
        def __init__(selfself, p, l):
            self.panjang