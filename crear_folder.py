import boto3

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']
    nombre_folder = event['body']['folder']
    
    # Proceso    
    s3 = boto3.client('s3')
    
    s3.put_object(Bucket=nombre_bucket, Key=(nombre_folder+'/'))

    response = s3.list_objects(Bucket=nombre_bucket)
    lista = []
    for obj in response['Contents']:
        lista.append(obj['Key'])

    return {
        'statusCode': 200,
        'bucket': nombre_bucket,
        'lista_objetos': lista
    }
