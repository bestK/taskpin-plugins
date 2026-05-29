# TaskPin Plugins

[TaskPin](https://github.com/bestK/taskpin) 官方插件仓库。

## 使用方式

1. 打开 TaskPin 管理窗口，点击 **Market**
2. 本仓库 `bestK/taskpin-plugins` 已作为默认源自动加载
3. 选择脚本，点击 **Download** 即可使用

## 脚本列表

| 文件 | 说明 |
|------|------|
| `example.lua` | 入门示例：HTTP 请求 + JSON 解析 + 参数声明 |
| `newapi_balance.lua` | 查询 AI API 账户余额并显示在任务栏 |
| `rich_text_demo.lua` | font() 富文本演示：多色、多行、左右对齐 |
| `zentao_task.lua` | 禅道项目管理：显示待办任务数，点击查看详情 |
| `oracle_sessions.lua` | Oracle 数据库会话监控，多实例支持，颜色预警 |
| `system_monitor.lua` | 系统监控：网速 + CPU + 内存，纯 sys.* API |
| `net_monitor.lua` | 网络进程监控：显示有活跃连接的进程及流量 |
| `claude_status.lua` | Claude Code 实时状态指示器 |

## 贡献脚本

1. Fork 本仓库
2. 添加你的 `.lua` 脚本
3. 在 `manifest.json` 中添加条目
4. 提交 PR

## manifest.json 格式

```json
{
  "scripts": [
    {
      "name": "脚本名",
      "file": "文件名.lua",
      "description": "简短描述",
      "author": "作者",
      "version": "1.0"
    }
  ]
}
```

## License

MIT
