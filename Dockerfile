# The 'Package' stage of the journey.
# This file is the recipe; the built image is the sealed container that
# runs identically anywhere - laptop, test, or production.

FROM python:3.12-slim

# Everything the app needs travels inside the image. This is why
# "works on my machine" stops being a problem.
WORKDIR /app
COPY app/ ./app/

# No third-party dependencies needed for the demo - the standard library
# is enough. In a real app, this is where 'pip install -r requirements' goes.

EXPOSE 8000
CMD ["python", "app/main.py"]
