import json
import math

def get_angle(x1, y1, x2, y2):
    return math.degrees(math.atan2(y2 - y1, x2 - x1))

def is_fallen(pose):
    keypoints = pose['keypoints']

    # 関節位置（y座標）取得（平均値を使って姿勢を判断）
    left_shoulder_y = keypoints[5 * 3 + 1]
    right_shoulder_y = keypoints[6 * 3 + 1]
    left_ankle_y = keypoints[15 * 3 + 1]
    right_ankle_y = keypoints[16 * 3 + 1]

    avg_shoulder_y = (left_shoulder_y + right_shoulder_y) / 2
    avg_ankle_y = (left_ankle_y + right_ankle_y) / 2
    vertical_diff = avg_ankle_y - avg_shoulder_y

    left_shoulder_x = keypoints[5 * 3]
    right_shoulder_x = keypoints[6 * 3]
    shoulder_width = abs(left_shoulder_x - right_shoulder_x)

    # 条件：肩と足首の高さが近く、肩幅が広ければ転倒とみなす
    if vertical_diff < 50 and shoulder_width > 100:
        return True
    return False


def detect_falls_from_json(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)

    for item in data:
        frame_id = item['image_id']
        person_pose = item
        fallen = is_fallen(person_pose)
        if fallen:
            print(f"🚨 転倒検出！: {frame_id}")
        else:
            print(f"✅ 正常: {frame_id}")

# アップロードしたファイルを使って実行
detect_falls_from_json('/home/umi/ビデオ/koke/koronbusu.json')
