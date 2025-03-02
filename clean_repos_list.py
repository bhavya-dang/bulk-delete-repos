import re

def extract_repo_format(url):
    pattern = r'(?:https?:\/\/github\.com\/)?([\w-]+)\/([\w.-]+)'
    match = re.search(pattern, url)
    if match:
        return f"{match.group(1)}\\{match.group(2)}"
    return "Invalid URL"

# Read and process repository URLs from file
formatted_repos = []
with open('repos.txt', 'r', encoding='utf-8') as f:  # Specify encoding
    for line in f:
        parts = line.split('|')
        if parts:
            url = parts[0].strip()
            formatted_output = extract_repo_format(url)
            formatted_repos.append(formatted_output)

# Write formatted repository names to output file
with open('output.txt', 'w', encoding='utf-8') as f:  # Specify encoding
    f.write('\n'.join(formatted_repos))
