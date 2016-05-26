#!/usr/bin/env python
#-*- coding: utf-8 -*-

from clarifai.client import ClarifaiApi
clarifai_api = ClarifaiApi() # assumes environment variables are set.
result = clarifai_api.tag_images(open('tests/data/metro-north.jpg', 'rb'))
print result['results'][0]['result']['tag']['classes']
