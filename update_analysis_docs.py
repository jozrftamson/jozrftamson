#!/usr/bin/env python3
import json
import re

# Load latest stats
with open('latest_stats.json', 'r') as f:
    stats = json.load(f)

print(f"📊 Updating documents with latest data...")
print(f"Total Repos: {stats['total']}")
print(f"Python Repos: {stats['languages'][1]['count']}")

# Update GITHUB_ACCOUNT_COMPLETE_ANALYSIS.md
with open('GITHUB_ACCOUNT_COMPLETE_ANALYSIS.md', 'r') as f:
    content = f.read()

# Replace old numbers with new ones
content = re.sub(r'223 Repositories', f"{stats['total']} Repositories", content)
content = re.sub(r'Total: 223 Repos', f"Total: {stats['total']} Repos", content)
content = re.sub(r'Python\s+45', f"Python {stats['languages'][1]['count']}", content)
content = re.sub(r'Original:\s+40', f"Original: {stats['original']}", content)
content = re.sub(r'💎 Original:\s+40', f"💎 Original: {stats['original']}", content)
content = re.sub(r'Analysedatum:\*\* 3\. August 2026', f"Analysedatum:** {stats['updated']}", content)

with open('GITHUB_ACCOUNT_COMPLETE_ANALYSIS.md', 'w') as f:
    f.write(content)

print("✅ Updated GITHUB_ACCOUNT_COMPLETE_ANALYSIS.md")

# Update VISUAL_SUMMARY.md
with open('VISUAL_SUMMARY.md', 'r') as f:
    content = f.read()

content = re.sub(r'Total: 223 Repos', f"Total: {stats['total']} Repos", content)
content = re.sub(r'Python\s+45', f"Python {stats['languages'][1]['count']}", content)
content = re.sub(r'Original:\s+40', f"Original: {stats['original']}", content)

with open('VISUAL_SUMMARY.md', 'w') as f:
    f.write(content)

print("✅ Updated VISUAL_SUMMARY.md")

# Update ACCOUNT_ANALYSIS_REPORT.md
with open('ACCOUNT_ANALYSIS_REPORT.md', 'r') as f:
    content = f.read()

content = re.sub(r'223 Repositories', f"{stats['total']} Repositories", content)
content = re.sub(r'Python\s+45', f"Python {stats['languages'][1]['count']}", content)
content = re.sub(r'Original:\s+40', f"Original: {stats['original']}", content)

with open('ACCOUNT_ANALYSIS_REPORT.md', 'w') as f:
    f.write(content)

print("✅ Updated ACCOUNT_ANALYSIS_REPORT.md")

print(f"\n🎉 All documents updated with latest data from {stats['updated']}")
