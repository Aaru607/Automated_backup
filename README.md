Certainly! Here are some common AWS CLI commands that you might want to save in a GitHub repository for managing AWS resources. You can include these commands in a README file or a script file in your repository.

### AWS CLI Commands

#### **1. List All S3 Buckets**
```bash
aws s3 ls
```

#### **2. Upload a File to S3**
```bash
aws s3 cp local-file.txt s3://your-bucket-name/path/to/destination/
```

#### **3. Download a File from S3**
```bash
aws s3 cp s3://your-bucket-name/path/to/source/local-file.txt .
```

#### **4. List All EC2 Instances**
```bash
aws ec2 describe-instances
```

#### **5. Start an EC2 Instance**
```bash
aws ec2 start-instances --instance-ids i-1234567890abcdef0
```

#### **6. Stop an EC2 Instance**
```bash
aws ec2 stop-instances --instance-ids i-1234567890abcdef0
```

#### **7. Create a New S3 Bucket**
```bash
aws s3api create-bucket --bucket your-new-bucket-name --region your-region
```

#### **8. Delete an S3 Bucket**
```bash
aws s3 rb s3://your-bucket-name --force
```

#### **9. List CloudWatch Alarms**
```bash
aws cloudwatch describe-alarms
```

#### **10. Create a CloudWatch Alarm**
```bash
aws cloudwatch put-metric-alarm --alarm-name "AlarmName" --metric-name "MetricName" --namespace "AWS/Service" --statistic "Average" --period 300 --threshold 1 --comparison-operator "GreaterThanOrEqualToThreshold" --evaluation-periods 1 --alarm-actions arn:aws:sns:your-region:your-account-id:your-sns-topic
```

#### **11. List Lambda Functions**
```bash
aws lambda list-functions
```

#### **12. Invoke a Lambda Function**
```bash
aws lambda invoke --function-name your-function-name output.json
```

#### **13. Create a New Lambda Function**
```bash
aws lambda create-function --function-name your-function-name --runtime python3.8 --role arn:aws:iam::your-account-id:role/your-role --handler lambda_function.lambda_handler --zip-file fileb://function.zip
```

#### **14. Delete a Lambda Function**
```bash
aws lambda delete-function --function-name your-function-name
```

#### **15. Describe IAM Roles**
```bash
aws iam list-roles
```

#### **16. Create an IAM Role**
```bash
aws iam create-role --role-name your-role-name --assume-role-policy-document file://trust-policy.json
```

#### **17. Attach a Policy to an IAM Role**
```bash
aws iam attach-role-policy --role-name your-role-name --policy-arn arn:aws:iam::aws:policy/your-policy
```

Feel free to customize these commands based on your specific needs and environment. You can save them in a file named, for example, `aws-cli-commands.md` or `aws-commands.sh` in your GitHub repository.
