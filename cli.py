"""CLI app implemented in docopt,that fetches a public API using HTTP client library 
Usage:
    cli.py latest
    cli.py history <date> 
    cli.py currency <base>
    cli.py (-h | --help)
Arguments
    <command> 
    <date> date
    <base> base
Options:
   -h --help    Show this screen"""

from docopt import docopt
import requests
import json
def get_latest():
  response=requests.get('http://api.fixer.io/latest')
  data=response.json()
  return data  
def get_history(date):
  new=requests.get('http://api.fixer.io/'+ date)
  extra=new.json()
  return extra
def get_currency(base):
  curr=requests.get('http://api.fixer.io/latest?base=' + base)
  info=curr.json()
  return info
if __name__=='__main__':
    ARGS = docopt(__doc__, version='1.0')  
if ARGS['latest']:
  print(get_latest())
if ARGS['history']:
  print(get_history(ARGS['<date>']))
if ARGS['currency']:
  print(get_currency(ARGS['<base>'])) 







