import os
import shutil

def start(r_path):

    cpu = os.path.join(r_path, "CPU")
    gpu = os.path.join(r_path, "GPU")
    m_board = os.path.join(r_path, "M_BOARD")
    extra = os.path.join(r_path, "Extra")

    for folder in [cpu, gpu, m_board, extra]:
        os.makedirs(folder, exist_ok=True)


    for file in os.listdir(r_path):
        path_file = os.path.join(r_path, file)
        
        if file.endswith(".txt"):
            if file.startswith("cpu_"):
                shutil.move(path_file, cpu)

            elif file.startswith("gpu_"):
                shutil.move(path_file, gpu)

            elif file.startswith("m_"):
                shutil.move(path_file, m_board)

            else:
                shutil.move(path_file, extra)

        else:
            if not os.path.isdir(path_file):
                shutil.move(path_file, extra)
        
        