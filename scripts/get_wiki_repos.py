"""Get the list of wiki repos from the GitHub API."""

import json
from pathlib import Path

import requests

GET_REPOS_URL = "https://api.github.com/orgs/letsbuildawiki/repos"

NON_WIKI_REPOS = [
    "letsbuildawiki.github.io",
]


def get_wiki_repos() -> None:
    """Get the list of wiki repos from the GitHub API."""
    all_repos = requests.get(GET_REPOS_URL, timeout=500).json()
    wiki_repos = [
        {"name": repo["name"], "url": repo["homepage"]}
        for repo in all_repos
        if repo["name"] not in NON_WIKI_REPOS
    ]
    path=Path("./site/_data/repos.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as file:
        file.write(json.dumps(wiki_repos))


if __name__ == "__main__":
    get_wiki_repos()
