conda create -n physical python=3.8 -y  
conda activate physical  
conda install pytorch==1.11.0 torchvision==0.12.0  cudatoolkit=11.3 -c pytorch  
pip install -r requirements.txt  
mkdir lib  
cd lib  
git clone https://github.com/ultralytics/yolov5  
cd ..  
cd assets
mkdir img