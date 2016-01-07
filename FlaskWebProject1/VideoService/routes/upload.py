
from VideoService import app
from datetime import datetime 
from time import strftime
import boto3

@app.before_request 
def before_requset(): 
    app.db = boto3.resource('dynamodb', 
                        region_name = 'us-west-2', 
                        aws_access_key_id = 'AKIAJ6DLWSW52NGKCFDQ', 
                        aws_secret_access_key = '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') 
    
@app.route('/generate_id/<username>', methods=['GET']) 
def generate_ID(username):
 #   app.logger.info('Start generating vidoe ID') 
     
    video_id = username + '_' + datetime.utcnow().strftime("%y%m%d_%H%M%S") 

    return video_id 


@app.route('/upload/<vid>', methods=['GET']) 
def upload(vid):
    #TODO
    #Django code snippet

    return 'completed' + vid


@app.route('/user/<name>', methods = ['GET'])
def get_user(name): 
    table_user = app.db.Table('users') 
    user = table_user.get_item(Key={'username' : name }) 
    if not user['Item']: 
        return 'no such user exists'
    try:  
       vid = user['Item']['vid'] 
    except Exception as e: 
        return 'This user current does not have any video'  