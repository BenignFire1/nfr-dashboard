import re

# Read the processed JS data
with open("processed_data.js", "r") as f:
    js_data = f.read()

# Read the HTML file
html_path = "NFR_Division_Dashboard (1).html"
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Define the start and end markers
start_marker = "// ─── DATA ────────────────────────────────────────────────────────────────────"
end_marker = "// ─── STATE ───────────────────────────────────────────────────────────────────"

# Find markers manually to avoid regex escape issues
start_idx = html_content.find(start_marker)
end_idx = html_content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_html = html_content[:start_idx + len(start_marker)] + "\n" + js_data + "\n    " + html_content[end_idx:]
    
    # Write the updated HTML
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print("HTML file updated successfully.")
else:
    print(f"Markers not found: Start={start_idx}, End={end_idx}")
   