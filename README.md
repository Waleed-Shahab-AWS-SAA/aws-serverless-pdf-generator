# 🧾 Automated PDF Generation Pipeline (AWS Serverless)

This project demonstrates a **serverless, event-driven architecture** on AWS that automatically converts uploaded JSON files into PDF documents and emails them to users.

It simulates real-world business use cases such as **invoice generation, certificates, and reports**, using fully managed AWS services.

---

## 🏗️ Architecture Overview

When a JSON file is uploaded to Amazon S3, an AWS Lambda function is triggered.  
The Lambda function reads the JSON file, generates a PDF using ReportLab, and sends the PDF as an email attachment using Amazon SES.

### Architecture Flow

User Uploads JSON
↓
Amazon S3 (Input Bucket)
↓ (PUT Event)
AWS Lambda (Python 3.10)
↓
PDF Generated (ReportLab Layer)
↓
Amazon SES (Email with Attachment)

⚙️ Lambda Function Responsibilities

Read JSON object from S3

Dynamically generate a PDF document

Format data line-by-line into the PDF

Send email using Amazon SES with PDF attachment

Log execution details to CloudWatch

🧩 Challenges Solved

Packaging native Python dependencies using Lambda Layers

Matching Lambda runtime (Python 3.10) with dependency binaries

Debugging CloudWatch logs and S3 trigger issues

Implementing MIME-based email attachments in SES

Handling event-driven execution flow

🚀 Future Enhancements

Store generated PDFs in an output S3 bucket

Add HTML-based PDF templates for professional formatting

Integrate API Gateway for direct uploads

Track documents using DynamoDB

Remove SES sandbox for production usage

📌 Learning Outcomes

This project helped build hands-on experience with:

Serverless architecture design

AWS event-driven services

Lambda layers and dependency management

CloudWatch debugging and monitoring

Real-world AWS automation workflows

👤 Author

Waleed Shahab
Aspiring Cloud Engineer
