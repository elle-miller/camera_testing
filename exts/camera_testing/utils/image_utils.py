import numpy as np
import os
import torch
import torchvision.transforms as transforms
from PIL import Image
from typing import List


def save_trajectory_gif_to_wandb(trajectory: List[torch.Tensor], wandb_session) -> None:
    """

    Args:
        trajectory: list of images in shape [T, H, W, C] or [T, C, H, W]
        wandb_session:

    wandb expects T, C, H, W

    Returns:

    """
    trajectory = torch.cat(trajectory, 0).cpu()

    if np.argmin(trajectory.shape) == 3:
        permute_order = (0, 3, 1, 2)
    else:
        permute_order = (0, 1, 2, 3)

    if trajectory.dtype is torch.float32:
        trajectory *= 255

    gen = np.array(trajectory[:, :, :, :3].permute(permute_order)).astype(np.uint8)

    wandb_session.log({'video': wandb_session.Video(gen, fps=60)})


def save_image(obs, img_name="lift.png", subfolder=None, nchw=True, print_stack=False):
    """
    Expects image in NCHW format, if in NHWC then set nchw=False
    """
    # filesaving 
    # img_dir = "/home/emil/code/external/IsaacLab/IsaacLabExtension/images/franka/"
    img_dir = "./images"
    
    if subfolder is not None:
        img_dir = os.path.join(img_dir, subfolder)
    
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)

    file_path = os.path.join(img_dir, img_name)

    obs = obs.clone()

    # reshape to have channels at last index
    if nchw:
        obs = obs.transpose(1, -1)

    if obs.dtype is torch.float32:
        obs *= 255

    obs = np.array(obs[0, :, :, :3].cpu()).astype(np.uint8)
    
    # the image needs to be in the shape [height, width, channels]
    img = Image.fromarray(obs)
    img.save(file_path)
