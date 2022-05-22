<template>
  <div>
    <el-container>
      <el-header height="2%" width="100%"></el-header>
      <el-main width="100%" height="100%">
        <div class="TopBox" id="graph1"></div>
        <div class="BottomBox_left" id="graph2"></div>
        <div class="BottomBox_middle" id="graph3"></div>
        <div class="BottomBox_right" id="graph4"></div>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import Vue from "vue";

export default {
  name: 'network',
  data() {
    return {
      NET_data: [0,0,0,0,0,0,0,0]
    }
  },
  methods:{
    myEcharts( myChart_L1, numset1, numset2){
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
            x: 40,
            y: 50,
            x2: 40,
            y2: 30, //图表下方空白部分高度
            containLabel:true
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
            axisLabel:{
              textStyle: {
                color: '#eeeeee',//坐标值得具体的颜色
              },
              formatter:'{value}kB/s'
            },
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
    myGraph1( myGraph){
      var option = {
        tooltip: {
          trigger: 'item'
        },
        color:['#e06343','#d0db55'],
        title: {
          top: '5%',
          left: 'center',
          text: '以太网传输丢包情况',
          textStyle: {
            color: '#FFF',
          },
        },
        legend: {
          type: 'scroll',
          orient: 'vertical',
          right: 1,
          top: '40%',
          bottom: 20,
          textStyle: {
            color: '#FFF',
          },
        },
        series: [
          {
            name: '以太网传输丢包情况',
            type: 'pie',
            radius: ['40%', '70%'],
            center: ['38%','55%'],
            avoidLabelOverlap: false,
            itemStyle: {
              borderRadius: 10,
              borderColor: '#fff',
              borderWidth: 2
            },
            label: {
              show: false,
              position: 'center'
            },
            emphasis: {
              label: {
                show: true,
                fontSize: '40',
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: false
            },
            data: [
              {value: parseFloat(this.NET_data.dropin), name: '接收丢包'},
              {value: parseFloat(this.NET_data.dropout), name: '发送丢包'}
            ]
          }
        ]
      };
      // 使用刚指定的配置项和数据显示图表。
      myGraph.setOption(option);//})
    },
    myGraph2( myGraph){
      var option = {
        color:['#37A2DA','#8378EA'],
        tooltip: {
          trigger: 'item'
        },
        title: {
          top: '5%',
          left: 'center',
          text: '以太网传输错误包情况',
          textStyle: {
            color: '#FFF',
          },
        },
        legend: {
          type: 'scroll',
          orient: 'vertical',
          right: 1,
          top: '40%',
          bottom: 20,
          textStyle: {
            color: '#FFF',
          },
        },
        series: [
          {
            name: '以太网传输错误包情况',
            type: 'pie',
            radius: ['40%', '70%'],
            center: ['38%','55%'],
            avoidLabelOverlap: false,
            itemStyle: {
              borderRadius: 10,
              borderColor: '#fff',
              borderWidth: 2
            },
            label: {
              show: false,
              position: 'center'
            },
            emphasis: {
              label: {
                show: true,
                fontSize: '40',
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: false
            },
            data: [
              {value: parseFloat(this.NET_data.errin), name: '接收错误包'},
              {value: parseFloat(this.NET_data.errout), name: '发送错误包'}
            ]
          }
        ]
      };
      // 使用刚指定的配置项和数据显示图表。
      myGraph.setOption(option);//})
    },
    myGraph3( myGraph){
      var option = {
        color:['#37a354', '#b55dba'],
        tooltip: {
          trigger: 'item'
        },
        title: {
          top: '5%',
          left: 'center',
          text: '以太网传输正常包情况',
          textStyle: {
            color: '#FFF',
          },
        },
        legend: {
          type: 'scroll',
          orient: 'vertical',
          right: 1,
          top: '40%',
          bottom: 20,
          textStyle: {
            color: '#FFF',
          },
        },
        series: [
          {
            name: '以太网传输正常包情况',
            type: 'pie',
            radius: ['40%', '70%'],
            center: ['38%','55%'],
            avoidLabelOverlap: false,
            itemStyle: {
              borderRadius: 10,
              borderColor: '#fff',
              borderWidth: 2
            },
            label: {
              show: false,
              position: 'center'
            },
            emphasis: {
              label: {
                show: true,
                fontSize: '40',
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: false
            },
            data: [
              {value: parseFloat(this.NET_data.packets_recv), name: '接收正常包'},
              {value: parseFloat(this.NET_data.packets_sent), name: '发送正常包'}
            ]
          }
        ]
      };
      // 使用刚指定的配置项和数据显示图表。
      myGraph.setOption(option);//})
    },
    getData() {
      let lineGraph = this.$echarts.init(document.getElementById('graph1'));
      let missGraph = this.$echarts.init(document.getElementById('graph2'));
      let errorGraph = this.$echarts.init(document.getElementById('graph3'));
      let normalGraph = this.$echarts.init(document.getElementById('graph4'));
      let _this = this;

      var numset1 = [];
      var numset2 = [];
      var numSlice = 30;
      var lenSlice = 1;
      for( var i = 0; i < numSlice*lenSlice; i++) {
        numset1.push(0);
        numset2.push(0);
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
          //console.log('running network...');
            _this.NET_data = res.data.net_data;
            //console.log(_this.NET_data)
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
        //console.log(_this.CPU_time);

        for( var i = 0; i < lenSlice; i++) {
          if (flag === 0){
            flag = 1;
            numset1.push(0);
            numset2.push(0);
          }else {
            numset1.push(parseFloat((parseFloat(_this.NET_data.bytes_recv - NET_recv_last) / Math.pow(2,10)).toFixed(3)));
            numset2.push(parseFloat((parseFloat(_this.NET_data.bytes_sent - NET_sent_last) / Math.pow(2,10)).toFixed(3)));
          }
          NET_recv_last = _this.NET_data.bytes_recv;
          NET_sent_last = _this.NET_data.bytes_sent;
          //console.log(ii);
        }

        numset1.splice(0,lenSlice);
        numset2.splice(0,lenSlice);

        _this.myEcharts( lineGraph, numset1, numset2);
        _this.myGraph1( missGraph);
        _this.myGraph2( errorGraph);
        _this.myGraph3( normalGraph);
      }
      chartsInit();

      this.timer = setInterval( function() {
        chartsInit();
      },1000)

      window.onresize = function(){
        lineGraph.resize();
        missGraph.resize();
        errorGraph.resize();
        normalGraph.resize();
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
  width: 28%;
  margin-right: 1.2%;
  margin-top: 2%;
  height: 45%;

  border: 1px solid rgb(68,68,68);
  border-radius: 10px;
  box-shadow: 0 2px 5px black
}
.BottomBox_middle{
  float: left;
  width: 28%;
  margin-left: 1.2%;
  margin-right: 1.2%;
  margin-top: 2%;
  height: 45%;

  border: 1px solid rgb(68,68,68);
  border-radius: 10px;
  box-shadow: 0 2px 5px black
}
.BottomBox_right{
  float: right;
  width: 28%;
  margin-left: 1.2%;
  margin-right: 10%;
  margin-top: 2%;
  height: 45%;

  border: 1px solid rgb(68,68,68);
  border-radius: 10px;
  box-shadow: 0 2px 5px black
}
</style>
