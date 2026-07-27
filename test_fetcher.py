from auditor.fetcher import collect_repository_files

files = collect_repository_files("pallets/click")

print(f"Found {len(files)} code files\n")

for file in files[:10]:
  print(file.path)
  