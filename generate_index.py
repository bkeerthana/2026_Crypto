from pathlib import Path

sections = {
    "Lecture Notes": "notes",
    "Lab Exercises": "labs",
    "Assignments": "assignments",
    "Question Bank": "question_bank",
    "Reference Materials": "references"
}

html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>2026 Cryptology Course Materials</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f4f7fb;
            color: #222;
        }

        header {
            background: #1f3c88;
            color: white;
            padding: 30px 20px;
            text-align: center;
        }

        header h1 {
            margin: 0;
            font-size: 32px;
        }

        header p {
            margin-top: 8px;
            font-size: 16px;
        }

        nav {
            background: #162b63;
            padding: 12px;
            text-align: center;
        }

        nav a {
            color: white;
            text-decoration: none;
            margin: 0 12px;
            font-weight: bold;
        }

        main {
            max-width: 1000px;
            margin: 30px auto;
            padding: 0 20px;
        }

        section {
            background: white;
            margin-bottom: 25px;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }

        section h2 {
            margin-top: 0;
            color: #1f3c88;
            border-bottom: 2px solid #e1e7f5;
            padding-bottom: 8px;
        }

        .file-list {
            list-style: none;
            padding: 0;
        }

        .file-list li {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #f8faff;
            margin: 10px 0;
            padding: 12px 15px;
            border-radius: 6px;
            border-left: 4px solid #1f3c88;
        }

        .file-list a {
            background: #1f3c88;
            color: white;
            padding: 7px 12px;
            border-radius: 5px;
            text-decoration: none;
            font-size: 14px;
        }

        .empty {
            color: #777;
            font-style: italic;
        }

        footer {
            text-align: center;
            padding: 20px;
            background: #162b63;
            color: white;
            margin-top: 30px;
        }
    </style>
</head>
<body>

<header>
    <h1>2026 Cryptology Course Materials</h1>
    <p>Lecture notes, lab exercises, assignments, question bank, and references</p>
</header>

<nav>
    <a href="#notes">Lecture Notes</a>
    <a href="#labs">Labs</a>
    <a href="#assignments">Assignments</a>
    <a href="#question_bank">Question Bank</a>
    <a href="#references">References</a>
</nav>

<main>
"""

for title, folder in sections.items():
    html += f'\n<section id="{folder}">\n'
    html += f"    <h2>{title}</h2>\n"
    html += '    <ul class="file-list">\n'

    folder_path = Path(folder)

    if folder_path.exists():
        files = sorted([file for file in folder_path.iterdir() if file.is_file() and file.name != ".gitkeep"])

        if files:
            for file in files:
                display_name = file.stem.replace("_", " ").replace("-", " ").title()
                html += f'        <li><span>{display_name}</span><a href="{file.as_posix()}">View / Download</a></li>\n'
        else:
            html += '        <li class="empty">No files uploaded yet.</li>\n'
    else:
        html += '        <li class="empty">No files uploaded yet.</li>\n'

    html += "    </ul>\n"
    html += "</section>\n"

html += """
</main>

<footer>
    <p>Department Course Repository | 2026</p>
</footer>

</body>
</html>
"""

Path("index.html").write_text(html, encoding="utf-8")
