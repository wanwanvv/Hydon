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
  name: 'disk',
  data() {
    return {
      DISK_io: [0,0,0,0,0,0,0,0,0],
      DISK_usage: [0,0,0,0]
    }
  },
  methods:{
    myEcharts( myChart_R1, numset2){
      var xid = [];
      var numSlice = 30;
      var lenSlice = 1;

      for( var i = 0; i < numSlice*lenSlice; i++) {
        xid.push(((numSlice*lenSlice-i)/lenSlice).toString()+'秒前');
      }
      xid.splice(numSlice*lenSlice-1,1,'现在');

      function showOption( dataset, title) {
        var option = {
          color: '#409EFF',
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
              interval: xid.length/5-1,
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
              formatter:'{value}%',
            }
          }],
          series: [
            {
              name: '实时值',
              type: 'line',
              showSymbol: false,
              data: dataset,
            }]
        };return option}

      myChart_R1.setOption(showOption(numset2,'磁盘占用率'));
    },
    myGraph1( myGraph){
      //var numset = [1477663, 116449878, 5703130];
      var numset = [parseFloat(this.DISK_io.read_time),parseFloat(this.DISK_io.write_time),parseFloat(this.DISK_io.busy_time)];
      var numset_change = [];
      for(let i = 0;i<numset.length;i++){
        if (numset[i] === 0){
          numset_change.push(0);
        }else{
          numset_change.push(Math.log10(numset[i])+1);
        }
      }
      var option = {
        color:'#a0f854',
        tooltip: {
          show:true,
          appendToBody:true,
          formatter(params){
            var dataX = ['磁盘读', '磁盘写', '磁盘处理\nI/O请求']
            return dataX[params.dataIndex]+"的总时间为"+numset[params.dataIndex]+"ms";
          }
        },
        grid: {
          x: '20%'
        },
        title: {
          top: '5%',
          left: 'center',
          text: '磁盘使用总时间情况',
          textStyle: {
            color: '#FFF',
          },
        },
        xAxis: {
          type: 'category',
          data: ['磁盘读', '磁盘写', '磁盘处理\nI/O请求'],
          axisLabel: {
            textStyle: {
              color: '#eeeeee',//坐标值得具体的颜色
            }
          }
        },
        yAxis: {
          type: 'value',
          axisLabel:{
            formatter:function (value){
              var texts = [];
              if (value === 0){
                texts.push(0+"ms");
              }else{
                texts.push("10^"+(value-1)+"ms");
              }
              return texts;
            },
            textStyle: {
              color: '#eeeeee',//坐标值得具体的颜色
            }
          },
        },
        series: [{
          data: numset_change,
          type: 'bar',
          barWidth: 35
        }]
      };
      // 使用刚指定的配置项和数据显示图表。
      myGraph.setOption(option);//})
    },
    myGraph2( myGraph){
      var option = {
        tooltip: {
          trigger: 'item',
          appendToBody: true
        },
        grid: {
          y: '15%'
        },
        title: {
          top: '5%',
          left: 'center',
          text: '磁盘读写总次数情况',
          textStyle: {
            color: '#FFF',
          },
        },
        legend: {
          type: 'scroll',
          orient: 'vertical',
          left: '70%',
          right: '3%',
          top: '40%',
          bottom: 20,
          textStyle: {
            color: '#FFF',
          },
        },
        series: [
          {
            name: '磁盘读写总次数情况',
            type: 'pie',
            radius: ['40%', '70%'],
            center: ['35%','55%'],
            avoidLabelOverlap: false,
            itemStyle: {
              borderRadius: 10,
              borderColor: '#fff',
              borderWidth: 2
            },
            grid:{
              y: '50%'
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
              {value: parseFloat(this.DISK_io.read_count), name: '读'},
              {value: parseFloat(this.DISK_io.read_merged_count), name: '读合并优化'},
              {value: parseFloat(this.DISK_io.write_count), name: '写'},
              {value: parseFloat(this.DISK_io.write_merged_count), name: '写合并优化'}
            ]
          }
        ]
      };
      // 使用刚指定的配置项和数据显示图表。
      myGraph.setOption(option);//})
    },
    myGraph3( myGraph){
      //var numset = [21294252544, 84999361024];
      var numset = [parseFloat((parseFloat(this.DISK_io.read_bytes)/Math.pow(2,30)).toFixed(3)),
        parseFloat((parseFloat(this.DISK_io.write_bytes)/Math.pow(2,30)).toFixed(3))]
      var option = {
        color:'#cf7efa',
        grid:{
          x:'15%'
        },
        xAxis: {
          type: 'category',
          data: ['读总字节数', '写总字节数'],
          axisLabel: {
            textStyle: {
              color: '#eeeeee',//坐标值得具体的颜色
            }
          }
        },
        tooltip: {
          show:true,
          appendToBody:true,
          formatter(params){
            var dataX = ['磁盘读', '磁盘写']
            return dataX[params.dataIndex]+"总字节数为"+numset[params.dataIndex]+"GB";
          }
        },
        title: {
          top: '5%',
          left: 'center',
          text: '磁盘读写总字节数情况',
          textStyle: {
            color: '#FFF',
          },
        },
        yAxis: {
          type: 'value',
          axisLabel:{
            formatter:'{value}GB',
            textStyle: {
              color: '#eeeeee',//坐标值得具体的颜色
            }
          },
        },
        series: [{
          data: numset,
          type: 'bar',
          barWidth:'32%'
        }]
      };
      // 使用刚指定的配置项和数据显示图表。
      myGraph.setOption(option);//})
    },
    getData() {
      let lineGraph = this.$echarts.init(document.getElementById('graph1'));
      let timeGraph = this.$echarts.init(document.getElementById('graph2'));
      let pieGraph = this.$echarts.init(document.getElementById('graph3'));
      let byteGraph = this.$echarts.init(document.getElementById('graph4'));
      let _this = this;

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
          //console.log('running disk...');
            _this.DISK_io = res.data.disk_data.disk_io;
            _this.DISK_usage = res.data.disk_data.disk_usage;
            //console.log(_this.DISK_io,_this.DISK_usage)
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
        //console.log(_this.CPU_time);

        for( var i = 0; i < lenSlice; i++) {
          numset1.push(parseFloat(_this.DISK_usage.percent));
          //console.log(ii);
        }
        numset1.splice(0,lenSlice);

        _this.myEcharts( lineGraph, numset1);
        _this.myGraph1( timeGraph);
        _this.myGraph2( pieGraph);
        _this.myGraph3( byteGraph);
      }
      chartsInit();

      this.timer = setInterval( function() {
        chartsInit();
      },1000)

      window.onresize = function(){
        lineGraph.resize();
        timeGraph.resize();
        pieGraph.resize();
        byteGraph.resize();
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
