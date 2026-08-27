# github-follower-sync

Python script to automatically compare GitHub followers and following lists, and unfollow users who aren’t following back.  
Initial code was generated with Ollama using the Gemma 4:12b model, then reviewed and adapted for reliability and safety.

> ⚠️ **Warning**: This script can perform real actions on your GitHub account (unfollow). Always test with a small subset first or enable a dry-run mode before enabling actual unfollows. Use at your own risk.

## Features

- Fetches your GitHub followers list.
- Compares both lists and identifies non-mutual follows (you follow them, but they don’t follow you).
- Optionally unfollows non-mutual users (configurable via CLI flag).
- Dry-run mode to preview actions without making changes.
- Respects GitHub API rate limits and uses pagination safely.

## Prerequisites

- Python 3.9 or higher.
- A GitHub personal access token with `read:user` and `write:user` scopes (or at least permissions to manage follows).
- `requests` library.

## Installation

1. Clone the repository:

   ```bash
   git clone git clone https://github.com/invweb/github-follower-sync-AI.git
   cd github-follower-sync
   python3 mut_subs.py
