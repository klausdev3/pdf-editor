# pdf-editor on aws infrastructure

This transformer can split and merge PDFs using AWS Lambda and S3, leveraging the PyPDF2 library to handle PDF operations.

Here's how you can do it using an HTML form, JavaScript for handling the file upload, and an AWS API Gateway to trigger the Lambda function for the processing.

Step 1: Set Up API Gateway to Trigger Lambda
Create Lambda Functions

You need two Lambda functions: one for splitting PDFs and one for merging PDFs.
Use the Lambda function code provided earlier and modify it to handle either splitting or merging based on the function's purpose.
Create API Gateway:

Go to the AWS API Gateway console and create a new REST API.
Create two endpoints: one for splitting and one for merging.
Integrate each endpoint with the corresponding Lambda function.

Step 2: HTML and JavaScript for File Upload

Step 3: Configure API Gateway to Accept File Uploads
Create an API Endpoint:

In the API Gateway, create two endpoints: /split and /merge.
For each endpoint, configure a POST method.
Integration with Lambda:

Integrate the POST methods with the corresponding Lambda functions.
Set Up Method Request and Integration Request:

In the Method Request, ensure that the Content-Type is set to multipart/form-data.
In the Integration Request, use a mapping template to pass the file data to the Lambda function.

Step 4: Modify Lambda Functions to Handle File Uploads
Modify your Lambda functions to handle the file data from the request. Below is an example of how to handle file uploads in the Lambda function.

Step 5: Deploy and Test
Deploy the API Gateway and Lambda functions.
Open index.html in a web browser, upload a PDF, and choose an action (split or merge).
Verify that the Lambda function processes the PDF and uploads the result to the specified S3 bucket.
This setup will allow you to upload PDFs via a simple HTML interface and process them with AWS Lambda.
