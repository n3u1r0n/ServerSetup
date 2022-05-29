from app import app

@app.route('/')
def index():
  return 'Nothing here', 404