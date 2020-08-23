FROM ubuntu:16.04

LABEL maintainer="Bikram"

# Pick up some TF dependencies
#RUN add-apt-repository ppa:jonathonf/python-3.6
#RUN sudo apt update
#RUN sudo apt install python3.6
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        libfreetype6-dev \
        libhdf5-serial-dev \
        libpng12-dev \
        libzmq3-dev \
        pkg-config \
	python3-pip \
        python \
        python-dev \
	python3 \
	python3-dev \
        rsync \
        software-properties-common \
        unzip \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    rm get-pip.py

RUN pip --no-cache-dir install \
        Pillow \
        h5py \
        ipykernel \
        jupyter \
        keras_applications==1.0.5 \
        keras_preprocessing==1.0.3 \
        matplotlib \
        numpy \
        pandas \
        scipy \
        sklearn \
        && \
    python -m ipykernel.kernelspec

# Install TensorFlow CPU version
RUN pip --no-cache-dir install \
    tensorflow
# --- ~ DO NOT EDIT OR DELETE BETWEEN THE LINES --- #
RUN pip install http://download.pytorch.org/whl/cpu/torch-0.4.1-cp27-cp27mu-linux_x86_64.whl
RUN pip install torchvision
# RUN ln -s -f /usr/bin/python3 /usr/bin/python#

# Set up our notebook config.
COPY jupyter_notebook_config.py /root/.jupyter/

# We just add a little wrapper script.
COPY run_jupyter.sh /

########## Below Part is not required if you are doing same over AWS ECS Console 
RUN mkdir -p /mnt/efs_data
RUN chown -R user:user /mnt/efs_data
VOLUME  /home/ubuntu/efs:/mnt/efs_data

# TensorBoard
EXPOSE 6006
# IPython
EXPOSE 8888

WORKDIR "/notebooks"

CMD ["/run_jupyter.sh", "--allow-root"]

#If you want to show the token ducring initial ia=mage run 
#CMD ["/usr/local/bin/jupyter notebook list"]
