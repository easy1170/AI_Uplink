import PIL
import os
# Import the Anvil Uplink library
import anvil.server
import anvil.media
# Connect to your Anvil app
anvil.server.connect('server_M56NPM2JZCQRBOJQ6QLVEBZE-56OQRGVZNS7GHKR4' , url="ws://localhost:3030/_/uplink")
@anvil.server.callable
def get_items():
    return "OK"
@anvil.server.callable
def classify_img(file):
    # with anvil.media.TempFile(file) as filename:
    #     img = load_img(filename)
    # img = img.resize((128,128), resample=PIL.Image.BICUBIC)
    # arr = img_to_array(img)
    # arr = np.expand_dims(arr, axis=0)
    # arr /=255.0
    #score = model.predict(arr)

    return "OK"
anvil.server.wait_forever()