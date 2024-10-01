from fpdf import FPDF # type: ignore

class PDF(FPDF):
    def __init__(self):
        super().__init__()

    def header_pdf(self, title):
        # Title
        self.set_font("Arial", "", 40)
        self.cell(197, 60, f"{title}", align="C")
        self.ln(30)

    def line_1(self, text):
        self.set_font("Helvetica", "B", 24)
        self.set_text_color(0,0,0)
        self.cell(197 / number , 50, f"{text}", align="C")

    def break_line(self, line):
        self.ln(line)

        
number = 5

pdf = PDF()
pdf.add_page()

pdf.header_pdf("+++ To DO List +++")

for i in range(10):
    for j in range(number):
        pdf.line_1(f"Item {j + 1}")
    pdf.break_line(8)

pdf.break_line(5)

pdf.output("outputs/test.pdf")

print("PDF created successfully")
