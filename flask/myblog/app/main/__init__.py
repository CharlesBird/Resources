from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
from ..models import Permission

@main.app_context_processor
def inject_permissions():
    """
    app_context_processor在flask中被称作上下文处理器
    把 Permission 类加入模板上下文
    """
    return dict(Permission=Permission)