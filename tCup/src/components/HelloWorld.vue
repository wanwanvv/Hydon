<template>
  <div height="100%">
    <el_container>
      <el-header height="142px">
        <el-menu :default-active="activeMenu"
                     router
                     @open="handleOpen"
                     @close="handleClose"
                  mode="horizontal"
                  background-color="#252525"
                  text-color="white"
                  active-text-color="#409EFF"
                  style="height: 80%">
          <el-menu-item class = "header-item" style="font-size:4vh;width: 23%">HAYDN数据运维软件</el-menu-item>
          <el-menu-item class = "header-item" style="width: 20%" index="/realtime">系统实时监测</el-menu-item>
          <el-menu-item class = "header-item" style="width: 20%" index="/prediction">系统指标预测</el-menu-item>
          <el-menu-item class = "header-item" style="width: 20%" index="/check">系统异常检测</el-menu-item>
          <el-menu-item class = "header-item" style="width: 17%;margin-bottom: 0%;height: 100%;">
            <img width="100%" src = "../assets/HUST.png"/>
          </el-menu-item>
        </el-menu>
      </el-header>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el_container>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  methods:{
    beginPre(){
      this.$message({
        message: '等待24秒将会出现预测结果',
        type: 'warning',
        duration:2000,
        showClose:true
      });
    }
  },
  computed: {
    activeMenu() {
      const route = this.$route
      const { meta, path } = route
      // if set path, the sidebar will highlight the path you set
      return meta.firstMenu
    }
  }
}
</script>

<style scoped>
  #system-title{
    padding-top:20px;

  }
  .el-container {
    padding: 0;
    margin: 0;
    height: 100%
  }
  .el-header {
    background-color: #252525;
    padding: 0 0 0 0;
  }
  .el-main {
    padding: 0;
    margin: 0;
    height: calc(100vh - 142px);
  }
  .el-menu {


  }
  .header-item{
    color: #eeeeee;
    font-size: 4vh;
    font-family: sans-serif;
    font-weight: 900;
    height: 100%;
    text-align: center;
    padding-top: 1.5%;
    padding-bottom: 1.5%;
  }

</style>
