from clarifai.client import ClarifaiApi
clarifai_api = ClarifaiApi() # assumes environment variables are set.
result = clarifai_api.tag_images(open(‘capstone/tests/data/metro-north.jpg’, 'rb'))
