
FROM odoo:16.0

USER root
RUN pip3 install --upgrade pip
USER odoo
