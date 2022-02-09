# Django
in docker file:
ENV PYTHONUNBUFFERED 1  //it dosen't allow python to buffered the outputs it just prit directly. avoid complecation while run docker image

RUN adduser -D user // adduser will create user -D will create user only for running this application not for home directory
USER user \    // will switch the user that we jsut created