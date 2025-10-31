aws sts assume-role \
  --role-arn arn:aws:iam::ACCOUNT_ID:role/ECS-Dev-Role \
  --role-session-name boto3-local-session \
  --duration-seconds 3600