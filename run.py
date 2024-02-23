import os
from my_suite import my_app


if __name__ == "__main__":
    my_app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )