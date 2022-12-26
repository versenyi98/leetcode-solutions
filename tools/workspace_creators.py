import json
import os

from pathlib import Path
from abc import ABC, abstractmethod


class WorkspaceCreator(ABC):
    def __init__(self, name):
        self.base_path = Path(__file__).absolute().parent.parent
        self.name = name

    def create_workspace(self):
        self.create_directory()
        self.write_testcases()
        self.write_info_json()

    @abstractmethod
    def create_directory(self):
        pass

    @abstractmethod
    def write_testcases(self):
        pass

    @abstractmethod
    def write_info_json(self):
        pass


class NoWorkspaceCreator(WorkspaceCreator):
    def create_directory(self):
        pass

    def write_testcases(self):
        pass

    def write_info_json(self):
        pass


class LeetCodeWorkspaceCreator(WorkspaceCreator):
    def __init__(self, problem_name):
        super().__init__(None)
        self.solutions_dir = self.base_path / "solutions"
        self.problem_name = problem_name
        self.problem_dir = None

    def create_directory(self):
        problem_id, problem_name = self.problem_name.split('.')
        problem_dir = "0" * (4 - len(problem_id)) + problem_id + "." + problem_name

        self.problem_dir = self.solutions_dir / problem_dir
        if not os.path.exists(self.problem_dir):
            os.mkdir(self.problem_dir)

    def write_testcases(self):
        pass

    def write_info_json(self):
        problem_id, problem_name = self.problem_name.split('.')

        url = f"https://leetcode.com/problems/{problem_name.strip().lower().replace(' ', '-')}/"

        info = {
            "Name": problem_name.strip(),
            "URL": url,
            "ID": problem_id.strip()
        }

        with open(self.problem_dir / "info.json", "w") as json_handle:
            json.dump(info, json_handle, indent=4)
