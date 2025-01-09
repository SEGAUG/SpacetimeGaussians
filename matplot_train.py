import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

log_filename = "training.log"  # 替换为日志文件实际路径

# 解析日志文件
data = []
with open(log_filename, "r") as file:
    for line in file:
        if "Loss:" in line and "Camera Center" in line:
            parts = line.split("|")
            loss = float(parts[0].split("Loss:")[1].strip())
            center = float(parts[1].split("Camera Center")[1].strip())
            # 保留四位有效数字
            loss = float(f"{loss:.4g}")
            center = float(f"{center:.4g}")
            data.append({"Loss": loss, "Camera Center": center})
            

# 转换为 DataFrame
df = pd.DataFrame(data)

# 计算每个 Camera Center 的平均 Loss
grouped = df.groupby("Camera Center", as_index=False).mean()

# 保留四位有效数字
grouped["Loss"] = grouped["Loss"].apply(lambda x: float(f"{x:.4g}"))
grouped["Camera Center"] = grouped["Camera Center"].apply(lambda x: float(f"{x:.4g}"))

# 使用 Seaborn 绘制条形图
plt.figure(figsize=(10, 6))
sns.barplot(x="Camera Center", y="Loss", data=grouped, palette="Blues_d")
plt.title("Average Loss by Camera Center")
plt.xlabel("Camera Center Distance")
plt.ylabel("Average Loss")
plt.xticks(rotation=45)
plt.grid(axis="y")

# 保存图片
plt.savefig("loss_vs_camera_center_bar_4digits.png")
