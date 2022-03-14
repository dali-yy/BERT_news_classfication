<template>
  <el-form
    ref="form"
    :model="form"
    :rules="rules"
    label-width="80px"
    v-loading="singleLoading"
  >
    <el-row :gutter="20">
      <el-col :span="16">
        <el-form-item label="新闻标题" prop="title">
          <el-input v-model="form.title"></el-input> </el-form-item
      ></el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="16">
        <el-form-item label="新闻内容" prop="content">
          <el-input
            type="textarea"
            v-model="form.content"
            :rows="15"
          ></el-input> </el-form-item
      ></el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="4">
        <el-form-item label="分类结果">
          <el-tag>{{ form.result }}</el-tag>
        </el-form-item></el-col
      >
    </el-row>
    <el-row :gutter="20">
      <el-col :span="11">
        <el-form-item>
          <el-button type="primary" @click="submitForm">开始分析</el-button>
          <el-button @click="resetForm">重置</el-button>
        </el-form-item></el-col
      >
    </el-row>
  </el-form>
</template>

<script>
import { cls } from "@/api/apis";

export default {
  name: "Singlecls",
  data: () => ({
    singleLoading: false,
    form: {
      title: "",
      content: "",
      result: "待分析"
    },
    rules: {
      title: [{ required: true, message: "请输入新闻标题", trigger: "blur" }],
      content: [
        { required: true, message: "请选输入新闻正文内容", trigger: "blur" }
      ]
    },
    categories: {
      0: "财经",
      1: "房产",
      2: "教育",
      3: "科技",
      4: "军事",
      5: "汽车",
      6: "体育",
      7: "游戏",
      8: "娱乐",
      9: "其他"
    }
  }),
  methods: {
    /**
     * @abstract 单条新闻分类-提交表单
     */
    submitForm() {
      this.$refs["form"].validate(valid => {
        if (valid) {
          this.singleLoading = true;
          console.log("开始分析单条新闻...");
          this.$message("新闻类别正在分析中，请稍后...");
          // 提交表单交给后台模型分析时，应先去除所有的空格、回车和换行，避免调用模型传参时受影响
          cls({
            title: this.form.title.replace(
              /[~`!@#$%^&*()\-\+\s\|\[\]\/{}<>\\.]/g,
              ""
            ),
            content: this.form.content.replace(
              /[~`!@#$%^&*()\-\+\s\|\[\]\/{}<>\\.]/g,
              ""
            ),
            mode: 0
          }).then(res => {
            console.log(res);
            if (res.code === 200) {
              this.$message({
                message: "新闻分类成功！",
                type: "success"
              });
              this.form.result = this.categories[res.msg];
              this.singleLoading = false;
            } else {
              this.$message({
                message:
                  "新闻分类失败！您的新闻标题或正文内容中可能含有非法特殊字符！",
                type: "error",
                duration: 2000
              });
              setTimeout(() => {
                this.singleLoading = false;
                this.form.result = "待分析";
              }, 1500);
            }
          });
        }
      });
    },

    /**
     * @abstract 重置单条新闻分类的表单
     */
    resetForm() {
      this.form.title = "";
      this.form.content = "";
      this.form.result = "待分析";
    }
  }
};
</script>

<style></style>
