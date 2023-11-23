#-*- code: utf-8 -*-

import sys
from fpdf import FPDF

def main():
    shirtify(input("Name: "))

def shirtify(s):
    pdf = FPDF(orientation="P", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", "B", 36)
    pdf.cell(h = 42, text = "CS50 Shirtificate", align = "C", center = True)
    pdf.image("./shirtificate.png", x="C", y=64, w=190, h=190)
    pdf.set_font("helvetica", "B", 24)
    pdf.set_text_color(r=255, g=255, b=255)
    pdf.cell(h=232, text = f"{s} took CS50", center = True)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
