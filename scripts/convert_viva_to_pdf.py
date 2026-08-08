import markdown
from pathlib import Path
from xhtml2pdf import pisa

def convert_md_to_pdf(md_file_path: str, pdf_file_path: str):
    with open(md_file_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(md_text, extensions=['tables', 'fenced_code'])

    # CSS Styling for PDF & Visual Architecture Diagram
    custom_css = """
    <style>
        @page {
            size: letter;
            margin: 1.2cm;
        }

        body {
            font-family: 'Helvetica', 'Arial', sans-serif;
            font-size: 10pt;
            line-height: 1.45;
            color: #1e293b;
        }

        h1 {
            font-size: 18pt;
            color: #2874f0;
            border-bottom: 2px solid #2874f0;
            padding-bottom: 4px;
            margin-top: 0;
            margin-bottom: 12px;
        }

        h2 {
            font-size: 13pt;
            color: #059669;
            border-bottom: 1px solid #059669;
            padding-bottom: 3px;
            margin-top: 16px;
            margin-bottom: 8px;
        }

        h3 {
            font-size: 11pt;
            color: #2874f0;
            margin-top: 10px;
            margin-bottom: 4px;
        }

        p {
            margin-top: 3px;
            margin-bottom: 6px;
        }

        blockquote {
            background-color: #f8fafc;
            border-left: 4px solid #059669;
            padding: 8px 12px;
            margin: 8px 0;
            color: #1e293b;
            font-size: 10pt;
        }

        code {
            font-family: 'Courier', monospace;
            background-color: #f1f5f9;
            color: #2874f0;
            padding: 2px 4px;
            font-size: 9pt;
        }

        /* VISUAL ARCHITECTURE DIAGRAM BOXES */
        .diagram-container {
            margin: 12px 0;
            padding: 10px;
            background-color: #f8fafc;
            border: 1px solid #cbd5e1;
            border-radius: 6px;
            text-align: center;
        }

        .diagram-box {
            display: inline-block;
            width: 30%;
            padding: 10px;
            margin: 4px;
            background-color: #0f172a;
            color: #ffffff;
            border-radius: 6px;
            vertical-align: top;
            font-size: 8.5pt;
        }

        .diagram-box.green {
            background-color: #059669;
        }

        .diagram-box.blue {
            background-color: #2874f0;
        }

        .diagram-box.dark {
            background-color: #090d16;
            border: 1px solid #f59e0b;
        }

        .arrow {
            font-size: 14pt;
            color: #2874f0;
            font-weight: bold;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 10px 0;
        }

        th {
            background-color: #059669;
            color: #ffffff;
            font-weight: bold;
            text-align: left;
            padding: 6px 8px;
            font-size: 9pt;
        }

        td {
            border: 1px solid #cbd5e1;
            padding: 6px 8px;
            font-size: 8.5pt;
            background-color: #ffffff;
        }

        tr:nth-child(even) td {
            background-color: #f8fafc;
        }

        ul, ol {
            margin-top: 3px;
            margin-bottom: 6px;
            padding-left: 18px;
        }

        li {
            margin-bottom: 3px;
        }

        strong {
            color: #0f172a;
        }
    </style>
    """

    # Inject HTML Visual Diagram into converted HTML
    visual_diagram_html = """
    <div class="diagram-container">
        <table>
            <tr>
                <td style="width:28%; background-color:#0f172a; color:#fff; text-align:center; padding:10px; border-radius:6px;">
                    <b style="color:#f59e0b; font-size:10pt;">👤 Step 1: User Query</b><br/><br/>
                    "Camera under 50k" or "Gaming setup"
                </td>
                <td style="width:8%; text-align:center; font-size:16pt; color:#2874f0; border:none; background:transparent;">➔</td>
                <td style="width:28%; background-color:#059669; color:#fff; text-align:center; padding:10px; border-radius:6px;">
                    <b style="font-size:10pt;">🔍 Step 2: Vector Retrieval</b><br/><br/>
                    Dense Embeddings (MiniLM-L6)<br/>Category Filter (Cameras)
                </td>
                <td style="width:8%; text-align:center; font-size:16pt; color:#2874f0; border:none; background:transparent;">➔</td>
                <td style="width:28%; background-color:#2874f0; color:#fff; text-align:center; padding:10px; border-radius:6px;">
                    <b style="font-size:10pt;">🤖 Step 3: AI Generation</b><br/><br/>
                    Zero-Hallucination Guardrail<br/>Strict Store Prices in ₹
                </td>
            </tr>
        </table>
    </div>
    """

    # Replace ASCII pre block with visual HTML diagram
    if "<pre><code>" in html_content:
        import re
        html_content = re.sub(r'<pre><code>\+------------[\s\S]*?</code></pre>', visual_diagram_html, html_content)

    full_html = f"<!DOCTYPE html><html><head><meta charset='utf-8'>{custom_css}</head><body>{html_content}</body></html>"

    with open(pdf_file_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(full_html, dest=pdf_file)

    if pisa_status.err:
        print(f"Error occurred while generating PDF: {pisa_status.err}")
    else:
        print(f"PDF generated successfully at: {pdf_file_path}")

if __name__ == "__main__":
    artifact_dir = Path("C:/Users/manoj/.gemini/antigravity/brain/7c39931c-aca7-4c0a-8aeb-79dfa263f4de")
    md_file = artifact_dir / "viva_script_and_project_defense.md"
    pdf_file = artifact_dir / "Viva_Voce_Script_and_Project_Defense.pdf"
    
    convert_md_to_pdf(str(md_file), str(pdf_file))
