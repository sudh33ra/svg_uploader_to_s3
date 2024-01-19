from flask import Flask, request, jsonify
import boto3
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_svg_to_s3():
    try:
        svg_file_name = request.form['svg_file_name']
        svg_file_content = request.form['svg_file_content']
        s3_bucket_name = request.form['s3_bucket_name']

        s3 = boto3.client('s3')

        s3.put_object(
            Body=svg_file_content,
            Bucket=s3_bucket_name,
            Key=svg_file_name,
            ACL='public-read',
            ContentType='image/svg+xml'
        )

        return jsonify({"message": f"Successfully uploaded {svg_file_name} to {s3_bucket_name} with public read access and metadata."})
    except Exception as e:
        return jsonify({"error": f"Error uploading file: {e}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

