# 蓝图 组 和 嵌套
### 层次结构
```python
# api/
# ├──content/
# │  ├──authors.py
# │  ├──static.py
# │  └──__init__.py
# ├──info.py
# └──__init__.py
# app.py

# api/content/authors.py
from sanic import Blueprint
authors = Blueprint('content_authors', url_prefix='/authors')


# api/content/static.py
from sanic import Blueprint
static = Blueprint('content_static', url_prefix='/static')


# api/content/__init__.py
from sanic import Blueprint
from .static import static
from .authors import authors
content = Blueprint.group(assets, authors, url_prefix='/content')


# api/info.py
from sanic import Blueprint
info = Blueprint('info', url_prefix='/info')


# api/__init__.py
from sanic import Blueprint
from .content import content
from .info import info
api = Blueprint.group(content, info, url_prefix='/api')


# app.py
from sanic import Sanic
from .api import api
app = Sanic(__name__)
app.blueprint(api)

```
