def get_asyncapi_ui_html(
    *,
    asyncapi_url: str,
):
    html = f"""
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="https://unpkg.com/@asyncapi/react-component@1.0.0-next.44/styles/default.min.css">
        <style>
body {{
    font-family: ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,Noto Sans,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji;
}}
        </style>
    </head>
    <body>
        
        <div id="asyncapi"></div>

        <script src="https://unpkg.com/@asyncapi/react-component@1.0.0-next.44/browser/standalone/index.js"></script>
        <script>
            AsyncApiStandalone.render({{
                schema: {{
                    url: '{asyncapi_url}',
                    options: {{ method: "GET", mode: "cors" }},
                }},
                config: {{
                    show: {{
                        sidebar: true,
                    }}
                }},
            }}, document.getElementById('asyncapi'));
        </script>

    </body>
</html>
    """

    return html
