import json
import boto3
import io
from PyPDF2 import PdfFileReader, PdfFileWriter

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Get the file content from the event
    body = event['body']
    is_base64_encoded = event.get('isBase64Encoded', False)
    
    # Decode the body if it's base64-encoded
    file_content = base64.b64decode(body) if is_base64_encoded else body.encode('utf-8')
    
    # Process the PDF (example: splitting)
    input_pdf = PdfFileReader(io.BytesIO(file_content))
    for page_num in range(input_pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(input_pdf.getPage(page_num))
        
        output_buffer = io.BytesIO()
        pdf_writer.write(output_buffer)
        output_buffer.seek(0)
        
        split_key = f"split/page-{page_num + 1}.pdf"
        s3_client.put_object(Bucket='YOUR_OUTPUT_BUCKET_NAME', Key=split_key, Body=output_buffer, ContentType='application/pdf')
    
    return {
        'statusCode': 200,
        'body': json.dumps(f"PDF processed: split into {input_pdf.getNumPages()} pages."),
        'isBase64Encoded': False,
        'headers': {
            'Content-Type': 'application/json'
        }
    }
