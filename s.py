# import random
# from reportlab.lib.pagesizes import letter
# from reportlab.lib import colors
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
# from reportlab.lib.styles import getSampleStyleSheet

# # Define the data for your report
# data = [
#     ['First Name', 'badar'],
#     ['Last Name', 'doja'],
#     ['Age', '23'],
#     ['City', 'islamabad'],
#     ['Country', 'pakistan'],
#     ['Education', 'undergraguate'],
#     ['Email', 'badar@gmail.com'],
#     ['Phone', '1234567890'],
#     ['Sex', 'male'],
#     ['Postal Code', '12345'],
#     ['Doctor ID', '123'],
#     ['Income', '100'],
#     ['High Blood Pressure', random.choice(['Yes', 'No'])],
#     ['High Cholesterol', random.choice(['Yes', 'No'])],
#     ['Cholesterol Check', random.choice(['Yes', 'No'])],
#     ['BMI', str(random.uniform(18.5, 30.0))],
#     ['Smoker', random.choice(['Yes', 'No'])],
#     ['Stroke', random.choice(['Yes', 'No'])],
#     ['Heart Disease or Attack', random.choice(['Yes', 'No'])],
#     ['Physical Activity', random.choice(['Active', 'Inactive'])],
#     ['Fruits Consumption', str(random.randint(0, 5)) + ' servings/day'],
#     ['Vegetables Consumption', str(random.randint(0, 5)) + ' servings/day'],
#     ['Heavy Alcohol Consumption', random.choice(['Yes', 'No'])],
#     ['Any Healthcare', random.choice(['Yes', 'No'])],
#     ['No Doctor because of Cost', random.choice(['Yes', 'No'])],
#     ['General Health', random.randint(1, 5)],
#     ['Mental Health', random.randint(1, 5)],
#     ['Physical Health', random.randint(1, 5)],
#     ['Difficulty in Walking', random.choice(['Yes', 'No'])]
# ]

# # Create a PDF report
# def generate_report(filename, data):
#     doc = SimpleDocTemplate(filename, pagesize=letter)

#     # Create a list of elements to include in the PDF
#     elements = []

#     # Define styles for the report
#     styles = getSampleStyleSheet()
#     title_style = styles['Heading1']
#     table_style = TableStyle([
#     ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header background color
#     ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
#     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Alignment of table cells
#     ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header font
#     ('FONTSIZE', (0, 0), (-1, 0), 12),  # Header font size
#     ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Header bottom padding
#     ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Table body background color
#     ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),  # Table body text color
#     ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),  # Table body font
#     ('FONTSIZE', (0, 1), (-1, -1), 10),  # Table body font size
#     ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Vertical alignment of table cells
#     ('LINEBEFORE', (0, 0), (-1, -1), 1, colors.black),  # Line color before table cells
#     ('LINEAFTER', (0, 0), (-1, -1), 1, colors.black),  # Line color after table cells
#     ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Grid lines color
#     ])

#     # Create a title for the report
#     title = Paragraph('Medical Report', title_style)
#     elements.append(title)
#     elements.append(Paragraph('<br/><br/>', styles['Normal']))

#     # Create a table to display the data
#     table = Table(data)
#     table.setStyle(table_style)
#     elements.append(table)

#     # Build the PDF document
#     doc.build(elements)

# # Generate the report
# generate_report('medical_report.pdf', data)



from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QColor, QFont, QPixmap
from PySide6.QtWidgets import QApplication, QSplashScreen, QLabel

# Create the application instance
app = QApplication([])

# Create the splash screen widget
splash = QSplashScreen()

# Set the splash screen properties
splash.setPixmap(QPixmap("C:/Users/saada/Desktop/national-cancer-institute-NFvdKIhxYlU-unsplash (1).jpg"))  # Set the splash screen image
splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)  # Set window flags
splash.setFont(QFont("Arial", 12, QFont.Bold))  # Set font properties
splash.showMessage("Loading...", Qt.AlignCenter, QColor(Qt.white))  # Show a loading message

# Show the splash screen
splash.show()

# Simulate loading time with a QTimer (replace this with your actual loading process)
loading_timer = QTimer()
loading_timer.singleShot(5000, app.quit)  # Simulate 5 seconds loading time, then quit the application

# Start the application event loop
app.exec()
