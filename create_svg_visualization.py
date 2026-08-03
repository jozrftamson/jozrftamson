#!/usr/bin/env python3
"""
GitHub Account SVG Visualization Generator
Creates colorful SVG charts without external dependencies
"""

def create_language_chart():
    """Create SVG bar chart for programming languages"""
    languages = [
        ('TypeScript', 70, '#3178c6'),
        ('Python', 45, '#3776ab'),
        ('JavaScript', 23, '#f7df1e'),
        ('Go', 22, '#00add8'),
        ('Jupyter Notebook', 8, '#f37726'),
        ('Rust', 5, '#dea584'),
        ('HTML', 5, '#e34c26'),
        ('Java', 4, '#b07219'),
        ('C#', 4, '#178600'),
        ('PHP', 3, '#4f5d95')
    ]
    
    width = 800
    height = 400
    bar_height = 30
    margin = 50
    max_value = 70
    
    svg = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <style>
            .title {{ font: bold 20px sans-serif; fill: #ffffff; }}
            .label {{ font: 12px sans-serif; fill: #ffffff; }}
            .value {{ font: bold 12px sans-serif; fill: #ffffff; }}
        </style>
    </defs>
    <rect width="{width}" height="{height}" fill="#0d1117"/>
    <text x="{width/2}" y="30" class="title" text-anchor="middle">Top 10 Programming Languages</text>
'''
    
    for i, (lang, count, color) in enumerate(languages):
        y = margin + i * (bar_height + 5)
        bar_width = (count / max_value) * (width - 2 * margin - 100)
        
        svg += f'''    <text x="10" y="{y + 20}" class="label">{lang}</text>
    <rect x="200" y="{y}" width="{bar_width}" height="{bar_height}" fill="{color}" rx="5"/>
    <text x="{200 + bar_width + 10}" y="{y + 20}" class="value">{count}</text>
'''
    
    svg += '</svg>'
    return svg

def create_category_chart():
    """Create SVG pie chart for project categories"""
    categories = [
        ('AI & Agents', 31, '#ff6b6b'),
        ('Backend & APIs', 13, '#4ecdc4'),
        ('Web Dev', 11, '#45b7d1'),
        ('Gaming & AR/VR', 9, '#96ceb4'),
        ('Design & UI/UX', 9, '#ffeaa7'),
        ('Kubernetes', 6, '#326ce5'),
        ('Other', 144, '#636e72')
    ]
    
    width = 600
    height = 400
    cx = width / 2
    cy = height / 2
    radius = 120
    
    total = sum(count for _, count, _ in categories)
    
    svg = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <style>
            .title {{ font: bold 20px sans-serif; fill: #ffffff; }}
            .legend {{ font: 12px sans-serif; fill: #ffffff; }}
        </style>
    </defs>
    <rect width="{width}" height="{height}" fill="#0d1117"/>
    <text x="{width/2}" y="30" class="title" text-anchor="middle">Project Categories</text>
'''
    
    start_angle = 0
    for i, (cat, count, color) in enumerate(categories):
        angle = (count / total) * 360
        end_angle = start_angle + angle
        
        # Calculate arc path
        start_rad = start_angle * 3.14159 / 180
        end_rad = end_angle * 3.14159 / 180
        
        x1 = cx + radius * np.cos(start_rad)
        y1 = cy + radius * np.sin(start_rad)
        x2 = cx + radius * np.cos(end_rad)
        y2 = cy + radius * np.sin(end_rad)
        
        large_arc = 1 if angle > 180 else 0
        
        svg += f'''    <path d="M {cx} {cy} L {x1} {y1} A {radius} {radius} 0 {large_arc} 1 {x2} {y2} Z" fill="{color}"/>
'''
        
        # Legend
        legend_y = 80 + i * 25
        svg += f'''    <rect x="20" y="{legend_y}" width="15" height="15" fill="{color}"/>
    <text x="40" y="{legend_y + 12}" class="legend">{cat}: {count} ({count/total*100:.1f}%)</text>
'''
        
        start_angle = end_angle
    
    svg += '</svg>'
    return svg

def create_stats_card():
    """Create SVG stats card"""
    width = 400
    height = 500
    
    svg = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <style>
            .title {{ font: bold 24px sans-serif; fill: #ffffff; }}
            .stat-label {{ font: bold 14px sans-serif; fill: #58a6ff; }}
            .stat-value {{ font: bold 20px sans-serif; fill: #ffffff; }}
            .emoji {{ font: 20px sans-serif; }}
        </style>
    </defs>
    <rect width="{width}" height="{height}" fill="#0d1117" rx="10"/>
    <rect width="{width}" height="{height}" fill="none" stroke="#30363d" stroke-width="2" rx="10"/>
    
    <text x="{width/2}" y="40" class="title" text-anchor="middle">📊 Repository Stats</text>
    
    <text x="30" y="90" class="stat-label">Total Repositories</text>
    <text x="30" y="120" class="stat-value">223</text>
    
    <text x="30" y="160" class="stat-label">🔱 Forks</text>
    <text x="30" y="190" class="stat-value">183 (82%)</text>
    
    <text x="30" y="230" class="stat-label">💎 Original</text>
    <text x="30" y="260" class="stat-value">40 (18%)</text>
    
    <text x="30" y="300" class="stat-label">🔒 Private</text>
    <text x="30" y="330" class="stat-value">21 (9%)</text>
    
    <text x="30" y="370" class="stat-label">🌍 Public</text>
    <text x="30" y="400" class="stat-value">202 (91%)</text>
    
    <text x="30" y="440" class="stat-label">⭐ With Stars</text>
    <text x="30" y="470" class="stat-value">10</text>
</svg>'''
    return svg

def create_skill_matrix():
    """Create SVG skill matrix"""
    skills = [
        ('TypeScript', 100, '#2ecc71'),
        ('Python', 80, '#2ecc71'),
        ('JavaScript', 75, '#f39c12'),
        ('Go', 70, '#f39c12'),
        ('React', 80, '#2ecc71'),
        ('Kubernetes', 60, '#3498db'),
        ('AI/ML', 75, '#f39c12'),
        ('DevOps', 65, '#3498db')
    ]
    
    width = 600
    height = 400
    bar_height = 35
    margin = 50
    
    svg = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <style>
            .title {{ font: bold 20px sans-serif; fill: #ffffff; }}
            .label {{ font: 14px sans-serif; fill: #ffffff; }}
            .value {{ font: bold 12px sans-serif; fill: #ffffff; }}
        </style>
    </defs>
    <rect width="{width}" height="{height}" fill="#0d1117"/>
    <text x="{width/2}" y="30" class="title" text-anchor="middle">🎯 Skill Matrix</text>
'''
    
    for i, (skill, level, color) in enumerate(skills):
        y = margin + i * (bar_height + 5)
        bar_width = (level / 100) * (width - 2 * margin - 150)
        
        svg += f'''    <text x="10" y="{y + 25}" class="label">{skill}</text>
    <rect x="180" y="{y}" width="{bar_width}" height="{bar_height}" fill="{color}" rx="5"/>
    <text x="{180 + bar_width + 10}" y="{y + 25}" class="value">{level}%</text>
'''
    
    svg += '</svg>'
    return svg

# Simple numpy replacement for cos/sin
import math
class np:
    @staticmethod
    def cos(x):
        return math.cos(x)
    @staticmethod
    def sin(x):
        return math.sin(x)

# Generate all SVG files
print("🎨 Creating SVG visualizations...")

with open('languages_chart.svg', 'w') as f:
    f.write(create_language_chart())
print("✅ Created: languages_chart.svg")

with open('categories_chart.svg', 'w') as f:
    f.write(create_category_chart())
print("✅ Created: categories_chart.svg")

with open('stats_card.svg', 'w') as f:
    f.write(create_stats_card())
print("✅ Created: stats_card.svg")

with open('skill_matrix.svg', 'w') as f:
    f.write(create_skill_matrix())
print("✅ Created: skill_matrix.svg")

print("\n🎉 All SVG visualizations created successfully!")
print("📁 Files created:")
print("   1. languages_chart.svg")
print("   2. categories_chart.svg")
print("   3. stats_card.svg")
print("   4. skill_matrix.svg")
