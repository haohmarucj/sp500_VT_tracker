# 动态定投助手(自动行情版)
1. 新建 GitHub 仓库,上传本目录全部文件(含 .github 文件夹)。
2. Settings → Pages → Source 选 Deploy from branch,分支 main,目录 / (root)。
3. Actions 页面手动运行一次 update-data(Run workflow),生成 data.json。
4. 访问 https://<用户名>.github.io/<仓库名>/ 即可。
标的代码在 fetch_data.py 顶部修改。
