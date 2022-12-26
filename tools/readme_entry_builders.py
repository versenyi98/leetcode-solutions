import constants

from urllib.parse import quote
from abc import ABC, abstractmethod


class EntryBuilder(ABC):
    def __init__(self):
        self.entry = ""

    def get(self):
        return self.entry

    @abstractmethod
    def build(self, data):
        pass


class LeetCodeEntryBuilder(EntryBuilder):
    def build(self, data):
        name = data["Name"]
        problem_id = data["ID"]
        url = data["URL"]

        dir_name = "0" * (4 - len(problem_id)) + problem_id + ". " + name

        path_to_solution = f"{constants.GITHUB_MAIN_BRANCH}/LeetCode/{quote(dir_name)}"

        self.entry = f"| {problem_id} | [{name}]({url}) | [Solution]({path_to_solution})|\n"
        return self

