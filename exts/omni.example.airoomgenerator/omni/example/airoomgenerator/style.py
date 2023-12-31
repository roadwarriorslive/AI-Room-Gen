# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import omni.ui as ui
from pathlib import Path

icons_path = Path(__file__).parent.parent.parent.parent / "icons"


gen_ai_style = {
    "HStack": {
        "margin": 3
    },
    "Button.Image::create": {"image_url": f"{icons_path}/plus.svg", "color": 0xFF00B976},
    "Button.Image::properties": {"image_url": f"{icons_path}/cog.svg", "color": 0xFF989898},
    "Line": {
        "margin": 3
    },
    "Label": {
        "margin_width": 5
    }
}


guide = """
Step 1: Select your Room
- Select your room and then click the '+' button. This will fill your room's path into the Area path box.

Step 2: Prompt
- Type in a prompt that you want to send along to ChatGPT. This can be information about what is inside of the room.
    For example, "generate a comfortable reception area that contains a front desk and an area for guest to sit down".

Step 3: Generate
- Select 'use ChatGPT' if you want to recieve a response from ChatGPT otherwise it will use a premade response.
    To use GPT you will need to enter an Open AI API key in the settings by clicking on the gear icon.
- Select 'use Deepsearch' if you want to use the deepsearch functionality.
    To use Deepsearch you will need a connection to an enterprise nucleus server with deepsearch enabled.
    Enter the path to this server in the "Nucleus Path" setting.
    Enter folder paths with props (rather than scenes) separated by commas (no spaces) in the "Path Filter" setting.
    When deepsearch is false it will spawn in cubes that greybox the scene.
- Hit Generate, after hitting generate it will start making the appropriate calls. Loading bar will be shown as api-calls are being made.
- Note: This extension assumes your scene is Y-up and that your assets are scaled in meters. 

Step 4: More Rooms
- To add another room you can repeat Steps 1-3.
- If you do not like the items it generated, you can hit the generate button until you are satisfied with the items.
"""