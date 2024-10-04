from fpdf import FPDF # type: ignore
import csv

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
        self.cell(197 / 3 , 50, f"{text}", align="C")

    def break_line(self, line):
        self.ln(line)

# CSV File
csv_file = "data/to_do_list.csv"
with open(csv_file, encoding="utf8") as list_file:
    data = list(csv.reader(list_file, delimiter=","))

# Create pdf
pdf = PDF()
pdf.add_page()

# Table
with pdf.table(data) as table:
    for data_row in data:
        row = table.row()
        for dataum in data_row:
            row.cell(dataum)

# Title
pdf.header_pdf("+++ To DO List +++")

# Write lines
for i in range(10):
    for j in range(number):
        pdf.line_1(f"Item {j + 1}")
    pdf.break_line(8)

pdf.break_line(5)

# Save in the folder
pdf.output("outputs/test.pdf")

print("PDF created successfully")
