import json
import boto3

def lambda_handler(event, context):
    
    BUCKET_NAME = 'thiagomess'
    KEY = 'teste.pem'
    s3 = boto3.client('s3')
    body = json.loads(event['body'])
    response = None
    
    
    
    if body['csr'].startswith('-----BEGIN CERTIFICATE-----'):
        csr = body["csr"]
        print(csr)
    else:
        raise Exception('not certificate valid')

    try:
        response_obj = s3.get_object(Bucket=BUCKET_NAME, Key=KEY)
        conteudo = response_obj['Body'].read().decode('utf-8')
        append = "{}\n{}".format(conteudo, csr)
        print(append)
        response = s3.put_object(Bucket=BUCKET_NAME, Key=KEY, Body=append)
    except Exception as e:
        response = s3.put_object(Bucket=BUCKET_NAME, Key=KEY, Body=csr)
    
    print(response['ETag'])
    
    return response
    
    
    
    
#     client = boto3.client('acm')

# def lambda_handler(event, context):
#     certificate=open('sample.vpn.crt', 'rb').read()
#     privatekey=open('sample.vpn.key', 'rb').read()
#     chain=open('ca.crt', 'rb').read()

#     response = client.import_certificate(
#         Certificate=certificate,
#         PrivateKey=privatekey,
#         CertificateChain=chain
#     )
#https://stackoverflow.com/questions/62975611/import-certificate-in-aws-acm-using-python
    
#     return {
#     'statusCode': 200,
#     'body': 'concluido'
#   }