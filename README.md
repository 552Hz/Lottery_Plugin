# 地下偶像抽签 AstrBot 插件

QQ 群里 `@机器人 /抽签` 后，返回一张地下偶像主题的每日运势图。

## 功能

- 每个 QQ 号每天的结果固定，以上海时区零点刷新。
- 运势随机为 `大吉`、`吉`、`中`、`凶`、`大凶`。
- 从 `吃ota饭`、`反切`、`关门`、`看活`、`规划远征`、`睡觉`、`喝酒`、`版聊` 中抽取 4 个，随机分到 `宜` 和 `忌`。
- 返回极简 PCIE 科技风图片，底图由代码生成，不依赖外部图片素材。

## 安装

把本目录放到 AstrBot 的 `data/plugins/` 下，确保插件目录里有：

- `main.py`
- `fortune_card.py`
- `metadata.yaml`
- `requirements.txt`
- `README.md`
- `.gitignore`
- `__init__.py`

AstrBot 会按 `requirements.txt` 安装 `Pillow`。

Windows Server 如果生成图片里的中文变成方框或乱码，请确认系统装有中文字体。插件会优先查找这些 Windows 字体：

- `C:/Windows/Fonts/msyh.ttc`，微软雅黑
- `C:/Windows/Fonts/simhei.ttf`，黑体
- `C:/Windows/Fonts/simsun.ttc`，宋体
- `C:/Windows/Fonts/Deng.ttf`，等线

如果服务器是精简版系统，可以安装中文语言包，或把可用的中文字体文件放进 `C:/Windows/Fonts/` 后重启 AstrBot。

## 使用

在群聊里发送：

```text
@机器人 /抽签
```

插件会生成并缓存当天图片，同一 QQ 号当天重复抽签会得到同一张图。
