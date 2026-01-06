import json
import boto3
import tempfile
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

# AWS clients (already available in Lambda)
s3 = boto3.client('s3')
ses = boto3.client('ses')

SENDER_EMAIL = "waleedshahab12@gmail.com"
RECIPIENT_EMAIL = "waleedshahab12@gmail.com"


def lambda_handler(event, context):
    # 1. Get S3 bucket and file name
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    # 2. Read JSON file from S3
    response = s3.get_object(Bucket=bucket_name, Key=object_key)
    json_content = response['Body'].read()
    data = json.loads(json_content)

    # 3. Create PDF in temporary directory
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        pdf_path = temp_pdf.name

    pdf = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter

    y_position = height - 50
    pdf.setFont("Helvetica", 12)

    for key, value in data.items():
        pdf.drawString(50, y_position, f"{key}: {value}")
        y_position -= 20

    pdf.save()

    # 4. Create email with PDF attachment
    message = MIMEMultipart()
    message['Subject'] = 'Automated PDF Generated'
    message['From'] = SENDER_EMAIL
    message['To'] = RECIPIENT_EMAIL

    body = MIMEText(
        "Hello,\n\nYour PDF has been generated automatically.\n\nRegards,\nAWS Lambda",
        "plain"
    )
    message.attach(body)

    with open(pdf_path, 'rb') as f:
        attachment = MIMEApplication(f.read())
        attachment.add_header(
            'Content-Disposition',
            'attachment',
            filename='generated_document.pdf'
        )
        message.attach(attachment)

    # 5. Send email via SES
    ses.send_raw_email(
        Source=SENDER_EMAIL,
        Destinations=[RECIPIENT_EMAIL],
        RawMessage={'Data': message.as_string()}
    )

    return {
        "statusCode": 200,
        "body": "PDF generated and emailed successfully"
    }
