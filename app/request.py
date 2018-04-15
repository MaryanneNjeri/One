import urlib.request,json
from .models import Images

api_key =None
base_url=None

def configure_request(app):
    global api_key,base_url
    api_key =api.config['PIX_API_KEY']
    base_url=app.config['PIX_BASE_URL']
def get_images(category):
    '''
    function that makes the request and gets the json response
    '''
    get_images_url=base_url.format(api_key,category)

    with urlib.request.urlopen(get_sources_url) as url:
        get_images_data=url.read()
        get_images_response=json.loads(get_images_data)

        images_results =None

        if get_images_response['hits']:
            images_results_list=get_images_response['hits']
            images_results= process_results(images_results)
        return images_results
def process_results(hits_list):
    images_results=[]
    for result in hits_list:
        id= result.get('id')
        userImageURL=result.get('userImageURL')
        webformatURL=result.get('webformatURL')
    if id:
        image_object =Images(id,userImageURL,webformatURL)
        images_results.append(image_object)
    return images_results
