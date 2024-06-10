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
    
    # Process the PDF (example: merging the first two pages)
    input_pdf = PdfFileReader(io.BytesIO(file_content))
    pdf_writer = PdfFileWriter()
    if input_pdf.getNumPages() > 1:
        pdf_writer.addPage(input_pdf.getPage(0))
        pdf_writer.addPage(input_pdf.getPage(1))
        
        output_buffer = io.BytesIO()
        pdf_writer.write(output_buffer)
        output_buffer.seek(0)
        
        merged_key = f"merged/merged.pdf"
        s3_client.put_object(Bucket='YOUR_OUTPUT_BUCKET_NAME', Key=merged_key, Body=output_buffer, ContentType='application/pdf')
    
    return {
        'statusCode': 200,
        'body': json.dumps(f"PDF processed: merged the first two pages."),
        'isBase64Encoded': False,
        'headers': {
            'Content-Type': 'application/json'
        }
    }
