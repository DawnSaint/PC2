from pytorch3d.structures import Pointclouds
from scipy.spatial.distance import cdist
import numpy as np

def point_cloud_f1_score(predicted: Pointclouds, ground_truth: Pointclouds, distance_threshold=0.1):
    # Get point coordinates
    points1 = predicted.points_padded().cpu().numpy()
    points2 = ground_truth.points_padded().cpu().numpy()

    # Calculate the minimum distance from each predicted point to the ground truth point cloud
    dist_matrix = cdist(points1[0], points2[0], 'euclidean')
    min_dist1 = np.min(dist_matrix, axis=1)
    min_dist2 = np.min(dist_matrix, axis=0)

    # Determine the matched points
    true_positives1 = np.sum(min_dist1 < distance_threshold)
    true_positives2 = np.sum(min_dist2 < distance_threshold)
    false_positives = points1.shape[1] - true_positives1
    false_negatives = points2.shape[1] - true_positives2

    # Compute Precision and Recall
    precision = true_positives1 / (true_positives1 + false_positives) if (true_positives1 + false_positives) > 0 else 0
    recall = true_positives2 / (true_positives2 + false_negatives) if (true_positives2 + false_negatives) > 0 else 0

    # Calculate F1-Score
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    print(f"F1-Score: {f1}")
    
    return f1

# # 创建示例点云数据
# points1 = torch.randn(1, 16384, 3)  # 预测的点云
# points2 = torch.randn(1, 16384, 3)  # 真实的点云

# # 创建 Pointclouds 对象
# predicted = Pointclouds(points1)
# ground_truth = Pointclouds(points2)

# # 计算 F1-Score
# f1 = point_cloud_f1_score(predicted, ground_truth, distance_threshold=0.01)

