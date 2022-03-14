var createError = require('http-errors')
var express = require('express')
var path = require('path')
var cookieParser = require('cookie-parser')
var logger = require('morgan')
var cors = require('cors')

var indexRouter = require('./routes/index')
var multerRouter = require('./routes/multer')
var processRouter = require('./routes/process')

var app = express()

// view engine setup
app.set('views', path.join(__dirname, 'views'))
app.use(express.static(path.join(__dirname, 'dist')))
app.set('view engine', 'ejs')

app.use(logger('dev'))
app.use(express.json())
app.use(express.urlencoded({ extended: false }))
app.use(cookieParser())
app.use(express.static(path.join(__dirname, 'public')))
app.use(cors())

app.use('/', indexRouter)
app.use('/multer', multerRouter)
app.use('/process', processRouter)

// catch 404 and forward to error handler
app.use(function (req, res, next) {
  next(createError(404))
})

// error handler
app.use(function (err, req, res, next) {
  console.log('next err', err)
  res.send({
    code: 500,
    msg: '新闻分类失败！您的新闻标题或正文内容中可能含有非法特殊字符！',
  })
})

module.exports = app
