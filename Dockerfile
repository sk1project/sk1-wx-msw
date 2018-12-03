FROM ubuntu:16.04
MAINTAINER sk1.project.org@gmail.com
 
RUN apt-get update && apt-get install -y gcc sudo python-dev python-gi \
gir1.2-glib-2.0 gir1.2-libmsi0 gir1.2-libgcab-1.0 python-pip \
&& pip install WiX.Py && apt-get clean

RUN mkdir -p /win32-devres/
RUN mkdir -p /win64-devres/

COPY win32-devres/pyd/ /win32-devres/pyd/
COPY win32-devres/portable.zip /win32-devres/
COPY win32-devres/sk1_msi.zip /win32-devres/
COPY win32-devres/uc2.zip /win32-devres/

COPY win64-devres/pyd/ /win64-devres/pyd/
COPY win64-devres/portable.zip /win64-devres/
COPY win64-devres/sk1_msi.zip /win64-devres/
COPY win64-devres/uc2.zip /win64-devres/

COPY sk1.ico /win32-devres/
COPY gpl_v3.rtf /win32-devres/
 
CMD ["/vagrant/bbox.py", "msw_build"]
