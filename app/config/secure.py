from urllib.parse import quote
SECRET_KEY = 'your secret key'
MONGO_URI = "localhost:27017"

CELETY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELETY_BRPLER_URL = 'redis://localhost:6379/0'

MONGODB_SETTINGS = {
    'db': 'china_tod',
    # 'host':"mongodb://root:Ctdna%402104%2310000@dds-2zeaab5b7908f0c41654-pub.mongodb.rds.aliyuncs.com:3717,dds-2zeaab5b7908f0c42111-pub.mongodb.rds.aliyuncs.com:3717/admin?replicaSet=mgset-27617029"
    'host':'mongodb://localhost:27017/database'
}