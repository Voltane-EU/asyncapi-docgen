from .models import AsyncAPI


def get_asyncapi(
    *,
    title: str,
    version: str = '0.0.1',
    channels,
    components = None,
    asyncapi_version: str = '2.5.0',
):
    output = {
        'asyncapi': asyncapi_version,
        'info': {
            'title': title,
            'version': version,
        },
        'channels': channels,
        'components': components,
    }

    return AsyncAPI(**output) #.dict(by_alias=True, exclude_none=True)
