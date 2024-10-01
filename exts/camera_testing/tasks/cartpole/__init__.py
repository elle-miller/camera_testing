# Copyright (c) 2022-2024, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""
Cartpole balancing environment.
"""

import gymnasium as gym

from . import agents

from .camera_cartpole import CartpoleRGBCameraEnvCfg

##
# Register Gym environments.
##

print("Registering cartpole environments")



gym.register(
    id="ImageCartpole",
    entry_point="camera_testing.tasks.cartpole.camera_cartpole:CartpoleCameraEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": CartpoleRGBCameraEnvCfg,
        "skrl_cfg_entry_point": f"{agents.__name__}:skrl_camera_ppo_cfg.yaml",
    },
)
