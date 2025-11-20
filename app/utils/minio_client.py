from io import BytesIO
from minio.api import Minio


from minio import Minio
from app.core import config

minio_client: Minio = Minio(
    endpoint=config.MINIO_ENDPOINT,
    access_key=config.MINIO_ACCESS_KEY,
    secret_key=config.MINIO_SECRET_KEY,
    secure=config.MINIO_USE_SSL
)

def upload_avatar(file_data:bytes, filename:str) -> str:
    """上传头像到MinIO"""
    bucket_name =  config.MINIO_BUCKET_NAME



    # 确保bucket存在
    if not minio_client.bucket_exists(bucket_name):
        minio_client.make_bucket(bucket_name)
    
    file_stream = BytesIO(file_data)
    
    # 上传文件
    result = minio_client.put_object(
        bucket_name=bucket_name,
        object_name=filename,
        data=file_stream,
        length=file_stream.getbuffer().nbytes,
        content_type="image/jpeg"
    )

    if result:
        return f"{filename}"
    
    return ""

def delete_avatar(filename:str):
    """删除头像从MinIO"""
    bucket_name = config.MINIO_BUCKET_NAME
    if minio_client.bucket_exists(bucket_name):
        return minio_client.remove_object(bucket_name, filename)
    return False


def get_avatar_url(filename:str)->str:
    """获取头像的URL"""
    return f"http://{config.MINIO_ENDPOINT}/{config.MINIO_BUCKET_NAME}/{filename}"
