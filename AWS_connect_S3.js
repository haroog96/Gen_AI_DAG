const aws = require('aws-sdk')
const config = require('./config.json')

(
async function(){
    try {
        aws.config.update({
           accessKeyId:config.accessKeyId,
           secretAccessKey:config.secretAccessKey,
           region: 'us-east-1'
        });
        console.log('Successfully connected');
    } catch (error) {
        console.log('our error',e);
    }
}
)();
