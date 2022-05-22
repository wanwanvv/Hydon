<template>
  <div>
    <el-container>
      <el-header height="2%"></el-header>
      <el-main>
        <div class="LeftBox" id="graph1"></div>
        <div class="RightBox" id="graph2"></div>
        <div class="LeftBox" id="graph3"></div>
        <div class="RightBox" id="graph4"></div>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import Vue from "vue";

export default {
  name: 'mainPage',
  data() {
    return {
      CPU_percent: [0,0,0,0,0,0,0,0],
      DISK_percent: 0,
      MEMORY_percent: 0,
      NET_recv: 0,
      NET_sent: 0
    }
  },
  methods: {
    myGraph1(myGraph, dataset) {
      //this.cgsJg=echarts.init(this.$refs.cgsJ);(自己联系的项目中)
      var xid = [];
      var numSlice = 30;
      var lenSlice = 1;

      for (var i = 0; i < numSlice * lenSlice; i++) {
        xid.push(((numSlice * lenSlice - i) / lenSlice).toString() + '秒前');
      }
      xid.splice(numSlice * lenSlice - 1, 1, '现在');

      var option = {
        animation: false,
        grid: {
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
            interval: xid.length / 5 - 1,
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
          axisLabel: {
            textStyle: {
              color: '#eeeeee',//坐标值得具体的颜色
            },
            formatter:'{value}%'
          },
          max:function (value){
            var curMax = value.max;
            if (curMax <= 3){
              return 3;
            }else{
              return Math.ceil(curMax/5)*5;
            }
          },
        }],
        series: [
          {
            name: 'CPU利用率',
            type: 'line',
            showSymbol: false,
            data: dataset,
            color: '#409EFF',
            //areaStyle: {}
          }]
      }
      myGraph.setOption(option);
    },
    myGraph2(myChart_R1, numset2) {
      var xid = [];
      var numSlice = 30;
      var lenSlice = 1;

      for (var i = 0; i < numSlice * lenSlice; i++) {
        xid.push(((numSlice * lenSlice - i) / lenSlice).toString() + '秒前');
      }
      xid.splice(numSlice * lenSlice - 1, 1, '现在');

      function showOption(dataset, title) {
        var option = {
          color: '#409EFF',
          animation: false,
          grid: {
            y2: 30  //图表下方空白部分高度
          },
          title: {
            top: '5%',
            left: 'center',
            text: title,
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
              return params[0].name + "磁盘的占用率："+params[0].value+"%";
            }
          },
          xAxis: [{
            // show: false,
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
              interval: xid.length / 5 - 1,
              showMaxLabel: true
            }
          }],
          yAxis: [{
            max:100,
            type: 'value',
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
              formatter:'{value}%'
            }
          }],
          series: [
            {
              name: title,
              type: 'line',
              showSymbol: false,
              data: dataset,
            }]
        };
        return option
      }
      myChart_R1.setOption(showOption(numset2, '磁盘占用率'));
    },
    myGraph3( myChart_L1, dataset){
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
          y2: 30  //图表下方空白部分高度
        },
        title: {
          top: '3%',
          left: 'center',
          text: '内存占用率',
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
            return params[0].name + "内存的占用率："+params[0].value+"%";
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
          max:100,
          axisLabel: {
            textStyle: {
              color: '#eeeeee',//坐标值得具体的颜色
            },
            formatter:'{value}%'
          }
        }],
        series: [
          {
            name: '内存占用率',
            type: 'line',
            showSymbol: false,
            data: dataset,
            color: '#409EFF',
            //areaStyle: {}
          }]
      }
      myChart_L1.setOption(option);
    },
    myGraph4( myChart_L1, numset1, numset2){
      var xid = [];
      var numSlice = 30;
      var lenSlice = 1;

      for( var i = 0; i < numSlice*lenSlice; i++) {
        xid.push(((numSlice*lenSlice-i)/lenSlice).toString()+'秒前');
      }
      xid.splice(numSlice*lenSlice-1,1,'现在');

      function showOption( dataset1,dataset2, title) {
        var option = {
          animation: false,
          grid: {
            y2: 30  //图表下方空白部分高度
          },
          title: {
            top: '5%',
            left: 'center',
            text: title,
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
              var relVal = params[0].name;
              for (var i = 0,l=params.length;i<l;i++){
                relVal += '<br/>' + params[i].marker + params[i].seriesName + ': ' + params[i].value + 'KB/s';
              }
              return relVal;
            }
          },
          legend:{
            orient:'vertical',
            x:'right',
            y:'top',
            show:true,
            data:['接收速率','发送速率'],
            textStyle: {
              color: '#FFF',
            },
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
            axisLabel: {
              textStyle: {
                color: '#eeeeee',//坐标值得具体的颜色
              },
              formatter:'{value}KB/s'
            }
          }],
          series: [
            {
              name: '接收速率',
              type: 'line',
              showSymbol: false,
              data: dataset1,
              // areaStyle: {}
            },
            {
              name: '发送速率',
              type: 'line',
              showSymbol: false,
              data: dataset2,
              itemStyle:{
                normal:{
                  lineStyle:{
                    type:'dotted'  //'dotted'虚线 'solid'实线
                  }
                }
              },
            }
          ]
        };return option}
      myChart_L1.setOption(showOption(numset1,numset2,'以太网传输速率'));
    },
    getData() {
      let Graph1 = this.$echarts.init(document.getElementById('graph1'));
      let Graph2 = this.$echarts.init(document.getElementById('graph2'));
      let Graph3 = this.$echarts.init(document.getElementById('graph3'));
      let Graph4 = this.$echarts.init(document.getElementById('graph4'));
      let _this = this;

      //async function
      var numset1 = [];
      var numset2 = [];
      var numset3 = [];
      var numset4 = [];
      var numset5 = [];
      var numSlice = 30;
      var lenSlice = 1;
      for( var i = 0; i < numSlice*lenSlice; i++) {
        numset1.push(0);
        numset2.push(0);
        numset3.push(0);
        numset4.push(0);
        numset5.push(0);
      }

      var flag = 0;
      var NET_recv_last;
      var NET_sent_last;
      const CancelToken = this.$axios.CancelToken

      async function chartsInit() {
        await _this.$axios.get('api/monitor/status',{
          cancelToken: new CancelToken(function executor (c) {
            Vue.$httpRequestList.push(c)
          })
        }).then((res) => {
          //console.log('running mainpage...');
          _this.CPU_percent = res.data.cpu_data.cpu_percent;
          _this.CPU_percent.forEach((item,index) =>{
            _this.CPU_percent[index] = parseFloat(_this.CPU_percent[index])
          })
          _this.DISK_percent = parseFloat(res.data.disk_data.disk_usage.percent);
          _this.MEMORY_percent = parseFloat(res.data.memory_data.basic_info.percent);
          _this.NET_recv = parseFloat(res.data.net_data.bytes_recv);
          _this.NET_sent = parseFloat(res.data.net_data.bytes_sent);
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
          numset2.push(_this.DISK_percent);
          numset3.push(_this.MEMORY_percent);
          if( flag === 0) {
            flag = 1;
            numset4.push(0);
            numset5.push(0);
          }
          else {
            numset4.push(parseFloat(((_this.NET_recv-NET_recv_last) / Math.pow(2, 10)).toFixed(3)));
            numset5.push(parseFloat(((_this.NET_sent-NET_sent_last) / Math.pow(2, 10)).toFixed(3)));
          }
          NET_recv_last = _this.NET_recv;
          NET_sent_last = _this.NET_sent;
            //console.log(ii);
        }

        numset1.splice(0,lenSlice);
        numset2.splice(0,lenSlice);
        numset3.splice(0,lenSlice);
        numset4.splice(0,lenSlice);
        numset5.splice(0,lenSlice);

        _this.myGraph1( Graph1, numset1);
        _this.myGraph2( Graph2, numset2);
        _this.myGraph3( Graph3, numset3);
        _this.myGraph4( Graph4, numset4, numset5);
      }
      chartsInit();

      this.timer = setInterval( function() {
        chartsInit();
      },1000)

      window.onresize = function(){
        Graph1.resize();
        Graph2.resize();
        Graph3.resize();
        Graph4.resize();
      }
    }
  },
  mounted() {
    //this.$nextTick(function() {
    this.getData();//})
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
  height: 45%;
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
  height: 45%;

  border: #333333;
  border-radius: 10px;
  box-shadow: 0 2px 5px black
}
.button{
  color: #eeeeee;
  border: #333333;
  border-radius: 10px;
  box-shadow: 0 2px 5px black
}
</style>
