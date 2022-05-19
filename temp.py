import boto3

website_configuration = {
    'IndexDocument'
}


s3 = boto3.client('s3')
result = s3.get_bucket_website(Bucket='iit-group12')
print(result)