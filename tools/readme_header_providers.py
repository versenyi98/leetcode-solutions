from abc import ABC, abstractmethod


class HeaderProvider(ABC):
    @abstractmethod
    def get(self):
        pass


class LeetCodeHeaderProvider(HeaderProvider):
    def get(self):
        header = "| ID | Link to description | Link to solution\n" + \
                 "|:---|:---|:---:|\n"
        return header
