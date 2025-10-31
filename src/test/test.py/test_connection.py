import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from lambda_handler import lambda_handler


test_json_path = os.path.join(os.path.dirname(__file__), '../events/test.json')
with open(test_json_path) as f:
    event = json.load(f)

lambda_handler(event, None)