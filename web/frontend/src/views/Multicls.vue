<template>
  <div>
    <el-row :gutter="20" type="flex" align="middle">
      <el-col :span="11"
        ><div class="translate-button">
          <el-button icon="el-icon-info" circle @click="info()"></el-button>
          <el-button
            type="primary"
            icon="el-icon-edit"
            plain
            @click="handleSubmit"
            :disabled="isDisabled"
            >开始识别</el-button
          >
        </div>
      </el-col>
      <el-col :span="11">
        <el-alert
          title="提交的含有多条新闻的表格文件格式样例："
          description="文件的第一行为表头，第二行起才是待分析的数据。“编号”是新闻条目的编号；“chanelName”上传时应放空，分析结束后会在该栏填入对应的分类结果；“title”是新闻的标题；“content”是新闻的正文内容。"
          type="info"
          :closable="false"
        >
        </el-alert>
      </el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="11">
        <el-upload
          class="upload-demo"
          ref="upload"
          drag
          action="http://127.0.0.1:3000/multer/upload"
          :file-list="fileList"
          :multiple="false"
          :before-upload="handleBeforeUpload"
          :on-success="handleSuccess"
          :on-error="handleError"
          :on-change="handleChange"
          :auto-upload="false"
          :disabled="isDisabled"
        >
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">
            将.xlsx/.csv文件拖到此处，或<em>点击上传</em>
          </div>
        </el-upload>
        <transition name="el-fade-in-linear">
          <div v-show="show" class="transition-box">
            <el-progress
              :text-inside="true"
              :stroke-width="26"
              :percentage="percent"
            ></el-progress>
            <div id="progress-bar">{{ processMsg }}</div>
          </div>
        </transition></el-col
      >
      <el-col :span="11">
        <el-table :data="tableData" border style="width: 100%">
          <el-table-column prop="no" label="编号" width="50"> </el-table-column>
          <el-table-column prop="channelName" label="channelName" width="120">
          </el-table-column>
          <el-table-column
            prop="title"
            label="title"
            :show-overflow-tooltip="true"
          >
          </el-table-column>
          <el-table-column
            prop="content"
            label="content"
            :show-overflow-tooltip="true"
          >
          </el-table-column> </el-table
      ></el-col>
    </el-row>
  </div>
</template>

<script>
import { cls, download } from "@/api/apis";

