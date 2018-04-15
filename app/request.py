import urllib.request,json
from .models import Images

api_key =None
base_url=None

def configure_request(app):
    global api_key,base_url
    api_key =app.config['PIX_API_KEY']
    base_url=app.config['PIX_BASE_URL']
def get_images(category):
    '''
    function that makes the request and gets the json response
    '''
    get_images_url=base_url.format(api_key,category)

    with urllib.request.urlopen(get_images_url) as url:
        get_images_data=url.read()
        get_images_response=json.loads(get_images_data)

        hits_results =None

        if get_images_response['hits']:
            hits_results_list=get_images_response['hits']
            hits_results= process_results(hits_results_list)
    return hits_results
def process_results(hits_list):
    hits_results=[]
    for item in hits_list:
        id= item.get('id')
        userImageURL=item.get('userImageURL')
        webformatURL=item.get('webformatURL')

        image_object =Images(id,userImageURL,webformatURL)
        hits_results.append(image_object)
    return hits_results
