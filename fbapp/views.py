from flask import Flask, render_template, url_for, request

app = Flask(__name__)

app.config.from_object('config')

from .utils import find_content, OpenGraphImage

@app.route('/')
@app.route('/index/')
def index():
  if 'img' in request.args:
    img = request.args['img']
    og_image = url_for('static', filename=img, _external=True)
    og_url = url_for('index', img=img, _external=True)
  else:
    og_image = url_for('static', filename='tmp/sample.jpg', _external=True)
    og_url = url_for('index', _external=True)
  description = """
                    Toi, tu n'as pas peur d'être seul ! Les grands espaces et les aventures sont faits pour toi. D'ailleurs, Koh Lanta est ton émission préférée ! Bientôt tu partiras les cheveux au vent sur ton radeau. Tu es aussi un idéaliste chevronné. Quelle chance !
                """

  return render_template('result.html',
                          user_name='Julio',
                          user_image=url_for('static', filename='img/profile.png'),
                          description=description,
                          blur=True,
                          og_url=og_url,
                          og_image=og_image)

@app.route('/result/')
def result():
  user_name = request.args.get('first_name')
  gender = request.args.get('gender')
  description = find_content(gender).description
  uid = request.args.get('id')
  profile_pic = 'http://graph.facebook.com/' + uid + '/picture?type=large'
  img = OpenGraphImage(uid, user_name, description).location
  og_url = url_for('index', _external=True, img=img)
  return render_template('result.html',
                          user_name=user_name,
                          user_image=profile_pic,
                          description=description,
                          og_url=og_url)
# if __name__ == "__main__":
#     app.run()
