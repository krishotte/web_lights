"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    Get('/home', 'WelcomeController@show').name('welcome'),

    Get('/', 'LightsController@show'),
    Post('/', 'LightsController@update')
]
