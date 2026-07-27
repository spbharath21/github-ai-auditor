#### fetcher.py

from dataclasses import dataclass

from pathlib import Path



from github import Github

from dotenv import load\_dotenv



import os



load\_dotenv()

token = os.getenv("GITHUB\_TOKEN")

g = Github(token)



@dataclass

class RepoFile:

&#x20;   path: str

&#x20;   content: str



ALLOWED\_EXTENSIONS = {

&#x20;   ".py",

&#x20;   ".js",

&#x20;   ".ts",

&#x20;   ".java",

&#x20;   ".go",

&#x20;   ".cpp",

&#x20;   ".c",

&#x20;   ".cs",

&#x20;   ".php",

&#x20;   ".rb",

}



def get\_repository(repo\_name):

&#x20;   return g.get\_repo(repo\_name)



def fetch\_files(repo\_name: str):

&#x20;   repo = get\_repository(repo\_name)

&#x20;   contents = repo.get\_contents("")



&#x20;   files = \[]

&#x20;   while contents:

&#x20;       item = contents.pop(0)



&#x20;       if item.type == "dir" :

&#x20;           contents.extend(repo.get\_contents(item.path))



&#x20;       else:

&#x20;           files.append(item)



&#x20;   return files



def is\_code\_file(path: str):

&#x20;   extension = Path(path).suffix.lower()



&#x20;   return extension in ALLOWED\_EXTENSIONS



def get\_file\_content(file):



&#x20;   try:

&#x20;       return file.decoded\_content.decode("utf-8")



&#x20;   except Exception:

&#x20;       return None



def collect\_repository\_files(repo\_name: str):



&#x20;   repository\_files = \[]



&#x20;   for file in fetch\_files(repo\_name):



&#x20;       if not is\_code\_file(file.path):

&#x20;           continue



&#x20;       content = get\_file\_content(file)



&#x20;       if content is None:

&#x20;           continue



&#x20;       repository\_files.append(

&#x20;           RepoFile(

&#x20;               path=file.path,

&#x20;               content=content

&#x20;           )

&#x20;       )



&#x20;   return repository\_files



#### pyprojec.toml

\[project]

name = "github-ai-auditor"

version = "0.1.0"

description = "Scans GitHub repos for OWASP LLM Top 10 vulnerabilities and security issues"

requires-python = ">=3.10"

dependencies = \[

&#x20;   "PyGithub>=2.3.0",

&#x20;   "python-dotenv>=1.0.0",

&#x20;   "rich>=13.7.0",

&#x20;   "jinja2>=3.1.0",

&#x20;   "click>=8.1.0",

]



\[project.scripts]

aiaudit = "auditor.cli:main"



\[build-system]

requires = \["setuptools>=68.0"]

build-backend = "setuptools.build\_meta"



\[tool.setuptools.packages.find]

include = \["auditor\*"]



#### .gitignore

venv/

\_\_pycache\_\_/

\*.pyc

.env

\*.egg-info/

.vscode/

reports/



#### .env

GITHUB\_TOKEN=ghp\_vB829zO1G4REHEkuVIgvleJJhYaxfU45sbKM



#### test\_fetcher.py

from auditor.fetcher import collect\_repository\_files



files = collect\_repository\_files("pallets/click")



print(f"Found {len(files)} code files\\n")



for file in files\[:10]:

&#x20; print(file.path)

&#x20;





