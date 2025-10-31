import os
from enum import Enum
from functools import cache
from pathlib import Path
from typing import Type, Optional, Callable

import dotenv
import requests
import yaml
from dotenv import load_dotenv
from git import Repo, DiffIndex, Blob

PROJECT_ROOT = Path(__file__).parent.parent.parent
def get_repo():
    repo: Repo = Repo(search_parent_directories=True)
    repo.remotes.origin.fetch(verbose=False)
    return repo

def _get_git_merge_diff(dirs_to_check: list[str] = None) -> DiffIndex:
    repo = get_repo()
    head_commit = repo.commit('HEAD')

    previous_commit = head_commit.parents[0]

    git_diff: DiffIndex = previous_commit.diff(head_commit, paths=dirs_to_check)

    return git_diff

if __name__ == "__main__":
    # git_merge_diff_dict: YamlDiffDict = get_git_merge_diff_dict()
    repo = get_repo()
    head_commit = repo.commit('HEAD')

    print(head_commit)
    previous_commit = head_commit.parents[0]
