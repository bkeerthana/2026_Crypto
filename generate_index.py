from pathlib import Path

sections = {
    "Lecture Notes": "notes",
    "Lab Exercises": "labs",
    "Assignments": "assignments",
    "Question Bank": "question_bank",
    "Reference Materials": "references"
}

html = """<!DOCTYPE html>
<html>
<head>
    <title>2026 Cryptology Course Materials</title>
</head>
<body>
    <h1>2026 Cryptology Course Materials</h1>
    <p>Course materials, lab exercises, assignments, and references.</p>
"""

for title, folder in sections.items():
    html += f"\n    <h2>{title}</h2>\n    <ul>\n"
    folder_path = Path(folder)

    if folder_path.exists():
        files = sorted(folder_path.iterdir())
        if files:
            for file in files:
                if file.is_file():
                    display_name = file.stem.replace("_", " ").replace("-", " ").title()
                    html += f'        <li><a href="{file.as_posix()}">{display_name}</a></li>\n'
        else:
            html += "        <li>No files uploaded yet.</li>\n"
    else:
        html += "        <li>No files uploaded yet.</li>\n"

    html += "    </ul>\n"

html += """
</body>
</html>
"""

Path("index.html").write_text(html, encoding="utf-8")