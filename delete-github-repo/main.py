import json
import asyncio
import subprocess


with open("./data.json", "r") as file:
    data = json.load(file)


def filter_condition(item):
    value = item.get("f6", None)

    if value is not None:
        return True


def map_filter(item):
    repo_href = item.get("wb-break-all href", None)
    if repo_href is not None:
        pathnames = repo_href.split("/Decolo")
        return "/Decolo" + pathnames[len(pathnames) - 1]


repo_list = list(map(map_filter, filter(filter_condition, data)))


async def delete_repo(repos):
    _repos = list(filter(None, repos))

    for _repo in _repos:
        print(f"Deleting {_repo}")

        command = [
            "gh",
            "api",
            "--method",
            "DELETE",
            "-H",
            "Accept: application/vnd.github+json",
            "-H",
            "X-GitHub-Api-Version: 2022-11-28",
            "/repos" + _repo,
        ]

        result = subprocess.run(command, capture_output=True, text=True)
        
        print(result.stdout)
        print(result.stderr)

asyncio.run(delete_repo(repo_list))
