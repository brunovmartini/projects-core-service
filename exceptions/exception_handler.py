from flask import Flask, Response
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError, Unauthorized


def add_exception_handler(app: Flask):
    @app.errorhandler(BadRequest)
    def handle_bad_request(e):
        return Response(
            response='Invalid request body.',
            status=400
        )

    @app.errorhandler(NotFound)
    def handle_not_found_error(e):
        return Response(
            response=e.description,
            status=404
        )

    @app.errorhandler(Unauthorized)
    def handle_not_found_error(e):
        return Response(
            response='User unauthorized.',
            status=401
        )

    @app.errorhandler(InternalServerError)
    def handle_not_found_error(e):
        return Response(
            response=e.description,
            status=500
        )
