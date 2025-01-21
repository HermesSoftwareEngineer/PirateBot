from flask import Blueprint, render_template, request
from .conversar_com_ia import conversar

bp = Blueprint('chat', __name__)
messages = []

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        human_message = request.form['message']
        messages.append(
            {
                'role': 'human',
                'content': human_message
            }
        )

        ia_message = conversar(human_message)
        messages.append(
            {
                'role': 'ia',
                'content': ia_message
            }
        )
        
        return render_template('chat.html', messages=messages)
    return render_template('chat.html', messages=messages)