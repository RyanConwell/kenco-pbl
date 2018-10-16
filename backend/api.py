from flask import (
    Blueprint, request, current_app
)
from flask_mail import Mail, Message
mail = Mail()

from backend.db import get_db

bp = Blueprint('api',__name__, url_prefix='/api')


@bp.route('/restock', methods=('GET', 'POST'))
def restock():
    if request.method == 'POST':
        device_id = request.form['device_id']

        device = get_db().execute(
            'SELECT * FROM device WHERE id = ?;', (device_id,)
        ).fetchone()

        get_db().execute(
            'INSERT INTO request (device_id) VALUES (?);', (device_id,)
        )
        get_db().commit()

        msg = Message("New Restock Request!")
        msg.recipients = [current_app.config['NOTIFICATION_RECIPIENT']]
        msg.body = 'A new restock request was received.\n\n\nProduct: {}\nLocation: {}\n\n\nThis message was sent automatically by a prototype "smart button"'.format(device['product'], device['location'])
        mail.send(msg)

        return "All good!"
