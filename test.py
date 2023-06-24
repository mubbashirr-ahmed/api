from flask import Flask, request
import facebook

app = Flask(__name__)

@app.route('/post_image', methods=['POST'])
def post_image():
    page_access_token = request.form.get('page_access_token')
    image = request.files.get('image')
    msg = request.form.get('message')

    if not image and (not msg or len(msg) < 1):
        return 'Image or message cannot be empty!', 400

    graph = facebook.GraphAPI(page_access_token)

    if image:
        image_data = image.read()
        graph.put_photo(image=image_data, message=msg)
    else:
        if len(msg) >= 1:
            graph.put_object(parent_object='me', connection_name='feed', message=msg)
        else:
            return 'Message cannot be empty!', 400

    return 'Post created successfully!'

if __name__ == '__main__':
    app.run()
