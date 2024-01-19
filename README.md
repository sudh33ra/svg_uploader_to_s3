# SVG Uploader to S3

Hey there! Welcome to the SVG Uploader to S3. This simple Flask app lets you upload SVG files to an Amazon S3 bucket effortlessly.

## Prerequisites

Before you get started, make sure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Python 3.8](https://www.python.org/downloads/release/python-380/) (if you prefer running without Docker)

## Getting Started

1. **Clone this repository to your local machine:**

    ```bash
    git clone https://github.com/your-username/svg-uploader-to-s3.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd svg-uploader-to-s3
    ```

3. **Build the Docker image:**

    ```bash
    docker build -t svg-uploader .
    ```

4. **Run the Docker container:**

    ```bash
    docker run -p 5001:5001 svg-uploader
    ```

   If you prefer running without Docker, ensure you have the required packages installed:

   ```bash
   pip install boto3 Flask
   ```
5. Then, run the Flask app:

   ```bash
   python app.py
   ```
The app will be accessible at http://localhost:5001. Feel free to change the port in app.py if needed.

### Usage
Use a tool like Postman or cURL to make a POST request to http://localhost:5001/upload.

Include the following form fields:

`svg_file_name`: The name you want for your SVG file in S3.
`svg_file_content`: The content of your SVG file.
`s3_bucket_name`: The name of your S3 bucket.
Receive a JSON response indicating the success or failure of the upload.

### Docker Configuration
If you need to set up your AWS credentials, mount your AWS credentials and config directory using:

   ```bash
   docker run -v /path/to/your/aws:/root/.aws -p 5001:5001 svg-uploader
   ```
Make sure your AWS credentials file (/path/to/your/aws/credentials) has the necessary permissions.

Feel free to reach out if you have any questions or run into issues. Happy uploading! 🚀
