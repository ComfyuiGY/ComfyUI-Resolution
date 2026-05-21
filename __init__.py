from .resolution_selector import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__version__ = "1.0.0"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]

# 注册JavaScript文件
WEB_DIRECTORY = "./web"

# 可选：如果需要在控制台看到提示
print("高级分辨率选择器插件已加载 - 支持联动功能")