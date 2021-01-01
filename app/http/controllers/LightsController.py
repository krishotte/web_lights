"""A LightsController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.response import Response
from masonite.controllers import Controller
from test_lights import get_lights, set_lights


class LightsController(Controller):
    """LightsController Controller Class."""

    def __init__(self, request: Request):
        """LightsController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        levels = [6, 8, 10, 12, 14, 16, 20, 40, 55, 70, 85, 98]
        levels.reverse()
        try:
            current_status = get_lights()[0:2]
            message = 'OK'
        except Exception:
            current_status = [0, 0]
            message = 'connection error'

        return view.render('lights', {
            'levels': levels,
            'current': current_status,
            'message': message,
        })

    def update(self, request: Request, response: Response):

        channel = -1
        level = -1
        try:
            print(f' channel 0: {request.all()["0"]}')
            channel = 0
            level = int(request.all()["0"])
        except KeyError:
            try:
                print(f' channel 1: {request.all()["1"]}')
                channel = 1
                level = int(request.all()["1"])
            except KeyError:
                print('channel not found')

        print(f' setting channel: {channel} to value: {level}')

        try:
            set_lights(channel, level)
            message = 'OK'
        except Exception:
            message = 'connection error'

        # return request.all()
        return response.redirect('/')
