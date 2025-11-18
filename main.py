from logic3 import *
from logic4 import *

def get_image(prompt):
    api = FusionBrainAPI('https://api-key.fusionbrain.ai/', 'C53F2CDCF3F1F40630CB27AA9501C29B', '3F0C6A7957FA6F584A43B7AEA00957D1')
    pipeline_id = api.get_pipeline()
    uuid = api.generate(prompt, pipeline_id)
    files = api.check_generation(uuid)
    return files[0]
