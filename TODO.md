Adapt FTs so they can run against a staging server.
Spin up a server, install required software and point staging/live domains at it.
Upload code to the server using Git.
Get a quick & dirty version of the site running on staging domain using Django dev server.
Manually set up virtualenv on the server (without virtualenvwrapper).
Move from quick & dirty version to production-ready configuration using Gunicorn, Systemd and domain sockets.
Write a script to automate deployment of the site.
Use the script to deploy the production version of the site.

