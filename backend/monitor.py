from flask import (
    Blueprint, render_template
)
from backend.db import get_db

bp = Blueprint('monitor', __name__)


@bp.route('/')
def index():
    db = get_db()
    requests = db.execute(
        'SELECT created, product, location FROM request JOIN device ON device_id = device.id ORDER BY created DESC;'
    ).fetchall()

    return render_template('monitor.html', requests=requests)