"""CLI app implemented in docopt,that fetches a public API using HTTP client library 
Usage:
    api.py create <title> <body>
    api.py get_all
    api.py get <post_id>
    api.py edit <post_id> <title> <body>
    api.py remove <post_id>
    api.py (-h | --help)
Arguments
    <command>
    <post_id>  The post id
    <title> The post title
    <body>  The post body
Options:
   -h --help    Show this screen"""
from docopt import docopt
import requests

API_URL='https://jsonplaceholder.typicode.com/posts/'

if __name__=='__main__':
    ARGS = docopt(__doc__, version='1.0')

if ARGS['create']:
    # POST
    PAYLOAD={
        'title': ARGS['<title>'],
        'body': ARGS['<body>']
    }

    RES=requests.post(API_URL, data=PAYLOAD)

    if RES.status_code==201:
        print('Successfully Created')
        for post in RES:
            print(post)
    else:
        print('Error: Problem creating post. ' \
            'Please check if you have write access',)

if ARGS['get_all']:
    # GET
    RES=requests.get(API_URL)
    if RES.status_code==200:
        print('Getting all posts...')
        for post in RES:
            print(post)
    else:
        print('Error: There was a problem ' \
            'processing your request')

if ARGS['get']:
    # GET specific
    POST_ID=ARGS['<post_id>']
    RES=requests.get(API_URL + POST_ID)

    if RES.status_code==200:
        print('Fetching post ' + POST_ID + ' successful')

        for post in RES:
            print(post)
    else:
        print('Error: There was a problem getting your post')

if ARGS['edit']:
    # PUT
    PAYLOAD={
        'title': ARGS['<title>'],
        'body': ARGS['<body>']
    }
    RES=requests.put(API_URL+ARGS['<post_id>'], data=PAYLOAD)

    if RES.status_code==200:
        print('Edit successful')
        for post in RES:
            print(post)
    else:
        print('Error: Problem editting post')

if ARGS['remove']:
    # DELETE
    POST_ID=ARGS['<post_id>']
    RES=requests.delete(API_URL+POST_ID)

    if RES.status_code==200:
        print('Post ' + POST_ID + ' successfully deleted')
    else:
        print('Error: Problem deleting post')
