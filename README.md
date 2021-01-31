localstack


Executando um Api gw criado pelo localstack:  http://localhost:4566/restapis/{ID}/{stage}/_user_request_/{path}
exemplo: http://localhost:4566/restapis/7ljnpwofex/prod/_user_request_/a



Outros comandos
aws --endpoint-url=http://localhost:4566 apigateway update-domain-name --domain-name 'api.example.com' --patch-operations "op='replace', path='/tags/teste', value='2'"

aws --endpoint-url=http://localhost:4566 apigateway get-domain-names

aws --endpoint-url=http://localhost:4566 acm request-certificate --domain-name www.example.com --validation-method DNS --idempotency-token 1234 --options CertificateTransparencyLoggingPreference=DISABLED


aws --endpoint-url=http://localhost:4566 s3 cp teste.pem s3://thiagomess/
