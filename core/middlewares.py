import logging

from django.contrib.auth.middleware import MiddlewareMixin


logger = logging.getLogger(__name__)


class LogRequestMiddleware(MiddlewareMixin):
    def process_request(self, request):
        logger.debug(f"Request Headers: {request.headers}")
        logger.debug(f"Request Body: {request.body}")

    def process_response(self, request, response):
        # noinspection PyBroadException
        try:
            logger.debug(f"Response Body: {response.content}")
        except Exception:
            pass
        return response
