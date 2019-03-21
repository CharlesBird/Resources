from flask import current_app, request, jsonify, url_for
from ..models import User, Post
from . import api


@api.route('/users/<int:id>')
def get_user(id):
    """
    获取用户信息
    ---
    tags:
    - "User"
    parameters:
      - name: id
        in: path
        type: integer
        format: int64
        required: true
    definitions:
      User:
        type: "object"
        properties:
          id:
            type: integer
            format: int64
    responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/User"
        400:
          description: "Invalid ID supplied"
        404:
          description: "Users not found"
    """
    user = User.query.get_or_404(id)
    return jsonify(user.to_json())


@api.route('/users/<int:id>/posts/')
def get_user_posts(id):
    """
    获取用户文章信息
    ---
    tags:
    - "User"
    parameters:
      - name: id
        in: path
        type: integer
        format: int64
        required: true
    definitions:
      User:
        type: "object"
        properties:
          id:
            type: integer
            format: int64
    responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/User"
        400:
          description: "Invalid ID supplied"
        404:
          description: "Users not found"
    """
    user = User.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    pagination = user.posts.order_by(Post.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_user_posts', id=id, page=page-1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_user_posts', id=id, page=page+1)
    return jsonify({
        'posts': [post.to_json() for post in posts],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })


@api.route('/users/<int:id>/timeline/')
def get_user_followed_posts(id):
    """
    获取关注的用户文章信息
    ---
    tags:
    - "User"
    parameters:
      - name: id
        in: path
        type: integer
        format: int64
        required: true
    definitions:
      User:
        type: "object"
        properties:
          id:
            type: integer
            format: int64
    responses:
        200:
          description: "successful operation"
          schema:
            $ref: "#/definitions/User"
        400:
          description: "Invalid ID supplied"
        404:
          description: "Users not found"
    """
    user = User.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    pagination = user.followed_posts.order_by(Post.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_user_followed_posts', id=id, page=page-1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_user_followed_posts', id=id, page=page+1)
    return jsonify({
        'posts': [post.to_json() for post in posts],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })
