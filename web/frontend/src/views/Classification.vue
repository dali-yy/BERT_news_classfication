<template>
  <el-container>
    <el-header>2021中国软件杯-A7-新闻文本分类算法</el-header>
    <div class="tab-wrap">
      <el-tabs v-model="activeName" @tab-click="handleSwitch">
        <el-tab-pane label="多条新闻分类" name="multi">
          <multicls />
        </el-tab-pane>
        <el-tab-pane label="单条新闻分类" name="single">
          <singlecls />
        </el-tab-pane>
      </el-tabs>
    </div>
  </el-container>
</template>

<script>
import Multicls from "./Multicls.vue";
import Singlecls from "./Singlecls.vue";

export default {
  data: () => ({
    activeName: "multi"
  }),
  components: {
    Multicls,
    Singlecls
  },
  methods: {
    /**
     * @abstract 切换模式：单条新闻分类或多条新闻分类
     * @param tab 选项卡对象
     * @param event 监听触发的事件
     */
    handleSwitch(tab, event) {
      console.log("切换：", tab.label);
    }
  }
};
</script>

<style>
body {
  margin: 0;
}
.el-header {
  background: #3282b8;
  margin-top: 0;
  margin-bottom: 1em;
  color: #eee;
  text-align: center;
  line-height: 60px;
  font-size: 20px;
  box-shadow: 0 0 3px 0 rgba(0, 0, 0, 0.2);
}
.tab-wrap {
  padding-left: 50px;
  padding-right: 50px;
}
</style>
