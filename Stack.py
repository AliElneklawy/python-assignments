from gc import collect

class FullStack(Exception):
    pass

class Stack():
    def __init__(self, newList=[], startstackLen=1000) -> None:
        assert len(newList) <= startstackLen, "stackLen of the stack is greater than the max stackLen specified"

        if newList is []:
            self.__dataList = []
        else:
            self.__dataList = newList[:]

        self.stackLen = startstackLen

    @property
    def stackLen(self):
        return f"{len(self.__dataList)} (Full)" if len(self.__dataList) == self.__stackLen else len(self.__dataList)

    @stackLen.setter
    def stackLen(self, newstackLen):
        self.__stackLen = newstackLen
        del self.__dataList[newstackLen:]
        collect()
        
    def push(self, *data):
        if len(self.__dataList) + len(data) <= self.__stackLen:
            for elem in data:
                self.__dataList.append(elem)
        else:
            raise FullStack("Stack is full")

    def pop(self):
        if len(self.__dataList) == 0:
            raise IndexError
        return self.__dataList.pop()

    @property
    def peek(self):
        return self.__dataList[-1]

    @property
    def show(self):
        return list(reversed(self.__dataList))
