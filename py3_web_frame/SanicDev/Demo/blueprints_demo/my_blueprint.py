from sanic.response import json
from sanic import Blueprint

bp = Blueprint('my_blueprint')

# 第一个蓝图
@bp.route('/')
async def bp_root(request):
    return json({'my': 'blueprint'})