export default {
  name: "Multicls",
  data: () => ({
    fileList: [],
    percent: 0,
    processMsg: "正在上传的新闻文件格式...",
    isDisabled: false,
    show: false,
    tableData: [
      {
        no: 1,
        channelName: "",
        title: "空军航空兵某旅组织青年飞行员开展现地教学活动",
        content:
          "“常香玉老前辈，我们是人民空军飞行员。今天来这里参观学习，特意带来了一架歼-20战斗机模型，向您报告！”近日，空军航空兵某旅组织歼-20试飞员李刚等一批青年飞行员，走进驻地某博物馆寻初心、话传承	博物馆的醒目位置，悬挂着“人民艺术家”、著名豫剧表演艺术家常香玉的两幅挂像。其中一幅的画面中，常香玉手捧一架米格-15战斗机模型。据介绍，这一米格-15战斗机模型，是由一级战斗英雄王海在抗美援朝作战中击落敌机的残骸制作而成，由空军部队赠予常香玉，表达对她当年为志愿军空军捐献战斗机的感激之情。	飞行员们被军民鱼水情深深打动。在常香玉的挂像前，青年飞行员刘洪江代表战友们深情告白：“新时代的人民空军，已经装备了国产新一代隐身战斗机歼-20。您当年为志愿军空军捐献米格-15战斗机的事迹，人民空军一代代飞行员铭记不忘。我们一定刻苦训练、建功蓝天、保卫祖国！”	“谢谢您，老前辈！”牛年春节，在抗美援朝战场击落击伤9架敌机的王海老英雄，当选“感动中国2020年度人物”。人们在整理历史资料时，发现了常香玉到前线慰问参战官兵和战斗英雄时所拍的两张珍贵照片，一张是王海和战友们与常香玉的合影，一张是常香玉手捧米格-15战斗机模型的照片。	常香玉的义举，让现场的飞行员们由衷敬佩。大家纷纷表示，要不负老司令员王海的期望，不负人民群众的深情厚爱。	党史学习教育开展以来，该旅把学习教育成果转化为工作动力，飞行员们苦练精飞，多次圆满完成重大战训任务，部队战斗力稳步提升。（申进科）(责编：陈羽、任佳晖)分享让更多人看到"
      },
      {
        no: 2,
        channelName: "",
        title: "钢铁板块年内涨超26% 多股上半年业绩亮眼",
        content:
          "今年以来，我国经济运行持续稳定恢复，钢材市场产销两旺，钢铁企业盈利明显好转。截至目前，A股钢铁板块36家上市公司已有9家发布2021年半年度业绩预告，其中8家实现预增。二级市场表现方面，上半年钢铁板块在28个申万一级行业中涨幅居前，截至6月25日收盘，钢铁板块年内涨幅达26.59%。　　6月26日，南钢股份发布业绩预增公告，预计2021年上半年实现归属于上市公司股东的净利润约为22.61亿元，同比增长约102.67%。此外，鞍钢股份预计上半年实现净利润48亿元左右，同比增长幅度为860%左右；沙钢股份预计上半年实现净利润3.6亿至5.4亿元，同比增长幅度为42.69%至114.04%；中信特钢预计上半年实现归属于上市公司股东的净利润为盈利41.3亿至42.3亿元，同比增长50.24%至53.87%。　　机构分析，今年以来，受益于下游地产、基建开工率提升，需求驱动钢铁类上市公司产销量出现较大幅度的增长。此外，供需两旺背景下，钢铁价格持续位于高位，吨钢利润处于较高水平。不过，6月中旬以来，国内钢材现货市场出现持续的震荡下跌行情。兰格钢铁网数据显示，截至6月24日，全国三级螺纹钢现货均价4880元/吨，较6月中旬下跌242元/吨；全国热轧卷板现货均价5340元/吨，较6月中旬下跌212元/吨。　　近日，中钢协副会长骆铁军表示，当前钢材市场下游需求呈现出新变化，但综合而言，今年的钢材消费总体呈增长态势，需求偏乐观。　　深港证券认为，钢铁行业需求端偏弱迹象显现，后续货币趋稳以及投资端回落或影响淡季钢材消费表现。此外，近期钢企陆续披露中报业绩，关注板材占比较高的钢企业绩持续超预期的可能性。（记者 高伟）"
      },
      {
        no: "...",
        channelName: "",
        title: "...",
        content: "..."
      }
    ]
  }),
  methods: {
    /**
     * @abstract 上传文件前类型检查，仅接受.xlsx和.csv的文件
     * @param file element-ui uplaod 组件的文件对象
     */
    handleBeforeUpload(file) {
      let format = file.name
        .substring(file.name.lastIndexOf(".") + 1)
        .toLowerCase();
      if (["xlsx", "csv"].indexOf(format) === -1) {
        this.$message.error("请上传正确格式的新闻文件！");
        this.$notify({
          title: "支持的文件格式",
          message: "xlsx、csv",
          position: "bottom-left",
          duration: 0
        });
        this.resetFileListAndShow();
        return false;
      } else if (/\s/.test(file.name)) {
        this.$message.error("文件名不能含有空格和中文括号！");
        this.resetFileListAndShow();
        return false;
      }
      // 通过格式检查后再展示进度条
      this.show = true;
      return true;
    },

    /**
     * @abstract 点击“开始识别”按钮后的回调，发起文件上传和后续操作
     */
    handleSubmit() {
      if (this.fileList.length === 0) {
        this.$message.error("尚未上传新闻文件，无法进行分类！");
        return false;
      }
      console.log("开始上传", this.fileList[0]);
      this.percent = 0;
      this.isDisabled = true;
      this.$refs.upload.submit();
    },

    /**
     * @abstract 新闻文件上传成功后的执行的回调，调用分析脚本对新闻进行分类
     * @param file element-ui uplaod 组件的文件对象
     */
    handleSuccess(file) {
      this.percent = 20;
      this.processMsg = "正在对数据进行分析（可能耗时较长，请稍后）...";
      // 设置虚拟进度，每秒触发一次
      let timer = setInterval(() => {
        this.virtualIncrease();
      }, 1000);
      cls({ filename: file.originalname, mode: 1 }).then(res => {
        if (res.code === 200) {
          this.percent = 100;
          this.processMsg = "分析完成，即将下载结果文件！";
          download(file.originalname);
        } else {
          this.$message.error("数据分析失败！");
        }
        clearTimeout(timer);
        this.resetFileListAndShow();
      });
    },

    /**
     * @abstract 上传失败的回调
     * @param res 后台返回的错误信息
     * @param file element-ui uplaod 组件的文件对象
     */
    handleError(res, file) {
      console.log("上传失败：", res);
      this.$message.error("上传失败！");
      this.resetFileListAndShow();
    },

    /**
     * @abstract 文件列表更新的回调
     * @param file element-ui uplaod 组件的文件对象
     * @param fileList element-ui uplaod 组件的绑定的文件列表
     */
    handleChange(file, fileList) {
      this.fileList = fileList.slice(-1);
      console.log("添加文件：", this.fileList[0]);
    },

    /**
     * @abstract 重置多条新闻分析的数据状态和显示状态
     */
    resetFileListAndShow() {
      this.isDisabled = false;
      this.fileList = [];
      setTimeout(() => {
        this.show = false;
      }, 5000);
    },

    /**
     * @abstract 由于后台模型判断一气呵成，可能存在需要判断的新闻条目较多的情况，故设置进度条虚拟进度计数器器
     *           每秒增长2%，到80%后每秒增长1%，到95%后每秒增长0.5%，直至99.5%停下
     */
    virtualIncrease() {
      if (this.percent < 80) {
        this.percent += 2;
      } else if (this.percent < 95) {
        this.percent += 1;
      } else if (this.percent < 99.5) {
        this.percent += 0.5;
      }
    },

    /**
     * @abstract 多条新闻分类-页面左下角的使用说明信息
     */
    info() {
      this.$notify({
        title: "使用方法",
        dangerouslyUseHTMLString: true,
        message:
          "<p>1、将文件拖拽到上传按钮位置，或直接点击上传按钮，上传含有新闻信息的.xlsx或.csv文件。</br>\
          2、点击左上方的“开始识别”按钮，稍等片刻，后台将分析文件并给出新闻分类结果，将结果保存在原文件中。</br>\
          3、新闻分类完成后将自动下载标记了新闻类别的文件。</br>\
          4、进度条将展示后台的实时进度。</p>",
        position: "bottom-left",
        duration: 0
      });
    }
  }
};
</script>

<style>
.translate-button {
  margin-bottom: 1em;
}
.upload-demo {
  text-align: center;
  height: 100%;
  width: 100%;
}
.el-upload {
  display: block;
  width: 100%;
  height: 192px;
}
.el-upload-dragger {
  width: 100%;
  height: 100%;
}
.el-dropdown-link {
  cursor: pointer;
  color: #409eff;
}
.el-icon-arrow-down {
  font-size: 12px;
}
#progress-bar {
  font-size: 12px;
  color: #606266;
}
</style>
