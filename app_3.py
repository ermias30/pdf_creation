from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False,margin=0)
df=pd.read_csv("topics.csv")


for index,row in df.iterrows():
    pdf.add_page()
    # print(row["ermi"])
    pdf.set_font(family="Times",size=12,style="B")
    pdf.cell(w=0,h=12,txt=row["Topic"],align="l",ln=1,border=0)
    pdf.line(10,22,200,22)

    pdf.ln(265)
    pdf.set_text_color(0,26,80)
    pdf.set_font(family="Times",size=10,style="I")
    pdf.cell(w=0,h=8,txt=row["Topic"],align="R")

    for i in range(row["Pages"]-1):
        pdf.add_page()
        pdf.ln(265)
        pdf.set_text_color(0, 26, 80)
        pdf.set_font(family="Times", size=10, style="I")
        pdf.cell(w=0, h=8, txt=row["Topic"], align="r")





# print(type(pdf))

# pdf.add_page()
# pdf.set_font(family="Times", size=12, style="B")
# pdf.cell(w=0, h=12, txt="hello ermias", align="L", ln=1, border=1)
# pdf.cell(w=0, h=12, txt="hello ermi", align="L", ln=1, border=1)
# pdf.add_page()

pdf.output("output.pdf")
