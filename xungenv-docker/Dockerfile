<<<<<<< HEAD
# chỉ định image gốc ban đầu mà muốn tạo ra sự thay đổi
# FROM continuumio/miniconda3

# tạo 1 thư mục làm mặc định cho container khi khởi tạo
# WORKDIR /workspace

# Copy file environment.yml vào container
# COPY environment.yml /workspace/environment.yml

# là các lệnh mà ta muốn chạy trong container : Tạo môi trường Conda từ environment.yml
# RUN conda install -n base -c conda-forge mamba && \
  #   mamba env create -f /tmp/environment.yml && \
  #   conda clean --all -y

# Đảm bảo shell mở với môi trường đã kích hoạt
# RUN echo "conda activate my_env" >> ~/.bashrc
# SHELL ["/bin/bash", "--login", "-c"]

# câu lệnh mồi chỉ thực thi khi khởi chạy container: Mở Python theo mặc định
# CMD ["python"]


FROM alpine
RUN apk add bash
CMD ["bash"]
=======
# # Sử dụng image Anaconda chính thức
# FROM continuumio/anaconda3

# # Thiết lập thư mục làm việc trong container
# WORKDIR /workspace

# # Copy file environment.yml vào container
# COPY environment.yml /workspace/environment.yml

# # Tạo môi trường Conda từ environment.yml
# RUN conda env create -f environment.yml

# # Đảm bảo shell mở với môi trường đã kích hoạt
# RUN echo "conda activate my_env" >> ~/.bashrc
# SHELL ["/bin/bash", "--login", "-c"]

# # Mở Python theo mặc định
# CMD ["python"]

# Sử dụng một image base từ Alpine Linux (nhẹ, nhanh)
FROM alpine:latest

# Thiết lập một lệnh mặc định khi container chạy
CMD ["echo", "Hello, Docker!"]
>>>>>>> e54226585b711790cddd9e5dc17e025ed8eb5084
