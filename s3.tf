resource "aws_s3_bucket" "b" {
  bucket = "thiagomess"


  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }

  versioning {
    enabled = true
  }
}