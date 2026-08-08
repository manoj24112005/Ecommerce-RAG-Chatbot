import markdown
from pathlib import Path
from xhtml2pdf import pisa

def create_script_and_diagram_pdf(pdf_file_path: str):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset='utf-8'>
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
                font-size: 17pt;
                color: #2874f0;
                border-bottom: 2px solid #2874f0;
                padding-bottom: 4px;
                margin-top: 0;
                margin-bottom: 12px;
                text-align: center;
            }

            h2 {
                font-size: 12pt;
                color: #059669;
                border-bottom: 1px solid #059669;
                padding-bottom: 3px;
                margin-top: 14px;
                margin-bottom: 6px;
            }

            blockquote {
                background-color: #f8fafc;
                border-left: 4px solid #059669;
                padding: 8px 12px;
                margin: 8px 0;
                color: #0f172a;
                font-size: 9.5pt;
                line-height: 1.4;
            }

            .diagram-container {
                margin: 12px 0;
                padding: 10px;
                background-color: #f8fafc;
                border: 1px solid #cbd5e1;
                border-radius: 6px;
            }

            table {
                width: 100%;
                border-collapse: collapse;
                margin: 6px 0;
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
                margin-top: 4px;
                margin-bottom: 6px;
                padding-left: 18px;
            }

            li {
                margin-bottom: 4px;
                font-size: 9.5pt;
            }

            strong {
                color: #0f172a;
            }
        </style>
    </head>
    <body>

        <h1>🎓 E-Cart Viva Presentation Script & Architecture Diagram</h1>

        <h2>🎙️ 1. 30-Second Viva Pitch (What to Say to Examiners)</h2>
        <blockquote>
            <b>"Good morning / afternoon, Respected External Examiners."</b><br/><br/>
            I am presenting <b>E-Cart</b>, an AI-powered E-Commerce platform featuring a <b>Strictly Grounded RAG Shopping Advisor</b>.<br/><br/>
            Unlike standard chatbots that make up fake products or prices, our system uses a <b>3-Stage RAG Pipeline</b>:
            <ol style="margin-top:4px; margin-bottom:4px;">
                <li><b>Retrieval</b>: Searches our real store catalog using 384-dimensional vector embeddings (MiniLM-L6) with Category Intent Filtering.</li>
                <li><b>Augmentation</b>: Prepares real product specifications and prices in Indian Rupees (₹).</li>
                <li><b>Generation</b>: AI generates answers strictly from store data, refusing any off-topic or fake questions.</li>
            </ol>
            It supports 28+ real tech products, a <b>5-Item Gaming Setup Builder</b>, and a <b>Full-Page Product View</b> with verified buyer reviews.
        </blockquote>

        <h2>🏗️ 2. System Architecture Diagram</h2>
        <div class="diagram-container">
            <table>
                <tr>
                    <td style="width:28%; background-color:#0f172a; color:#fff; text-align:center; padding:10px; border-radius:6px;">
                        <b style="color:#f59e0b; font-size:9.5pt;">👤 Step 1: User Query</b><br/><br/>
                        "Camera under 50k" or "Gaming setup"
                    </td>
                    <td style="width:8%; text-align:center; font-size:16pt; color:#2874f0; border:none; background:transparent;">➔</td>
                    <td style="width:28%; background-color:#059669; color:#fff; text-align:center; padding:10px; border-radius:6px;">
                        <b style="font-size:9.5pt;">🔍 Step 2: Vector Retrieval</b><br/><br/>
                        Dense Embeddings (MiniLM-L6)<br/>Category Filter (Cameras)
                    </td>
                    <td style="width:8%; text-align:center; font-size:16pt; color:#2874f0; border:none; background:transparent;">➔</td>
                    <td style="width:28%; background-color:#2874f0; color:#fff; text-align:center; padding:10px; border-radius:6px;">
                        <b style="font-size:9.5pt;">🤖 Step 3: AI Generation</b><br/><br/>
                        Zero-Hallucination Guardrail<br/>Strict Store Prices in ₹
                    </td>
                </tr>
            </table>
        </div>

        <h2>🖥️ 3. Live Demonstration Script (Step-by-Step Walkthrough)</h2>
        <ul>
            <li><b>Step 1 (Store Layout)</b>: <i>"Here is the E-Cart home page with sticky category navigation tabs."</i></li>
            <li><b>Step 2 (Full-Page View)</b>: <i>"Clicking any product opens the Full-Page Detail View with high-res image preview, spec tables, and verified buyer reviews."</i></li>
            <li><b>Step 3 (Gaming Setup Builder)</b>: <i>"Clicking 'Build Gaming Setup' in the chatbot automatically curates a 5-item gaming bundle (PC + OLED Monitor + Mouse + Keyboard + Headset) with 1-click cart buttons."</i></li>
            <li><b>Step 4 (Category Filter Test)</b>: <i>"Asking 'camera under 50 k' returns real cameras like GoPro HERO 12 & Sony ZV-E10, and zero smartphones."</i></li>
            <li><b>Step 5 (Anti-Hallucination Test)</b>: <i>"Asking an off-topic question like 'who won the world cup?' triggers our zero-hallucination guardrail refusal."</i></li>
        </ul>

    </body>
    </html>
    """

    with open(pdf_file_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(html_content, dest=pdf_file)

    if pisa_status.err:
        print(f"Error generating PDF: {pisa_status.err}")
    else:
        print(f"Standalone PDF generated successfully at: {pdf_file_path}")

if __name__ == "__main__":
    artifact_dir = Path("C:/Users/manoj/.gemini/antigravity/brain/7c39931c-aca7-4c0a-8aeb-79dfa263f4de")
    pdf_file = artifact_dir / "Viva_Script_and_Architecture_Diagram.pdf"
    create_script_and_diagram_pdf(str(pdf_file))
