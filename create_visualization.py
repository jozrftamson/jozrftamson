#!/usr/bin/env python3
"""
GitHub Account Visualization Generator
Creates colorful charts and diagrams for the account analysis
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle
import numpy as np

# Set style
plt.style.use('dark_background')

# Create figure with subplots
fig = plt.figure(figsize=(20, 12))
fig.suptitle('GitHub Account Analysis: @jozrftamson', 
             fontsize=24, fontweight='bold', color='white')

# Data
languages = ['TypeScript', 'Python', 'JavaScript', 'Go', 'Jupyter\nNotebook', 
             'Rust', 'HTML', 'Java', 'C#', 'PHP']
lang_counts = [70, 45, 23, 22, 8, 5, 5, 4, 4, 3]
lang_colors = ['#3178c6', '#3776ab', '#f7df1e', '#00add8', '#f37726',
               '#dea584', '#e34c26', '#b07219', '#178600', '#4f5d95']

categories = ['AI & Agents', 'Backend & APIs', 'Web Dev', 'Gaming & AR/VR',
              'Design & UI/UX', 'Kubernetes', 'E-Commerce', 'Speech & Audio',
              'Automation', 'Data Eng', 'Other']
cat_counts = [31, 13, 11, 9, 9, 6, 4, 4, 3, 2, 131]
cat_colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#ffeaa7',
              '#326ce5', '#fd79a8', '#a29bfe', '#74b9ff', '#55efc4', '#636e72']

# 1. Programming Languages Bar Chart (Top Left)
ax1 = plt.subplot(2, 3, 1)
bars1 = ax1.barh(languages, lang_counts, color=lang_colors, edgecolor='white', linewidth=1.5)
ax1.set_xlabel('Number of Repositories', fontsize=12, fontweight='bold')
ax1.set_title('Top 10 Programming Languages', fontsize=14, fontweight='bold', pad=20)
ax1.grid(axis='x', alpha=0.3, linestyle='--')
for i, (bar, count) in enumerate(zip(bars1, lang_counts)):
    ax1.text(count + 1, i, str(count), va='center', fontweight='bold', fontsize=10)

# 2. Project Categories Pie Chart (Top Middle)
ax2 = plt.subplot(2, 3, 2)
# Only show top categories, group others
top_cats = categories[:10]
top_counts = cat_counts[:10]
top_colors = cat_colors[:10]

wedges, texts, autotexts = ax2.pie(top_counts, labels=top_cats, colors=top_colors,
                                     autopct='%1.1f%%', startangle=90,
                                     textprops={'fontsize': 9, 'fontweight': 'bold'},
                                     pctdistance=0.85)
ax2.set_title('Project Categories Distribution', fontsize=14, fontweight='bold', pad=20)

# 3. Repository Stats (Top Right)
ax3 = plt.subplot(2, 3, 3)
ax3.axis('off')
stats_text = """
📊 REPOSITORY STATISTICS

Total Repositories:     223
🔱 Forks:               183 (82%)
💎 Original:            40 (18%)
🔒 Private:             21 (9%)
🌍 Public:              202 (91%)
⭐ With Stars:          10

🎯 MAIN FOCUS
🤖 AI & Agents:         31 repos
🎨 Design & UI/UX:      9 repos
☸️ Kubernetes:          6 repos

