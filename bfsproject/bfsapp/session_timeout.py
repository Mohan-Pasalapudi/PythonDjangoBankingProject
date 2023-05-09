import datetime


class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            last_activity = request.session.get('last_activity')
            if last_activity:
                time_since_last_activity = (datetime.datetime.now() - last_activity).seconds
                if time_since_last_activity > settings.SESSION_COOKIE_AGE:
                    # Logout user
                    auth.logout(request)
                    messages.info(request, 'You have been automatically logged out due to inactivity.')
                    return redirect('login')
            request.session['last_activity'] = datetime.datetime.now()

        response = self.get_response(request)
        return response
