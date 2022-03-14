var express = require('express')
var router = express.Router()

const multer = require('multer')
const fs = require('fs')

/**
 * @abstract 单个文件上传，文件保存至 backend/upload 目录下
 * @file 上传的文件对象
 */
router.post(
  '/upload',
  multer({
    dest: 'upload',
  }).single('file', 10),
  (req, res) => {
    const file = req.file
    console.log(file)
    fs.rename(file.path, `upload/${file.originalname}`, (err) => {
      if (err) {
        console.log(err)
      }
      console.log('文件保存完成!')
    })
    res.send(file)
  }
)

/**
 * @abstract 单个文件下载
 * @query filename 要下载的文件名，实际上对应的就是上传的用于分析的文件名
 */
router.get('/download', (req, res) => {
  res.download(`upload/${req.query.filename}`)
})

module.exports = router
