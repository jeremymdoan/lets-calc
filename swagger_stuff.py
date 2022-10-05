template = {
    "swagger": "2.0",
    "info": {
        "title": "Let's calc",
        "description": (
            "A simple api to do calcs"
        ),
        "contact": {
            "responsibleOrganization": "Jeremy Doan",
            "responsibleDeveloper": "Jeremy Doan",
        },
        # "termsOfService": "http://me.com/terms",
        "version": 0.1,
    },
    "host": "127.0.0.1:5000",  # overrides localhost:5000
    "basePath": "/",  # base bash for blueprint registration
    "schemes": ["http"],
    "protocol": "http",
    "tags": [
        {
            "name": "Functions",
            "description": "Different calcs you can try"
        },
    ],
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "spec",
            "route": "/spec.json",
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": "/",
}
