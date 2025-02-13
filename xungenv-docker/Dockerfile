# Sử dụng image Anaconda chính thức
FROM continuumio/anaconda3

# Thiết lập thư mục làm việc trong container
WORKDIR /workspace

# Copy file environment.yml vào container
COPY environment.yml /workspace/environment.yml

# Tạo môi trường Conda từ environment.yml
RUN conda env create -f environment.yml

# Đảm bảo shell mở với môi trường đã kích hoạt
RUN echo "conda activate my_env" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

# Mở Python theo mặc định
CMD ["python"]