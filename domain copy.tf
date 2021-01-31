resource "aws_api_gateway_domain_name" "example" {
  domain_name              = "api.example.com"
  regional_certificate_arn = "arn:aws:acm:us-east-1:000000000000:certificate/41914748-1229-45ce-b20e-6a176cf1cc21"
  
  endpoint_configuration {
    types = ["REGIONAL"]
  }

  mutual_tls_authentication {
    truststore_uri = "s3://thiagomess/teste.pem"
  }

  security_policy = "TLS_1_2"

  tags ={
      teste = 1
  }
  
}


# # # resource "aws_api_gateway_base_path_mapping" "test" {
# # #   api_id      = aws_api_gateway_rest_api.test.id
# # #   stage_name  = aws_api_gateway_deployment.example.stage_name
# # #   domain_name = aws_api_gateway_domain_name.example.domain_name
# # # }


# # # resource "aws_api_gateway_deployment" "example" {
# # #   # See aws_api_gateway_rest_api docs for how to create this
# # #   rest_api_id = aws_api_gateway_rest_api.test.id
# # #   stage_name  = "prod"
# # # }