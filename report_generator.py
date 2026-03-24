from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_report(name, age, condition, risk):
    doc = SimpleDocTemplate("report.pdf")
    styles = getSampleStyleSheet()

    content = []
    content.append(Paragraph(f"Patient: {name}", styles["Normal"]))
    content.append(Paragraph(f"Age: {age}", styles["Normal"]))
    content.append(Paragraph(f"Condition: {condition}", styles["Normal"]))
    content.append(Paragraph(f"Risk Score: {risk:.2f}", styles["Normal"]))

    doc.build(content)

    return "report.pdf"