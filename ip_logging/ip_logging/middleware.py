import logging

from django.utils import timezone
from django.http import HttpResponseForbidden

from account.models import RequestCount


# Configure logging
logger = logging.getLogger("ip_logger")


class IpLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        ip_address = request.META.get("REMOTE_ADDR")
        request_time = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        path = request.path

        logger.info(
            f"Path : {path} , Ip Address : {ip_address} , Request_time : {request_time}"
        )

        response = self.get_response(request)

        return response


class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if "admin" not in request.path:
            ip = request.META.get("REMOTE_ADDR")
            rate_limit_time = timezone.now() - timezone.timedelta(minutes=1)

            request_obj, created = RequestCount.objects.get_or_create(
                ip=ip, defaults={"count": 1}
            )

            if request_obj.updated_at >= rate_limit_time:
                if request_obj.count >= 5:
                    return HttpResponseForbidden(
                        "You have exceeded the limit of 5 requests per minute."
                    )
                else:
                    request_obj.count += 1
            else:
                request_obj.count = 1
            request_obj.save()

        response = self.get_response(request)

        return response
