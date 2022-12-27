from pprint import pprint

from chalicelib.config import settings
from chalicelib.logger_app import logger
from github import Github

github_token = settings.GITHUB_TOKEN
gh = Github(github_token)
gh_user = gh.get_user()


def update_file(filename, message, repo, branch="main"):
    repo = gh.get_repo(full_name_or_id=repo)
    contents = repo.get_contents(filename, ref="main")
    sha = contents.sha
    res = repo.update_file(contents.path, message, f"{sha}", sha, branch=branch)
    commit = res["commit"]
    logger.info(f"New commit is at {commit.html_url}")
    return commit.html_url
