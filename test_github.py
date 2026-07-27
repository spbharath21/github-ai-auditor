from github import Github  # type: ignore
from dotenv import load_dotenv
import os

load_dotenv()

g = Github(os.getenv("GITHUB_TOKEN"))

user = g.get_user()

print(user.login)