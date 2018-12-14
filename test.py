import requests
import json

web_hook_url= 'https://hooks.slack.com/services/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'
slack_msg= {'text':'Alert from Python'}
requests.post(web_hook_url,data=json.dumps(slack_msg))
