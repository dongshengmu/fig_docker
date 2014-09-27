from flask import Flask
from redis import Redis
import os
app = Flask(__name__)
redis = Redis(host="redis_1", port=6379)
redis.set('greeting', 'Hello')

@app.route('/')
def hello():
    import os
    hostname = os.getenv('HOSTNAME')
    redis.incr('hits')
    return '%s hostname %s! I have been seen %s times.' % (redis.get('greeting'), hostname, redis.get('hits'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
