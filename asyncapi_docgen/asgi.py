from starlette.applications import Starlette
from starlette.responses import HTMLResponse, JSONResponse
from starlette.routing import Route
from .utils import get_asyncapi
from .docs import get_asyncapi_ui_html


def docs(request):
    return HTMLResponse(get_asyncapi_ui_html(asyncapi_url='/asyncapi.json'))


def asyncapi(request):
    return JSONResponse(get_asyncapi(
        title='Test',
        channels={
          'test/test': {
            'subscribe': {
              'operationId': 'TestTestSubscribe'
            }
          }
        },
    ))


app = Starlette(routes=[
    Route('/docs', docs),
    Route('/asyncapi.json', asyncapi)
])
