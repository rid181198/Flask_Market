from market import app
import os
if __name__=='__main__':
    app.run(host = '0.0.0.0',debug=os.environ.get('DEBUG') == '1', port=5000)