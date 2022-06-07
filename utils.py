from datetime import datetime
from minio import Minio

client = Minio('192.168.0.204:9000', access_key="admin",
               secret_key="P@ssw0rd", secure=False)


def creat_bucket():
    now = datetime.now()
    data_now = now.strftime("%Y%m%d")
    found = client.bucket_exists(data_now)
    if not found:
        client.make_bucket(data_now)
    return data_now
# client = boto3.client('s3', endpoint_url='http://192.168.0.204:9000', config=Config(signature_version='s3v4'), aws_access_key_id='admin', aws_secret_access_key='P@ssw0rd')
# s3 = boto3.resource('s3',
#                     endpoint_url='http://192.168.0.204:9000',
#                     aws_access_key_id='admin',
#                     aws_secret_access_key='P@ssw0rd',
#                     config=Config(signature_version='s3v4'),
#                     region_name='us-east-1')
# bucket="mybucket1"
# name="objectname"
# list = client.list_objects_v2(Bucket=bucket)
# client.create_bucket(Bucket='mybucket1')
# client.Object('mybucket1', f'{str(uuid.uuid4())}.txt').put(Body=open('test.txt', 'rb'))

# client.put_object(Body=f'text.txt', Bucket='mybucket1', Key=f'{str(uuid.uuid4())}.txt')
# print()
# try:
# s3.create_bucket(Bucket='mybucket1')
#    s3.Object('mybucket1', f'{str(uuid.uuid4())}.txt').put(Body=open('test.txt', 'rb'))
# except ClientError:
#   print('создана')


# obj_status = s3.list_objects(Bucket = 'mybucket1')
# print(obj_status)
