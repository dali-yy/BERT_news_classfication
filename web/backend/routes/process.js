var express = require('express')
var router = express.Router()
const createError = require('http-errors')
var child_process = require('child_process')

/**
 * @abstract 调用新闻分类模型
 * @body 多条新闻：{ filename: 文件名, mode: 1 }
 *       单条新闻：{ title: 新闻标题, content: 新闻正文内容, mode: 0 }
 */
router.post('/cls', (req, res, next) => {
  let mode = req.body.mode
  let command = ''
  // 根据mode对应的不同模式（即多条新闻分类或单条新闻分类），拼接要执行的命令
  if (mode === 1) {
    let filename = req.body.filename
    command = ['python src/file_predict.py ', 'upload/', filename].join('')
  } else {
    let title = req.body.title
    let content = req.body.content
    command = ['python src/one_predict.py', content, title].join(' ')
  }
  console.log(command)
  // 执行模型调用命令，并根据回调返回对应结果
  child_process.exec(command, function (error, stdout, stderr) {
    if (error) {
      console.error('error: ' + error)
      let err = createError(500)
      next(err)
      return
    }
    // 多条新闻分类将结果直接标记在原文件上，因此只需要返回200状态码，通知前端发起下载即可
    if (mode === 1) {
      console.log('文件分析结束，新闻分类分析完成！')
      res.send(JSON.stringify({ code: 200, msg: '新闻分类分析完成！' }))
      // 单条新闻分类将结果输出到控制台，因此需要把stdout返回给前端
    } else {
      console.log('单条分析结束，新闻类别：', stdout)
      res.send(JSON.stringify({ code: 200, msg: stdout }))
    }
  })
})

module.exports = router
