import requests
import matplotlib.pyplot as plt
import csv
import time


username = ""
token = "" 


headers = {"Authorization": f"token {token}"} if token else {}

repos = []
page = 1

print(f"🔍 Fetching repositories for user: {username} ...\n")


while True:
    url = f"https://api.github.com/users/{username}/repos?page={page}&per_page=100"
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error fetching page {page}: {response.status_code} {response.text}")
        break

    data = response.json()
    if not data:
        break

    repos.extend(data)
    print(f"Page {page} fetched ({len(data)} repos)")
    page += 1
    time.sleep(0.2)

if not repos:
    print("No repositories found or API limit reached.")
    exit()


language_totals = {}
for repo in repos:
    if repo.get("fork"):
        continue 
    
    lang_url = repo.get("languages_url")
    if not lang_url:
        continue

    try:
        langs_response = requests.get(lang_url, headers=headers)
        if langs_response.status_code != 200:
            print(f"Skipping {repo['name']} (HTTP {langs_response.status_code})")
            continue

        langs = langs_response.json()
        for lang, count in langs.items():
            try:
                language_totals[lang] = language_totals.get(lang, 0) + int(count)
            except ValueError:
                print(f"Invalid count for {lang} in {repo['name']}: {count}")
                continue

    except Exception as e:
        print(f"Error processing {repo['name']}: {e}")
        continue


total_bytes = sum(language_totals.values())

if not total_bytes:
    print(" No language data found.")
    exit()

print(f"\nLanguage Usage Summary for {username}")
print("==========================================")

sorted_langs = sorted(language_totals.items(), key=lambda x: x[1], reverse=True)
for lang, count in sorted_langs:
    percent = (count / total_bytes) * 100
    print(f"{lang:20s}: {percent:6.2f}%")


csv_filename = "github_language_stats.csv"
with open(csv_filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Language", "Bytes", "Percentage"])
    for lang, count in sorted_langs:
        percent = (count / total_bytes) * 100
        writer.writerow([lang, count, f"{percent:.2f}%"])

print(f"\nReport saved as {csv_filename}")


plt.figure(figsize=(8, 8))
plt.pie(
    [count for _, count in sorted_langs],
    labels=[lang for lang, _ in sorted_langs],
    autopct="%1.1f%%",
    startangle=140
)
plt.title(f"Languages used by {username}")
plt.show()
