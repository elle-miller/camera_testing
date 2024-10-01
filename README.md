### camera_testing



Reproduce camera issue
```
python scripts/train.py --task ImageCartpole --headless --enable_cameras --num_envs 4
```



## Installation
Clone latest Isaac Lab release
```
git@github.com:isaac-sim/IsaacLab.git
cd IsaacLab
```

Install Isaac Sim via pip through conda environment
```
# miniconda install https://docs.anaconda.com/miniconda/#quick-command-line-install
conda create -n isaaclab python=3.10
conda activate isaaclab
pip install torch==2.4.0 --index-url https://download.pytorch.org/whl/cu118
pip install --upgrade torchvision
pip install --upgrade pip
# uninstall these first to upgrade
pip install isaacsim-rl isaacsim-replicator isaacsim-extscache-physics isaacsim-extscache-kit-sdk isaacsim-extscache-kit isaacsim-app --extra-index-url https://pypi.nvidia.com
```
Install Isaac Lab and verify it works:
```
cd IsaacLab
./isaaclab.sh --install
python source/standalone/workflows/skrl/train.py --task Isaac-Reach-Franka-v0 --headless
```
Install `camera_testing` extension as editable package. Test if working.
```
git clone git@github.com:elle-miller/camera_testing.git
cd camera_testing
python -m pip install -e .
```
