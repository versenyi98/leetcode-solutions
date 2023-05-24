import argparse

from workspace_creators import LeetCodeWorkspaceCreator


def prepare_workspace_for_problem(name: str):
    workspace_creator = LeetCodeWorkspaceCreator(name)
    workspace_creator.create_workspace()


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("name")

    args = arg_parser.parse_args()

    prepare_workspace_for_problem(args.name)


if __name__ == "__main__":
    main()
