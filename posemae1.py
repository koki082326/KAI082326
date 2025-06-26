import json
import numpy as np

def process_pose_json(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    poses = []
    for frame in data:
        if 'keypoints' in frame:
            keypoints = frame['keypoints']
            joints = []
            for i in range(0, len(keypoints), 3):  # x, y, confidence
                x = keypoints[i]
                y = keypoints[i + 1]
                conf = keypoints[i + 2]
                if conf < 0.5:
                    x, y = np.nan, np.nan
                joints.extend([x, y])
            poses.append(joints)

    poses = np.array(poses)
    return poses

# ★ ここでファイルパスを定義する（上に置く！）
json_file = '/home/umi/ビデオ/koke/koronbusu.json'

# ★ 関数呼び出しはファイルパス定義の後！
pose_data = process_pose_json(json_file)
print(pose_data.shape)
print("全フレーム数:", pose_data.shape[0])
print("1フレームあたりのキーポイント数:", pose_data.shape[1])

