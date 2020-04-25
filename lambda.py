import boto3, json

HOSTED_ZONE_ID = '<YOUR-DOMAIN-HOST-NMAE-ID>'

def lambda_handler(event, context):
    route53 = boto3.client('route53')
    ip =  event["ip"]
    password = event["password"]
    if password != "<YOUR-PASSWORD>":
        return {
            'statusCode': 404,
            'body': ip
        }
    dns_changes = {
        'Changes': [
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': "<YOUR-DOMAIN-VHOST>",
                    'Type': 'A',
                    'ResourceRecords': [
                        {
                            'Value': ip
                        }
                    ],
                    'TTL': 300
                }
            }
        ]
    }

    response = route53.change_resource_record_sets(
        HostedZoneId=HOSTED_ZONE_ID,
        ChangeBatch=dns_changes
    )

    return {
            'statusCode': 201,
            'body': ip
        }
