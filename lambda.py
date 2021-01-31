import json
import boto3
import os

def lambda_handler(event, context):
    
    BUCKET_NAME = 'thiagomess'
    KEY = 'teste.pem'
    print('Using LocalStack endpoint %s' % os.environ['LOCALSTACK_HOSTNAME'])


    s3 = boto3.client('s3', region_name='us-east-1', use_ssl=False,
                        aws_access_key_id="", aws_secret_access_key="",
                        endpoint_url='http://%s:4566' % os.environ['LOCALSTACK_HOSTNAME'])

    apigw = boto3.client('apigateway', region_name='us-east-1', use_ssl=False,
                        aws_access_key_id="", aws_secret_access_key="",
                        endpoint_url='http://%s:4566' % os.environ['LOCALSTACK_HOSTNAME'])

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
  
    response_api = apigw.get_domain_name(
        domainName='api.example.com'
    )
    print('--------')
    print(response_api)

    response_update = apigw.update_domain_name(
    domainName='api.example.com',
    patchOperations=[
                        {'op' : 'replace',
    'path' : '/certificateArn',
    'value' : 'arn:aws:acm:us-east-1:012345678910:certificate/34a95aa1-77fa-427c-aa07-3a88bd9f3c0a'}
                        
                    ]
    )


    print('------------------------------------------------')
    print(response_update)
    #  response_api = apigw.get_domain_name(
    #     domainName='api.example.com'
    # )   
    # print(response_api)
    
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