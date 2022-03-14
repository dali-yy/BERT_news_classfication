/**
 * @abstract 调用新闻分类接口，对新闻文本进行分析。mode = 1：根据文件分类多条新闻；mode = 0：根据表单分类单条新闻
 * @param {用于分析的数据} data 多条新闻：{ filename: 文件名, mode: 1 }
 *                             单条新闻：{ title: 新闻标题, content: 新闻正文内容, mode: 0 }
 */
export function cls(data) {
  return fetch("http://localhost:3000/process/cls", {
    method: "post",
    body: JSON.stringify(data),
    headers: { "Content-Type": "application/json" }
  }).then(res => {
    return res.json();
  });
}

/**
 * @abstract 调用文件下载接口，下载的文件名即为上传时的文件名，下载的文件将包含已经标记好的新闻类别信息
 * @param {filename} filename 要下载的文件名
 */
export function download(filename) {
  window.location.href = `http://localhost:3000/multer/download?filename=${filename}`;
}
