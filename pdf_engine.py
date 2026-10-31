
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit


def create_pdf(text):

    buffer = BytesIO()

    pdf = canvas.Canvas(
        buffer,
        pagesize=A4
    )

    width, height = A4

    x = 50
    y = height - 50

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(x, y, "AI Business Plan")

    y -= 35

    pdf.setFont("Helvetica", 10)

    for paragraph in text.split("\n"):

        lines = simpleSplit(
            paragraph,
            "Helvetica",
            10,
            width - 100
        )

        for line in lines:

            if y < 50:

                pdf.showPage()

                y = height - 50

                pdf.setFont("Helvetica", 10)

            pdf.drawString(x, y, line)

            y -= 15

    pdf.save()

    buffer.seek(0)

    return buffer
