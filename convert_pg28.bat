@echo off
cd /d "D:\Samera portfolio"
del "static\images\portfolio_pg28.jpg"
python -c "import fitz; doc = fitz.open('static/images/new_PORTFOLIO PG28.pdf'); page = doc[0]; pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0)); pix.save('static/images/portfolio_pg28.jpg'); doc.close(); print('Done!')"
pause
