from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))

c = canvas.Canvas("example.pdf", pagesize=letter)
c.setFont("Arial", 14)
c.drawString(50, 750, "ООО «НПО 'ПЕРМНЕФТЕГАЗ', 614064, Пермский край, г.о.Пермский, г.Пермь, ул.Героев Хасана, стр.46Б; ОКВЭД 27.90, info@permneftegaz.ru, тел. (342) 270-10-11")
c.save()