<template>
  <div>
    <el-container>
      <el-header height="2%" width="100%"></el-header>
      <el-main width="100%" height="100%">
        <div class="TopBox" id="graph1"></div>
        <div class="BottomBox_left" id="graph2"></div>
        <div class="BottomBox_right" id="graph3"></div>
      </el-main>
    </el-container>
  </div>
</template>

<script>
  import Vue from 'vue'

export default {
  name: 'cpu',
  data() {
    return {
      CPU_percent: [0,0,0,0,0,0,0,0],
      CPU_time: [0,0,0,0,0,0,0,0,0]
    }
  },
  methods:{
    myEcharts( myGraph, dataset){
      //this.cgsJg=echarts.init(this.$refs.cgsJ);(自己联系的项目中)
      var xid = [];
      var numSlice = 30;
      var lenSlice = 1;

      for( var i = 0; i < numSlice*lenSlice; i++) {
        xid.push(((numSlice*lenSlice-i)/lenSlice).toString()+'秒前');
      }
      xid.splice(numSlice*lenSlice-1,1,'现在');

        var option = {
          animation: false,
          grid: {
            x: 40,
            y: 50,
            x2: 40,
            y2: 30  //图表下方空白部分高度
          },
          title: {
            top: '5%',
            left: 'center',
            text: 'CPU利用率',
            textStyle: {
              color: '#FFF',
            },
          },
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              animation: false
            },
            appendToBody:true,
            formatter: function (params) {
              return params[0].name + "CPU的利用率："+params[0].value+"%";
            }
          },
          xAxis: [{
            show: true,
            type: 'category',
            boundaryGap: false,
            data: xid,
            axisLine: {
              lineStyle: {
                type: 'solid',
                color: '#eeeeee',//左边线的颜色
              }
            },
            axisLabel: {
              textStyle: {
                color: '#eeeeee',//坐标值得具体的颜色
              },
              interval: xid.length/5 - 1,
              showMaxLabel: true
            }
          }],
          yAxis: [{
            type: 'value',
            axisLine: {
              lineStyle: {
                type: 'solid',
                color: '#eeeeee',//左边线的颜色
              }
            },
            max:function (value){
              var curMax = value.max;
              //console.log(curMax);
              if (curMax <= 2){
                return 2;
              }else{
                return Math.ceil(curMax/5)*5;
              }
            },
            axisLabel: {
              textStyle: {
                color: '#eeeeee',//坐标值得具体的颜色
              },
              formatter:'{value}%',
              showMaxLabel: true
            }
          }],
          series: [
            {
              name: '实时值',
              type: 'line',
              showSymbol: false,
              data: dataset,
              color: '#409EFF',
              //areaStyle: {}
            }]
        }
      myGraph.setOption(option);

    },
    myGraph( myGraph){
      //let myGraph = this.$echarts.init(document.getElementById('graph2'));
      var option = {
        //animation: false,
        grid: {
          x: 40,
          y: 50,
          x2: 40,
          y2: 30,
          containLabel: true
        },
        tooltip: {
          show:true,
          formatter(params){
            return "CPU核心"+params.dataIndex+"的占用率为"+params.data+"%";
          },
          appendToBody: true
        },
        title: {
          top: '5%',
          left: 'center',
          text: 'CPU核心占用率',
          textStyle: {
            color: '#FFF',
          },
        },
        xAxis: {
          type: 'category',
          data: ['0', '1', '2', '3', '4', '5', '6','7'],
          axisLine: {
            lineStyle: {
              type: 'solid',
              color: '#eeeeee',//左边线的颜色
            }
          },
        },
        yAxis: {
          type: 'value',
          max:function (value){
            var curMax = value.max;
            //console.log(curMax);
            if (curMax <= 5){
              return 5;
            }else{
              return Math.ceil(curMax/5)*5;
            }
          },
          axisLabel:{formatter:'{value}%'},
          axisLine: {
            lineStyle: {
              type: 'solid',
              color: '#eeeeee',//左边线的颜色
            }
          },
        },
        series: [{
          //data: [0.0,18.2,17.3,20.8,22.1,20.6,19.8,40.5],
          data: this.CPU_percent,
          type: 'bar',
          color:'#fc765e',
          barWidth:30
        }]
      };
      // 使用刚指定的配置项和数据显示图表。
      myGraph.setOption(option);//})
    },
    myGraph2( myGraph){
      //var numset = [22842.16,411371.69,3675.74,8411371.69,434.33,393.8,402.95,0.0,0.0,0.0];
      var numset = [parseFloat(this.CPU_time.user)/10,  parseFloat(this.CPU_time.nice)/10,   parseFloat(this.CPU_time.system)/10,
                    parseFloat(this.CPU_time.idle)/10,    parseFloat(this.CPU_time.iowait)/10,   parseFloat(this.CPU_time.irq)/10,
                    parseFloat(this.CPU_time.softirq)/10,  parseFloat(this.CPU_time.steal)/10,  parseFloat(this.CPU_time.guest)/10]
      var numset_change = [];
      for (let i = 0;i<numset.length;i++){
        if (numset[i] === 0){
          numset_change.push(0);
        }else {
          numset_change.push(Math.log10(numset[i])+1);
        }
      }
      var option = {
        grid: {
          x: 50,
          y: 50,
          x2: 50,
          y2: 40,
        },
        tooltip: {
          show:true,
          formatter(params){
            //console.log(params);
            var names = ["用户态使用CPU总时间","根据优先级修正值分配给低优先级用户态使用的CPU总时间","系统态使用CPU总时间","CPU空闲总时间","CPU等待IO的总时间","CPU处理硬中断总时间","CPU处理软中断总时间","虚拟机运行模式下，其它虚拟机占用CPU总时间","CPU虚拟化运行总时间"];
            return names[params.dataIndex]+": "+numset[params.dataIndex]+"秒";
          },
          appendToBody:true
        },
        title: {
          top: '5%',
          left: 'center',
          text: 'CPU使用时间',
          textStyle: {
            color: '#FFF',
          },
        },
        xAxis: {
          type: 'category',
          data: ['user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq','steal','guest'],
          axisLabel:{
            show:true,
            interval:0,
            rotate:45
          },
          axisLine: {
            lineStyle: {
              type: 'solid',
              color: '#eeeeee',//左边线的颜色
            }
          },
        },
        yAxis: {
          type: 'value',
          axisLabel:{
            formatter:function (value){
              var texts = [];
              if (value === 0){
                texts.push(0+"s");
              }else{
                texts.push("10^"+(value-1)+"s");
              }
              return texts;
            }
          },
          axisLine: {
            lineStyle: {
              type: 'solid',
              color: '#eeeeee',//左边线的颜色
            }
          },
        },
        series: [{
          name: 'cpu use time',
          data: numset_change,
          type: 'bar',
          color:'#aa88f8',
          barWidth:30
        }]
      };
      // 使用刚指定的配置项和数据显示图表。
      myGraph.setOption(option);//})
    },
    getData() {
      let percentGraph = this.$echarts.init(document.getElementById('graph2'));
      let timeGraph = this.$echarts.init(document.getElementById('graph3'));
      let lineGraph = this.$echarts.init(document.getElementById('graph1'));
      let _this = this;

      //async function


      var numset1 = [];
      var numSlice = 30;
      var lenSlice = 1;
      for( var i = 0; i < numSlice*lenSlice; i++) numset1.push(0);

      const CancelToken = this.$axios.CancelToken

      async function chartsInit() {
        await _this.$axios.get('api/monitor/status',{
          cancelToken: new CancelToken(function executor (c) {
            Vue.$httpRequestList.push(c)
          })
        }).then((res) => {
            //console.log('running cpu...');
            _this.CPU_percent = res.data.cpu_data.cpu_percent;
            _this.CPU_percent.forEach((item,index) =>{
              _this.CPU_percent[index] = parseFloat(_this.CPU_percent[index])
            })
            _this.CPU_time = res.data.cpu_data.cpu_time;
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
        //console.log(_this.CPU_time);

        for( var i = 0; i < lenSlice; i++) {
          var avg = 0;
          for( var i = 0; i < 8; i++) avg += _this.CPU_percent[i];
          avg /= 8;
          numset1.push(parseFloat(avg.toFixed(3)));
          //console.log(ii);
        }
        numset1.splice(0,lenSlice);

        _this.myEcharts( lineGraph, numset1);
        _this.myGraph( percentGraph);
        _this.myGraph2( timeGraph);
      }
      chartsInit();

      this.timer = setInterval( function() {
        chartsInit();
      },1000)

      window.onresize = function(){
        lineGraph.resize();
        percentGraph.resize();
        timeGraph.resize();
      }
    }
  },
  mounted() {
    this.getData();
  },
  beforeDestroy() {
    if (this.timer) {
      clearInterval(this.timer); // 在Vue实例销毁前，清除我们的定时器
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
.TopBox {
  width: 90%;
  margin-right: 1%;
  margin-top: 1%;
  height: 45%;
  border: 1px solid rgb(68,68,68);
  border-radius: 10px;
  box-shadow: 0 2px 5px black
}
.BottomBox_left{
  float: left;
  width: 40%;
  margin-right: 1%;
  margin-top: 2%;
  height: 45%;

  border: 1px solid rgb(68,68,68);
  border-radius: 10px;
  box-shadow: 0 2px 5px black
}
.BottomBox_right{
  float: right;
  width: 45%;
  margin-right: 10%;
  margin-top: 2%;
  height: 45%;

  border: 1px solid rgb(68,68,68);
  border-radius: 10px;
  box-shadow: 0 2px 5px black
}
</style>
