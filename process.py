import subprocess

def compress_mp4(input_path, output_path, crf=28, scale=None):
    """
    使用 FFmpeg 压缩视频
    :param input_path: 输入视频
    :param output_path: 输出视频
    :param crf: 压缩质量（越大越小，推荐 24~30）
    :param scale: (width, height) 例如 (1280, -1)
    """
    cmd = ["ffmpeg", "-i", input_path]

    # 降低分辨率
    if scale is not None:
        cmd += ["-vf", f"scale={scale[0]}:{scale[1]}"]

    # 使用 h264 编码 + CRF 压缩
    cmd += [
        "-vcodec", "libx264",
        "-crf", str(crf),
        "-preset", "medium",
        output_path,
        "-y"   # 覆盖文件
    ]

    print("Running:", " ".join(cmd))
    subprocess.run(cmd, check=True)

# 使用示例：
compress_mp4("projects/LightMotion/static/videos/ours/output1.mp4", "output1.mp4", crf=30, scale=(1280, -1))
