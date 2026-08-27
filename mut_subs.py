#In the terminal command line, we write:
#export GITHUB_TOKEN=’insert_github_token_here'
#Python3 mut_subs.py
import os
import requests

# --- SETTINGS --- run from the console: python mut_subs.py
TOKEN = os.environ.get("GITHUB_TOKEN")
if not TOKEN:
    raise ValueError("GITHUB_TOKEN is not set. Run: export GITHUB_TOKEN='ghp_...'"
                     "\nOr pass the token via an environment variable.")

HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github+json",
}
BASE_URL = "https://api.github.com"

def fetch_logins(endpoint):
    """Loads all logins, taking pagination into account (if there are many subscriptions)."""
    logins = []
    url = endpoint
    while url:
        resp = requests.get(url, headers=HEADERS)
        resp.raise_for_status()
        data = resp.json()
        logins.extend(user["login"] for user in data)
        # GitHub returns links to the next page in the Link headers
        links = resp.links
        url = links.get("next", {}).get("url")
    return set(logins)

def main():
    print("Loading followers (who is following you)...")
    followers = fetch_logins(f"{BASE_URL}/user/followers")

    print("Loading following (who is following you)...")
    following = fetch_logins(f"{BASE_URL}/user/following")

    # Those you follow but who don’t follow you back
    non_mutual = following - followers

    total_following = len(following)
    mutual_count = len(followers & following)
    non_mutual_count = len(non_mutual)

    print("\n--- Result ---")
    print(f"Total subscriptions (following): {total_following}")
    print(f"Mutual subscriptions: {mutual_count}")
    print(f"Non-mutual (you follow them, they don't follow you): {non_mutual_count}\n")

    if non_mutual:
        print("List of users (non-mutual):")
        for login in sorted(non_mutual):
            print(login)
    else:
        print("All your subscriptions are mutual — there’s no one to unsubscribe from.")

if __name__ == "__main__":
    main()