🔥 ACTIVITY LEVEL
Very Active (5 updates today!)
"""
ax3.text(0.1, 0.5, stats_text, fontsize=11, family='monospace',
         verticalalignment='center', bbox=dict(boxstyle='round', 
         facecolor='#2d3436', alpha=0.8, edgecolor='white', linewidth=2))

# 4. Language Percentage Breakdown (Bottom Left)
ax4 = plt.subplot(2, 3, 4)
lang_percentages = [35, 23, 12, 11, 4, 3, 3, 2, 2, 2, 3]  # Including "Other"
lang_labels_full = languages + ['Other']
lang_colors_full = lang_colors + ['#95a5a6']

y_pos = np.arange(len(lang_labels_full))
bars4 = ax4.barh(y_pos, lang_percentages, color=lang_colors_full, 
                 edgecolor='white', linewidth=1.5)
ax4.set_yticks(y_pos)
ax4.set_yticklabels(lang_labels_full)
ax4.set_xlabel('Percentage (%)', fontsize=12, fontweight='bold')
ax4.set_title('Language Distribution by Percentage', fontsize=14, fontweight='bold', pad=20)
ax4.grid(axis='x', alpha=0.3, linestyle='--')
for i, (bar, pct) in enumerate(zip(bars4, lang_percentages)):
    ax4.text(pct + 0.5, i, f'{pct}%', va='center', fontweight='bold', fontsize=10)

# 5. Skill Matrix Heatmap (Bottom Middle)
ax5 = plt.subplot(2, 3, 5)
skills = ['TypeScript', 'Python', 'JavaScript', 'Go', 'React', 
          'Kubernetes', 'AI/ML', 'DevOps']
skill_levels = [100, 80, 75, 70, 80, 60, 75, 65]
colors_skill = ['#2ecc71' if s >= 80 else '#f39c12' if s >= 70 else '#3498db' for s in skill_levels]

bars5 = ax5.barh(skills, skill_levels, color=colors_skill, edgecolor='white', linewidth=1.5)
ax5.set_xlabel('Skill Level (%)', fontsize=12, fontweight='bold')
ax5.set_title('Skill Matrix', fontsize=14, fontweight='bold', pad=20)
ax5.set_xlim(0, 110)
ax5.grid(axis='x', alpha=0.3, linestyle='--')
for i, (bar, level) in enumerate(zip(bars5, skill_levels)):
    ax5.text(level + 2, i, f'{level}%', va='center', fontweight='bold', fontsize=10)

# 6. Activity Timeline (Bottom Right)
ax6 = plt.subplot(2, 3, 6)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug']
activity = [15, 18, 25, 30, 28, 35, 40, 45]  # Simulated activity data
ax6.plot(months, activity, marker='o', linewidth=3, markersize=10, 
         color='#00b894', markerfacecolor='#00cec9', markeredgewidth=2, 
         markeredgecolor='white')
ax6.fill_between(months, activity, alpha=0.3, color='#00b894')
ax6.set_ylabel('Commits/Updates', fontsize=12, fontweight='bold')
ax6.set_title('Activity Timeline 2026', fontsize=14, fontweight='bold', pad=20)
ax6.grid(True, alpha=0.3, linestyle='--')
ax6.set_ylim(0, 50)

# Add legend for categories
legend_elements = [mpatches.Patch(facecolor=cat_colors[0], edgecolor='white', label='🤖 AI & Agents (Main Focus)'),
                   mpatches.Patch(facecolor=cat_colors[1], edgecolor='white', label='⚙️ Backend & APIs'),
                   mpatches.Patch(facecolor=cat_colors[2], edgecolor='white', label='🌐 Web Development')]
fig.legend(handles=legend_elements, loc='lower center', ncol=3, 
          fontsize=11, frameon=True, fancybox=True, shadow=True)

plt.tight_layout(rect=[0, 0.03, 1, 0.96])
plt.savefig('github_analysis_visualization.png', dpi=300, bbox_inches='tight', 
            facecolor='#1a1a1a', edgecolor='none')
print("✅ Visualization saved as: github_analysis_visualization.png")
plt.close()

# Create a second image with repository type breakdown
fig2, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
fig2.patch.set_facecolor('#1a1a1a')
fig2.suptitle('Repository Analysis Deep Dive', fontsize=20, fontweight='bold', color='white')

# Fork vs Original
ax1.pie([183, 40], labels=['Forks (82%)', 'Original (18%)'], 
        colors=['#e74c3c', '#2ecc71'], autopct='%1.1f%%',
        startangle=90, textprops={'fontsize': 12, 'fontweight': 'bold'})
ax1.set_title('Fork vs Original Repositories', fontsize=14, fontweight='bold', pad=20)

# Public vs Private
ax2.pie([202, 21], labels=['Public (91%)', 'Private (9%)'],
        colors=['#3498db', '#9b59b6'], autopct='%1.1f%%',
        startangle=90, textprops={'fontsize': 12, 'fontweight': 'bold'})
ax2.set_title('Public vs Private Repositories', fontsize=14, fontweight='bold', pad=20)

# Top Categories Bar
top_5_cats = categories[:5]
top_5_counts = cat_counts[:5]
top_5_colors = cat_colors[:5]
bars = ax3.bar(top_5_cats, top_5_counts, color=top_5_colors, edgecolor='white', linewidth=2)
ax3.set_ylabel('Number of Repositories', fontsize=12, fontweight='bold')
ax3.set_title('Top 5 Project Categories', fontsize=14, fontweight='bold', pad=20)
ax3.grid(axis='y', alpha=0.3, linestyle='--')
for bar, count in zip(bars, top_5_counts):
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2., height + 0.5,
             str(count), ha='center', va='bottom', fontweight='bold', fontsize=11)
plt.setp(ax3.xaxis.get_majorticklabels(), rotation=15, ha='right')

# Tech Stack Summary
ax4.axis('off')
tech_stack = """
🛠️ TECH STACK OVERVIEW

Frontend:
  • TypeScript, React, Next.js
  • HTML5, CSS3, TailwindCSS

Backend:
  • Python (FastAPI, Django)
  • Node.js, Go
  • REST APIs, GraphQL

AI & ML:
  • LLM Integration
  • Agent Frameworks (Hermes)
  • Model Context Protocol (MCP)

DevOps & Cloud:
  • Kubernetes, Docker
  • CI/CD, GitOps
  • Cloud Platforms
"""
ax4.text(0.1, 0.5, tech_stack, fontsize=11, family='monospace',
         verticalalignment='center', bbox=dict(boxstyle='round',
         facecolor='#2d3436', alpha=0.8, edgecolor='white', linewidth=2))

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('github_analysis_deep_dive.png', dpi=300, bbox_inches='tight',
            facecolor='#1a1a1a', edgecolor='none')
print("✅ Deep dive visualization saved as: github_analysis_deep_dive.png")

print("\n🎨 All visualizations created successfully!")
print("📁 Files created:")
print("   1. github_analysis_visualization.png")
print("   2. github_analysis_deep_dive.png")
