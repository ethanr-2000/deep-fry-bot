from itertools import islice
from fbchat import Client
from fbchat.models import *
import src.deeppyer as dp
import requests
from io import BytesIO
from PIL import Image

username = "<username>"
password = "<password>"
t_id = "<id>"


class DeepFryBot(Client):
    def onMessage(self, mid=None, author_id=None,
                  message=None, message_object=None,
                  thread_id=t_id, thread_type=ThreadType.GROUP,
                  ts=None, metadata=None, msg=None):
        try:
            if message_object.text == "Can I request a deep fry":
                im = []
                images = self.fetchThreadImages(thread_id=thread_id)
                for i in islice(images, 1):
                    im_url = i.large_preview_url
                    res = requests.get(im_url)
                    im = Image.open(BytesIO(res.content))

                fry_im = dp.deepfry(im)
                fry_im.save('fried.jpg')
                self.sendLocalImage('fried.jpg', thread_id=thread_id, thread_type=thread_type)
        except Exception as e:
            self.sendMessage('Sorry, something went wrong', thread_id=thread_id, thread_type=thread_type)


client = DeepFryBot(username, password, max_tries=1)
client.listen()
