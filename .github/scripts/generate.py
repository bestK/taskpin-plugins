#!/usr/bin/env python3
"""Scan .lua files, update manifest.json and README.md with script table + install buttons."""

import os
import json
import re

REPO = "bestK/taskpin-plugins"
BRANCH = "master"
RAW_BASE = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}"
PAGES_BASE = "https://bestk.github.io/taskpin-plugins"

IGNORED_FILES = {"goose_sprites.png", "claude.png", "claude_spinner.gif"}


def parse_lua_metadata(filepath):
    meta = {"file": os.path.basename(filepath), "name": "", "description": "", "author": "bestK", "version": "1.0"}
    first_comment_desc = ""
    first_line = True

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            stripped = line.strip()
            if not stripped.startswith("--"):
                break
            content = stripped[2:].strip()

            if first_line:
                first_line = False
                # "file.lua - Description" pattern
                m = re.match(r"[\w.]+\s*-\s*(.+)", content)
                if m:
                    first_comment_desc = m.group(1).strip()

            if content.startswith("@name"):
                meta["name"] = content[5:].strip()
            elif content.startswith("@version"):
                meta["version"] = content[8:].strip()
            elif content.startswith("@param") or content.startswith("@refresh") or content.startswith("@bar_width") or content.startswith("@require"):
                pass
            elif not meta["description"] and not content.startswith("@") and content and not re.match(r"[\w.]+\.lua", content):
                # Use first non-directive comment as description
                if " - " in content:
                    meta["description"] = content.split(" - ", 1)[1].strip()
                elif first_comment_desc:
                    pass  # will use first_comment_desc below

    if not meta["name"]:
        meta["name"] = os.path.splitext(meta["file"])[0]
    if not meta["description"] and first_comment_desc:
        meta["description"] = first_comment_desc

    return meta


def main():
    scripts = []
    for f in sorted(os.listdir(".")):
        if f.endswith(".lua"):
            meta = parse_lua_metadata(f)
            scripts.append(meta)

    # Write manifest.json
    manifest = {"scripts": scripts}
    with open("manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
        f.write("\n")

    # Generate README.md
    readme = f"""# TaskPin Plugins

[TaskPin](https://github.com/bestK/taskpin) official plugin repository.

[TaskPin](https://github.com/bestK/taskpin) 官方插件仓库。

---

## Scripts / 脚本列表

| Name | Description | Version | Install |
|------|-------------|---------|---------|
"""
    for s in scripts:
        raw_url = f"{RAW_BASE}/{s['file']}"
        install_url = f"{PAGES_BASE}/install.html?url={raw_url}"
        badge = f"[![Install](https://img.shields.io/badge/TaskPin-Install-blue)]({install_url})"
        readme += f"| {s['name']} | {s['description']} | {s['version']} | {badge} |\n"

    readme += f"""
---

## Usage / 使用方式

1. Click the **Install** button above / 点击上方 **Install** 按钮一键安装
2. Or open TaskPin → **Market** → Download / 或打开 TaskPin → **Market** → 下载

## Contributing / 贡献脚本

1. Fork this repo / Fork 本仓库
2. Add your `.lua` script / 添加你的脚本
3. Submit a PR / 提交 PR (manifest.json and README are auto-generated)

### Script header format / 脚本头部格式

```lua
-- script_name.lua - Short description
-- @name Display Name
-- @version 1.0
-- @refresh 3000
-- @param key type Description
```

---

## Lua Script API Reference / Lua 脚本 API 参考

Full documentation: [English](https://github.com/bestK/taskpin/blob/master/docs/LUA_API_EN.md) | [中文](https://github.com/bestK/taskpin/blob/master/docs/LUA_API.md)

---

## License

MIT
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme)

    print(f"Generated manifest with {len(scripts)} scripts")


if __name__ == "__main__":
    main()
