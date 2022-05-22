<template>
  <div>
    <el-container style="background-color: #252525">
      <el-aside width = 20%>
        <el-button class = "button" @click="toMainPage" style="margin-top: 20%;margin-left: 25%;width: 50%;background-color:#252525;" autofocus>概览</el-button>
        <el-button class = "button" @click="toCPU" style="margin-top: 20%;margin-left: 25%;width: 50%;background-color:#252525">CPU利用率</el-button>
        <el-button class = "button" @click="toMemory" style="margin-top: 20%;margin-left: 25%;width: 50%;background-color:#252525;">内存占用率</el-button>
        <el-button class = "button" @click="toDisk" style="margin-top: 20%;margin-left: 25%;width: 50%;background-color:#252525;">磁盘占用率</el-button>
        <el-button class = "button" @click="toNetwork" style="margin-top: 20%;margin-left: 25%;width: 50%;background-color:#252525;">以太网</el-button>
<!--        <el-button class = "button" style="margin-top: 10%;margin-left: 25%;width: 50%;background-color:#252525;">网络IO时间</el-button>-->
<!--        <el-button class = "button" style="margin-top: 10%;margin-left: 25%;width: 50%;background-color:#252525;">GPU利用率</el-button>-->
<!--        <el-button class = "button" style="margin-top: 10%;margin-left: 25%;width: 50%;background-color:#252525;">指标6</el-button>-->
      </el-aside>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </div>
</template>

<script>
  export default {
    name: 'RealTime',
    methods:{
      toCPU(){
        window.location.href = '/#/realTime/cpu'
      },
      toMainPage(){
        window.location.href = '/#/realTime/mainPage'
      },
      toMemory(){
        window.location.href = '/#/realTime/memory'
      },
      toDisk(){
        window.location.href = '/#/realTime/disk'
      },
      toNetwork(){
        window.location.href = '/#/realTime/network'
      }

    }
  }
</script>

<style scoped>
  .el-container {
    padding: 0;
    margin: 0;
    height: calc(100vh - 142px);
  }
  .el-aside {
    padding: 0;
    margin: 0;
    color: #333;
    height: 100%;
  }
  .el-main {
    padding: 0;
    margin: 0;
    height: 100%;
    width: 100%
  }
  .LeftBox {
    width: 48%;
    float: left;
    margin-right: 1%;
    margin-top: 0%;
    margin-bottom: 1%;
    height: 31%;
    border: #333333;
    border-radius: 10px;
    box-shadow: 0 2px 5px black
  }
  .RightBox{
    width: 48%;
    float: right;
    margin-right: 1%;
    margin-top: 0%;
    margin-bottom: 1%;
    height: 31%;

    border: #333333;
    border-radius: 10px;
    box-shadow: 0 2px 5px black
  }
  .button{
    color: #eeeeee;
    border: #333333;
    border-radius: 10px;
    box-shadow: 0 2px 5px black;
    font-size: 2.3vh;
  }
  .el-button:focus, .el-button:hover {
    color: #409eff;
  }
</style>
