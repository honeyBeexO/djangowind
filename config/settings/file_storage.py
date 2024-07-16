from config.env import env
# STORAGES setting: Starting with Django 4.2, default file storage engine
# can be configured with the STORAGES setting under the default key.
# Previously: DEFAULT_FILE_STORAGE setting

STORAGES = {
        "default": {
            "BACKEND": "storages .backends.s3.S3Storage",
            "OPTIONS": {}
        }
}

AWS_S3_ACCESS_KEY_ID = env ("AWS_S3_ACCESS _KEY _ID")
AWS_S3_SECRET_ACCESS_KEY = env ("AWS_S3_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env ("AWS_STORAGE _BUCKET_NAME")
AWS_S3_REGION_NAME = env ("AWS _S3_REGION_NAME")

# from storages.backends.s3boto3 import S3Boto3Storage


# class StaticRootS3Boto3Storage(S3Boto3Storage):
#     location = "static"
#     default_acl = "public-read"


# class MediaRootS3Boto3Storage(S3Boto3Storage):
#     location = "media"
#     file_overwrite = False