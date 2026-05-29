# TaskPin Plugins

[TaskPin](https://github.com/bestK/taskpin) official plugin repository.

[TaskPin](https://github.com/bestK/taskpin) 官方插件仓库。

---

## Usage / 使用方式

1. Open TaskPin management window, click **Market** / 打开 TaskPin 管理窗口，点击 **Market**
2. This repo `bestK/taskpin-plugins` is loaded as default source / 本仓库已作为默认源自动加载
3. Select a script, click **Download** / 选择脚本，点击 **Download** 即可使用

## Scripts / 脚本列表

| File | Description |
|------|-------------|
| `example.lua` | Getting started: HTTP + JSON + params / 入门示例 |
| `newapi_balance.lua` | AI API balance display / AI API 余额查询 |
| `rich_text_demo.lua` | Rich text demo: colors, alignment / 富文本演示 |
| `zentao_task.lua` | Zentao task monitor / 禅道任务监控 |
| `oracle_sessions.lua` | Oracle session monitor / Oracle 会话监控 |
| `system_monitor.lua` | System monitor: CPU + MEM + Net / 系统监控 |
| `net_monitor.lua` | Network process monitor / 网络进程监控 |
| `claude_status.lua` | Claude Code real-time status / Claude Code 状态指示器 |

## Contributing / 贡献脚本

1. Fork this repo / Fork 本仓库
2. Add your `.lua` script / 添加你的脚本
3. Add an entry to `manifest.json` / 在 manifest.json 中添加条目
4. Submit a PR / 提交 PR

### manifest.json format

```json
{
  "scripts": [
    {
      "name": "script_name",
      "file": "filename.lua",
      "description": "Short description",
      "author": "author",
      "version": "1.0"
    }
  ]
}
```

---

## Lua Script API Reference / Lua 脚本 API 参考

Full documentation: [English](https://github.com/bestK/taskpin/blob/master/docs/LUA_API_EN.md) | [中文](https://github.com/bestK/taskpin/blob/master/docs/LUA_API.md)

### Quick Reference / 速查

#### Return Values / 返回值

```lua
-- Return 1: display text (string or font() span)
-- Return 2: clickable flag (boolean, optional)
-- Return 3: click URL or dialog() spec (optional)
return font("Hello", "#0F0", 9), true, "https://example.com"
```

#### font(text, color, size, align)

Rich text span with custom color, size, alignment. Use `..` to concatenate.

```lua
return font("CPU:", "#888", 8) .. font("45%", "#FF0000", 14)
return font("Left", "#FFF", 9) .. font("Right", "#888", 9, "right")
```

#### icon(source, width, height, align)

Image span. Supports PNG, animated GIF, base64 data URI.

```lua
return icon("logo.png", 16, 16) .. font(" Status", "#FFF", 9)
```

#### dialog(spec)

Popup dialog on click. Used as 3rd return value.

```lua
local info = dialog({
    title = "Status", width = 320, height = 200, refresh = 5,
    content = {
        { type = "text", value = "Title", color = "#FF8800", size = 12, bold = true },
        { type = "hr" },
        { type = "text", value = "Content", color = "#CCC", size = 10 },
        { type = "table", columns = {"Name", "Value"}, rows = {{"CPU", "45%"}} },
    }
})
return font("OK", "#0F0", 9), true, info
```

#### json.decode(str)

Parse JSON string to Lua table.

#### http.get(url) / http.post(url, body, headers)

Synchronous HTTP requests. Returns response body string or nil.

#### sys.*

| Function | Returns |
|----------|---------|
| `sys.cpu()` | CPU usage 0-100 |
| `sys.memory()` | `{total_mb, used_mb, percent}` |
| `sys.disk(drive)` | `{total_gb, free_gb, percent}` |
| `sys.battery()` | `{percent, charging, seconds_left}` |
| `sys.uptime()` | Seconds since boot |
| `sys.process_count()` | Number of processes |
| `sys.net()` | `{recv_bytes, send_bytes}` |
| `sys.net_speed()` | `{download, upload}` bytes/sec |
| `sys.net_processes()` | Array of `{pid, name, connections, download, upload}` |
| `sys.file_mtime(path)` | Unix timestamp or nil |
| `sys.find_newest(dir, ext)` | Path of newest matching file or nil |

#### Script Header Declarations / 脚本头部声明

```lua
-- @param api_key string API Key
-- @param port number Port number
-- @refresh 3000
```

- `@param` declares UI input fields / 声明参数输入框
- `@refresh` sets refresh interval in ms (min 1000) / 设置刷新间隔

---

## License

MIT
