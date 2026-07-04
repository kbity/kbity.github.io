import os
import markdown

template_path = "template.html"
mdd = "./markdown"
htmlfiles = "./docs"

# load template file
with open(template_path, "r", encoding="utf-8") as f:
    template = f.read()

for root, dirs, files in os.walk(mdd):
    for filename in files:
        if not filename.endswith(".md"):
            continue

        md_path = os.path.join(root, filename)
        rel_path = os.path.relpath(md_path, mdd)  # relative to ./markdown
        base_name = os.path.splitext(rel_path)[0] + ".html"
        output_path = os.path.join(htmlfiles, base_name)

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(md_path, "r", encoding="utf-8") as f:
            md_content = f.read()

        html_content = markdown.markdown(md_content, extensions=["fenced_code", "tables"])

        final_html = template.replace("<!-- Wiki Content Here -->", html_content)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(final_html)

        print(f"generated file {output_path}")
